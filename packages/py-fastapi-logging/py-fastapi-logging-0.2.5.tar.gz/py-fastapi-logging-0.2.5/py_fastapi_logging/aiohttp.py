import logging
from time import time
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any, NamedTuple, TypeAlias

from multidict import MultiDict
from yarl import URL

try:
    from aiohttp import TraceConfig
except ImportError as exc:
    raise ImportError("Using this module requires the aiohttp library.") from exc

if TYPE_CHECKING:
    from aiohttp import ClientSession, TraceRequestChunkSentParams, TraceRequestEndParams, TraceRequestStartParams

    _ParamsDict: TypeAlias = dict[str, str | list[str]]


class _Request(NamedTuple):
    service_name: str | None
    request_id: str | None
    method: str
    url: URL
    start_time: float


def create_logging_trace_config(service_name: str | None) -> TraceConfig:
    def context_factory(**kwargs: Any) -> SimpleNamespace:
        return SimpleNamespace(service_name=service_name, **kwargs)

    trace_config: TraceConfig = TraceConfig(context_factory)  # type: ignore[arg-type]
    trace_config.on_request_start.append(_on_request_start)
    trace_config.on_request_chunk_sent.append(_on_request_chunk_sent)
    trace_config.on_request_end.append(_on_request_end)
    return trace_config


def _convert_params_to_dict(params_mulitdict: MultiDict) -> "_ParamsDict":
    params_dict: "_ParamsDict" = {}
    for key in params_mulitdict.keys():
        values = params_mulitdict.getall(key)
        params_dict[key] = values[0] if len(values) == 1 else values
    return params_dict


def _make_tags_list(*tags: str | None) -> list[str]:
    return list(filter(None, tags))


async def _on_request_start(
    session: "ClientSession",
    context: SimpleNamespace,
    params: "TraceRequestStartParams",
) -> None:
    context.request = _Request(
        service_name=context.service_name,
        request_id=params.headers.get("X-Request-Id"),
        method=params.method,
        url=params.url,
        start_time=time(),
    )


async def _on_request_chunk_sent(
    session: "ClientSession",
    context: SimpleNamespace,
    params: "TraceRequestChunkSentParams",
) -> None:
    request: _Request = context.request
    try:
        request_body = params.chunk.decode("utf-8")
    except Exception:
        logging.exception("Failed to decode request body")
        request_body = "(failed to decode)"

    logging.info(
        f"Request {request.method} {request.url}",
        extra={
            "tags": _make_tags_list("SERVICE", request.service_name, "REQUEST"),
            "request_id": request.request_id,
            "payload": {
                "method": request.method,
                "url": str(request.url.with_query(None)),
                "params": _convert_params_to_dict(request.url.query),
                "body": request_body,
            },
        },
    )


async def _on_request_end(
    session: "ClientSession",
    context: SimpleNamespace,
    params: "TraceRequestEndParams",
) -> None:
    request: _Request = context.request
    request_time_ms: int = round((time() - request.start_time) * 1000)
    logging.info(
        f"Response {request.method} {request.url}",
        extra={
            "tags": _make_tags_list("SERVICE", request.service_name, "RESPONSE"),
            "request_id": request.request_id,
            "payload": {
                "status": params.response.status,
                "response_time": f"{request_time_ms}ms",
                "response_body": await params.response.text(),
            },
        },
    )
