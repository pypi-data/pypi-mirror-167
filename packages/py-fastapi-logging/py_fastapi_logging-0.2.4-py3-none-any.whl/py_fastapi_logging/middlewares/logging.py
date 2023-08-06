import json
from collections.abc import Iterable, MutableMapping, MutableSequence
from http import HTTPStatus
from logging import Logger, getLogger
from time import time
from typing import Any, Literal, TypeAlias, cast

from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from starlette.types import ASGIApp

from py_fastapi_logging.config.config import LogConfigure, init_logger
from py_fastapi_logging.constants import REQUEST_ID_HEADER
from py_fastapi_logging.middlewares.utils.request_id import generate_request_id
from py_fastapi_logging.schemas.request import RequestPayload
from py_fastapi_logging.schemas.response import ResponsePayload
from py_fastapi_logging.utils.extra import set_extra_to_environ

_Payload: TypeAlias = RequestPayload | ResponsePayload
_Params: TypeAlias = dict[str, Any] | None


class LoggingMiddleware(BaseHTTPMiddleware):
    _app_name: str
    _prefix: str | None
    _config: LogConfigure | None
    _logger: Logger
    _exclude_requests_starting_with: frozenset[str]
    _marker_filtered: str

    def __init__(
        self,
        app: ASGIApp,
        app_name: str,
        dispatch: DispatchFunction | None = None,
        prefix: str | None = None,
        logger: Logger | None = None,
        exclude_requests_starting_with: Iterable[str] | None = None,
        marker_filtered: str = "[filtered]",
    ) -> None:
        super(LoggingMiddleware, self).__init__(app, dispatch)
        self._app_name = app_name
        self._prefix = prefix
        self._exclude_requests_starting_with = frozenset(exclude_requests_starting_with or ())
        self._marker_filtered = marker_filtered
        if logger is None:
            self._config = init_logger(app_name=app_name)
            self._logger = getLogger("default")
        else:
            self._config, self._logger = None, logger

    @staticmethod
    def get_request_id_header(headers: dict[str, str]) -> str | None:
        for name, value in headers.items():
            if name.casefold() == REQUEST_ID_HEADER.casefold():
                return value

        return None

    @staticmethod
    async def get_protocol(request: Request) -> str:
        protocol: Literal["http", "websocket"] = request.scope["type"]
        http_version: Literal["1.0", "1.1", "2"] = request.scope["http_version"]
        return f"HTTP/{http_version}" if protocol == "http" else ""

    @staticmethod
    async def set_body(request: Request, body: bytes) -> None:
        async def receive() -> dict[str, Any]:
            return {"type": "http.request", "body": body}

        request._receive = receive

    async def get_body(self, request: Request) -> bytes:
        body: bytes = await request.body()
        await self.set_body(request, body)
        return body

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time: float = time()
        request_body: str

        try:
            raw_request_body: bytes = await request.body()
            await self.set_body(request, raw_request_body)
            raw_request_body = await self.get_body(request)
            request_body = raw_request_body.decode()
        except Exception:
            request_body = ""

        request_headers: dict[str, str] = dict(request.headers.items())
        request_id: str = self.get_request_id_header(request_headers) or generate_request_id(prefix=self._prefix)
        set_extra_to_environ("request_id", request_id)

        server: tuple[str, int | None] = request.get("server", ("localhost", 80))
        host_or_socket, port = server

        common_extras: dict[str, str] = {"progname": self._app_name, "request_id": request_id}
        request_log_payload: RequestPayload = RequestPayload(
            method=request.method,
            path=request.url.path,
            params=dict(request_params) if (request_params := request.query_params) else None,
            host=f"{host_or_socket}:{port}" if port is not None else host_or_socket,
            body=request_body,
        )

        extra_payload: dict[str, Any] = common_extras | {
            "tags": ["API", "REQUEST"],
            "payload": self._filter_private_data(request_log_payload),
        }
        self._logger.info(f"REQUEST {request.method} {request.url.path}", extra=extra_payload)

        response: Response
        response_body: bytes
        try:
            response = await call_next(request)
        except Exception as exc:
            response_body = HTTPStatus.INTERNAL_SERVER_ERROR.phrase.encode()
            response = Response(
                content=response_body,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            )
            self._logger.exception("Unexpected error", exc_info=exc)
        else:
            if isinstance(response, StreamingResponse):
                response_body = b""
                async for chunk in response.body_iterator:
                    response_body += chunk
            else:
                response_body = response.body

            response = Response(
                content=response_body,
                status_code=int(response.status_code),
                headers=dict(response.headers),
                media_type=response.media_type,
            )

        if response.status_code >= status.HTTP_400_BAD_REQUEST or not self._is_url_path_in_exclude_list(request):
            duration: int = round((time() - start_time) * 1000.0)
            response_log_payload: ResponsePayload = {
                "status": response.status_code,
                "response_time": f"{duration}ms",
                "response_body": response_body.decode(),
            }
            extra_payload = common_extras | {
                "tags": ["API", "RESPONSE"],
                "payload": self._filter_private_data(response_log_payload),
            }
            self._logger.info(f"RESPONSE {response.status_code} {request.url.path}", extra=extra_payload)

        return response

    def _is_url_path_in_exclude_list(self, request: Request) -> bool:
        return any(request.url.path.startswith(path) for path in self._exclude_requests_starting_with)

    def _filter_private_data(self, payload: _Payload) -> _Payload:
        if not (filtered_fields := LogConfigure.get_exclude_fields(self._config)):
            return payload

        match payload:
            case {"method": _, "path": _, "host": _, "params": params, "body": str(body)} as value:
                payload = cast(RequestPayload, value)
                payload["params"] = self._filter_params(cast(_Params, params), filtered_fields)
                payload["body"] = self._filter_body(body, filtered_fields)
            case {"status": _, "response_time": _, "response_body": str(body)} as value:
                payload = cast(ResponsePayload, value)
                payload["response_body"] = self._filter_body(body, filtered_fields)

        return payload

    def _filter_params(self, params: _Params, filtered_fields: list[str]) -> _Params:
        if not params or not filtered_fields:
            return params

        new_params: dict[str, Any] = params.copy()
        for key in params:
            if key in filtered_fields:
                new_params[key] = self._marker_filtered

        return new_params

    def _filter_body(self, body: str, filtered_fields: list[str]) -> str:
        try:
            request_json: Any = json.loads(body)
            response_json: Any = self._filter_json_body(request_json, filtered_fields)
            return json.dumps(response_json, ensure_ascii=False, separators=(",", ":"))
        except Exception:
            return body

    def _filter_json_body(self, body: Any, filtered_fields: list[str]) -> Any:
        if isinstance(body, MutableMapping):
            return {
                key: self._filter_json_body(value, filtered_fields)
                if key not in filtered_fields
                else self._marker_filtered
                for key, value in body.items()
            }
        elif isinstance(body, MutableSequence):
            return [self._filter_json_body(item, filtered_fields) for item in body]
        else:
            return body
