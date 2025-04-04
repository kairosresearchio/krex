import hmac
import hashlib
import time
import json
import requests
import logging
from dataclasses import dataclass, field
from urllib.parse import urlencode
from .endpoints.market import FuturesMarket
from .endpoints.trade import FuturesTrade
from .endpoints.account import FuturesAccount
from ..utils.errors import FailedRequestError
from ..product_table.manager import ProductTableManager


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    timeout: int = field(default=10)
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)

    api_map = {
        "https://fapi.binance.com": {
            FuturesTrade,
            FuturesMarket,
            FuturesAccount,
        },
        "https://api.binance.com": {},
    }
            

    def __post_init__(self):
        if self.logger is None:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = self.logger

        self.ptm = ProductTableManager.get_instance()
    
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

    def _request(self, method, path, query: dict = None, signed: bool = False):
        if query is None:
            query = {}

        if signed:
            query["timestamp"] = int(time.time() * 1000)
            query["recvWindow"] = 5000
            query["signature"] = self._sign(query)

        base_url = self._get_base_url(path)
        url = f"{base_url}{path}"
        if method.upper() == "GET":
            url += f"?{urlencode(query)}" if query else ""
            request_func = self.session.get
        elif method.upper() == "POST":
            request_func = self.session.post
        elif method.upper() == "DELETE":
            request_func = self.session.delete
        elif method.upper() == "PUT":
            request_func = self.session.put
        else:
            raise ValueError(f"Unsupported method: {method}")

        try:
            response = request_func(url, headers=self._headers(), timeout=self.timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Params: {query}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=query.get("timestamp", "Unknown"),
                resp_headers=response.headers if response else None,
            )