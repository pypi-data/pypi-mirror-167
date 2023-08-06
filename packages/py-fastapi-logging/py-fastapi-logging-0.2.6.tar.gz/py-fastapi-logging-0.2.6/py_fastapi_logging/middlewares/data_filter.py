import cgi
import json
import logging
import re
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence
from typing import Any

from py_fastapi_logging.schemas.request import RequestPayload
from py_fastapi_logging.schemas.response import ResponsePayload


class DataFilter:
    _filtered_fields: Iterable
    _marker_filtered: str
    _multipart_body_part_pattern: re.Pattern
    _url_encoded_body_pattern: re.Pattern

    def __init__(self, filtered_fields: Iterable, marker_filtered: str) -> None:
        self._filtered_fields = filtered_fields
        self._marker_filtered = marker_filtered

        fields_regex = "|".join(self._filtered_fields)
        self._multipart_body_part_pattern = re.compile(
            rf"(^[\r\n]*Content-Disposition: *form-data; *name=\"(?:{fields_regex})\".*?[\r\n]+).*?(\r\n|\r|\n)$",
            flags=re.DOTALL + re.IGNORECASE,
        )
        self._url_encoded_body_pattern = re.compile(rf"\b({fields_regex})=[^&]*")

    def filter_request_payload(self, payload: RequestPayload, headers: Mapping) -> None:
        if self._filtered_fields:
            try:
                payload["params"] = self._filter_data(payload["params"])
                payload["body"] = self._filter_request_body(payload["body"], headers)
            except Exception:
                logging.exception("Failed to filter response payload")

    def filter_response_payload(self, payload: ResponsePayload) -> None:
        if self._filtered_fields:
            try:
                payload["response_body"] = self._filter_json_body(payload["response_body"])
            except Exception:
                logging.exception("Failed to filter request payload")

    def _filter_request_body(self, body: str, headers: Mapping) -> str:
        if content_type := headers.get("content-type"):
            media_type, content_options = cgi.parse_header(content_type)
            if media_type == "multipart/form-data" and (boundary := content_options.get("boundary")):
                return self._filter_multipart_body(body, boundary)

        if self._is_json_body(body):
            return self._filter_json_body(body)

        return self._filter_url_encoded_body(body)

    def _is_json_body(self, body: str) -> bool:
        return body.startswith(("[", "{"))

    def _filter_json_body(self, body: str) -> str:
        request_json: Any = json.loads(body)
        response_json: Any = self._filter_data(request_json)
        return json.dumps(response_json, ensure_ascii=False, separators=(",", ":"))

    def _filter_data(self, data: Any) -> Any:
        if isinstance(data, MutableMapping):
            return {
                key: self._filter_data(value) if key not in self._filtered_fields else self._marker_filtered
                for key, value in data.items()
            }
        elif isinstance(data, MutableSequence):
            return list(map(self._filter_data, data))
        else:
            return data

    def _filter_url_encoded_body(self, body: str) -> str:
        return self._url_encoded_body_pattern.sub(r"\1=[filtered]", body)

    def _filter_multipart_body(self, body: str, boundary: str) -> str:
        separator = f"--{boundary}"
        filtered_parts = map(
            self._filter_multipart_body_part,
            body.split(separator),
        )
        return separator.join(filtered_parts)

    def _filter_multipart_body_part(self, part: str) -> str:
        return self._multipart_body_part_pattern.sub(rf"\1{self._marker_filtered}\2", part)
