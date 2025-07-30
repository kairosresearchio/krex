import hmac
import hashlib
import json
import time
import httpx
import logging
from dataclasses import dataclass, field
from typing import Dict, Optional, Any
from urllib.parse import urlencode
from krex.utils.common import Common
from krex.utils.errors import FailedRequestError
from krex.utils.helpers import generate_timestamp
from krex.async_support.product_table.manager import ProductTableManager


@dataclass
class HTTPManager:
    base_url: str = "https://www.bitmex.com"
    api_key: str | None = field(default=None)
    api_secret: str | None = field(default=None)
    timeout: int = field(default=5)
    logger: logging.Logger | None = field(default=None)
    session: httpx.AsyncClient | None = field(default=None, init=False)
    ptm: ProductTableManager | None = field(default=None, init=False)
    preload_product_table: bool = field(default=True)
    last_rate_limit_info: Optional[Dict[str, Any]] = field(default=None, init=False)

    async def async_init(self):
        self.session = httpx.AsyncClient(
            timeout=self.timeout,
            http2=False,
            limits=httpx.Limits(
                max_connections=10,
                max_keepalive_connections=10,
            ),
        )
        self._logger = self.logger or logging.getLogger(__name__)
        self.last_rate_limit_info = None
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.BITMEX)
        return self

    def _sign(self, method: str, path: str, expires: int, body: str = "") -> str:
        """Generate Bitmex API signature according to BitMEX documentation"""
        if self.api_secret is None:
            raise ValueError("api_secret is required for signing requests")
        message = method + path + str(expires) + body
        signature = hmac.new(self.api_secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
        return signature

    def _headers(self, method: str, path: str, body: str = "", signed: bool = True):
        """Generate headers for Bitmex API"""
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        if self.api_key and self.api_secret and signed:
            expires = int(time.time()) + 5  # 5 seconds from now
            signature = self._sign(method, path, expires, body)
            headers.update({"api-key": self.api_key, "api-signature": signature, "api-expires": str(expires)})

        return headers

    async def _request(
        self,
        method,
        path: str,
        query: dict[str, str | int | list[str] | float | bool] | None = None,
        signed: bool = True,
    ):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        response = None
        try:
            url = f"{self.base_url}{path}"
            body = ""
            full_path = path

            if method.upper() == "GET":
                if query:
                    query_string = urlencode(query)
                    url += f"?{query_string}"
                    full_path += f"?{query_string}"
                response = await self.session.get(url, headers=self._headers(method, full_path, signed=signed))
            elif method.upper() == "POST":
                body = json.dumps(query, separators=(",", ":")) if query else ""
                response = await self.session.post(
                    url,
                    headers=self._headers(method, full_path, body, signed=signed),
                    content=body,
                )
            elif method.upper() == "PUT":
                body = json.dumps(query, separators=(",", ":")) if query else ""
                response = await self.session.put(
                    url,
                    headers=self._headers(method, full_path, body, signed=signed),
                    content=body,
                )
            elif method.upper() == "DELETE":
                body = json.dumps(query, separators=(",", ":")) if query else ""
                response = await self.session.request(
                    method="DELETE",
                    url=url,
                    headers=self._headers(method, full_path, body, signed=signed),
                    content=body,
                )
            else:
                raise ValueError(f"Unsupported method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            timestamp = generate_timestamp(iso_format=True)

            if not response.status_code // 100 == 2:
                error_message = (
                    data.get("error", {}).get("message", "Unknown error") if isinstance(data, dict) else response.text
                )
                raise FailedRequestError(
                    request=f"{method} {url} | Body: {query}",
                    message=f"BITMEX API Error: {error_message}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            self._update_rate_limit_info(response.headers)

            return data

        except httpx.RequestError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Params: {query}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp if "timestamp" in locals() else "Unknown",
                resp_headers=response.headers if response else None,
            )

    def _update_rate_limit_info(self, headers: httpx.Headers):
        if "x-ratelimit-remaining" in headers:
            self.last_rate_limit_info = {
                "limit": headers.get("x-ratelimit-limit"),
                "remaining": headers.get("x-ratelimit-remaining"),
                "reset": headers.get("x-ratelimit-reset"),
                "remaining-1s": headers.get("x-ratelimit-remaining-1s"),
            }

    def get_rate_limit_info(self) -> Optional[Dict[str, Any]]:
        return self.last_rate_limit_info
