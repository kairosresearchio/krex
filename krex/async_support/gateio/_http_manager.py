import hmac
import json
import time
import httpx
import logging
import hashlib
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.common import Common


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    base_url: str = field(default="https://api.gateio.ws")
    logger: logging.Logger = field(default=None)
    timeout: int = field(default=10)
    session: httpx.AsyncClient = field(default=None, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.GATEIO)
        return self

    def _resolve_path(self, path_template, path_params: dict = None) -> str:
        if isinstance(path_template, Enum):
            path_template = path_template.value
        try:
            return path_template.format(**(path_params or {}))
        except KeyError as e:
            raise ValueError(f"Missing path parameter: {e}")

    def _sign(self, method: str, url_path: str, query: Optional[dict], body: Optional[dict], timestamp: str) -> str:
        payload_string = json.dumps(body or {}, separators=(",", ":")) if body else ""
        hashed_payload = hashlib.sha512(payload_string.encode("utf-8")).hexdigest()

        query_string = ""
        if query:
            query_string = "&".join(f"{k}={v}" for k, v in sorted(query.items()))

        s = f"{method.upper()}\n{url_path}\n{query_string}\n{hashed_payload}\n{timestamp}"
        return hmac.new(self.api_secret.encode("utf-8"), s.encode("utf-8"), hashlib.sha512).hexdigest()

    async def _request(
        self,
        method: str,
        path: str,
        path_params: Optional[dict] = None,
        query: Optional[dict] = None,
        body: Optional[dict] = None,
        signed: bool = True,
    ):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        query = query or {}
        body = body or {}

        resolved_path = self._resolve_path(path, path_params)
        full_path = "/api/v4" + resolved_path
        url = self.base_url + full_path

        timestamp = str(int(time.time()))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")
            sign = self._sign(method, full_path, query, body, timestamp)
            headers.update(
                {
                    "KEY": self.api_key,
                    "Timestamp": timestamp,
                    "SIGN": sign,
                }
            )

        try:
            method_upper = method.upper()
            body_string = None
            if method_upper in ("POST", "PUT", "PATCH"):
                body_string = json.dumps(body, separators=(",", ":"))

            if method_upper == "GET":
                response = await self.session.get(url, headers=headers, params=query)
            elif method_upper == "POST":
                response = await self.session.post(url, headers=headers, params=query, content=body_string)
            elif method_upper == "PUT":
                response = await self.session.put(url, headers=headers, params=query, content=body_string)
            elif method_upper == "DELETE":
                response = await self.session.delete(url, headers=headers, params=query)
            elif method_upper == "PATCH":
                response = await self.session.patch(url, headers=headers, params=query, content=body_string)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            if response.status_code // 100 == 2:
                return response.json()

            raise FailedRequestError(
                request=f"{method_upper} {url}",
                message=f"GATEIO API Error: {response.status_code}, {response.text}",
                status_code=response.status_code,
                time=timestamp,
                resp_headers=dict(response.headers),
            )

        except FailedRequestError:
            raise
        except Exception as e:
            raise FailedRequestError(
                request=f"{method_upper} {url}",
                message=f"Request failed: {e}",
                status_code="unknown",
                time=timestamp,
                resp_headers={},
            )
