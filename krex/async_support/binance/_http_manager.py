import hmac
import hashlib
import time
import httpx
import logging
from dataclasses import dataclass, field
from urllib.parse import urlencode
from .endpoints.market import FuturesMarket, SpotMarket
from .endpoints.trade import FuturesTrade, SpotTrade
from .endpoints.account import FuturesAccount, SpotAccount
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.common import Common


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    timeout: int = field(default=10)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(default=None, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    api_map = {
        "https://fapi.binance.com": {
            FuturesTrade,
            FuturesMarket,
            FuturesAccount,
        },
        "https://api.binance.com": {
            SpotMarket,
            SpotTrade,
            SpotAccount,
        },
    }

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.BINANCE)
        return self

    def _get_base_url(self, path):
        for base_url, enums in self.api_map.items():
            if type(path) in enums:
                return base_url
        raise ValueError(f"Unknown API path: {path} (type={type(path)})")

    def _sign(self, params: dict) -> str:
        query_string = urlencode(params)
        return hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    def _headers(self):
        return {"X-MBX-APIKEY": self.api_key} if self.api_key else {}

    async def _request(self, method, path, query: dict = None, signed: bool = True):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        if query is None:
            query = {}

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")
            query["timestamp"] = int(time.time() * 1000)
            query["recvWindow"] = 5000
            query["signature"] = self._sign(query)

        response = None
        try:
            base_url = self._get_base_url(path)
            url = f"{base_url}{path}"
            if method.upper() == "GET":
                url += f"?{urlencode(query)}" if query else ""
                response = await self.session.get(url, headers=self._headers())
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=self._headers(), data=query)
            elif method.upper() == "DELETE":
                url += f"?{urlencode(query)}" if query else ""
                response = await self.session.delete(url, headers=self._headers())
            else:
                raise ValueError(f"Unsupported method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            timestamp = generate_timestamp(iso_format=True)

            if isinstance(data, dict) and "code" in data and str(data["code"]) != "200":
                code = data.get("code", "Unknown")
                error_message = data.get("msg", "Unknown error")
                raise FailedRequestError(
                    request=f"{method} {url} | Body: {query}",
                    message=f"BINANCE API Error: [{code}] {error_message}",
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

        except httpx.RequestError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Params: {query}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=query.get("timestamp", "Unknown"),
                resp_headers=response.headers if response else None,
            )
