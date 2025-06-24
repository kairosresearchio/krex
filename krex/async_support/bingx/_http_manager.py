import hmac
import hashlib
import logging
import httpx
from dataclasses import dataclass, field
from urllib.parse import urlencode
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.common import Common


def get_header(api_key, signature, timestamp):
    return {
        "Content-Type": "application/json",
        "X-BX-APIKEY": api_key,
        "X-BX-SIGNATURE": signature,
        "X-BX-TIMESTAMP": str(timestamp),
    }


def get_header_no_sign():
    return {"Content-Type": "application/json"}


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    timeout: int = field(default=10)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)
    base_url: str = field(default="https://open-api.bingx.com")

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.BINGX)
        return self

    def _sign(self, params: dict) -> str:
        signing_params = {k: v for k, v in params.items() if k != "signature" and v is not None and v != ""}
        sorted_params = dict(sorted(signing_params.items()))
        query_string = urlencode(sorted_params)
        return hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if not self.session:
            await self.async_init()

        if query is None:
            query = {}

        timestamp = generate_timestamp()

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")
            query["apiKey"] = self.api_key
            query["timestamp"] = timestamp
            query["signature"] = self._sign(query)
            headers = get_header(self.api_key, query["signature"], timestamp)
        else:
            headers = get_header_no_sign()

        url = self.base_url + path

        try:
            if method.upper() == "GET":
                if query:
                    sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
                    url += "?" + sorted_query if sorted_query else ""
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=query if query else {})
            elif method.upper() == "PUT":
                response = await self.session.put(url, headers=headers, json=query if query else {})
            elif method.upper() == "DELETE":
                response = await self.session.delete(url, headers=headers, json=query if query else {})
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if data.get("code", 0) != 0:
                code = data.get("code", "Unknown")
                error_message = data.get("msg", "Unknown error")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"BingX API Error: [{code}] {error_message}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            if not response.status_code // 100 == 2:
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"HTTP Error {response.status_code}: {response.text}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            return data

        except httpx.HTTPError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {query}",
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", "Unknown"),
                time=timestamp,
                resp_headers=getattr(e.response, "headers", None),
            )
