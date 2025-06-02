import hmac
import json
import logging
import requests
import hashlib
from dataclasses import dataclass, field
from .endpoints.account import FundingAccount, FuturesAccount
from .endpoints.market import FuturesMarket, SpotMarket
from .endpoints.trade import FuturesTrade, SpotTrade
from ..product_table.manager import ProductTableManager
from ..utils.errors import FailedRequestError
from ..utils.helpers import generate_timestamp
from ..utils.common import Common


def sign_message(timestamp, memo, body, secret_key):
    message = f"{timestamp}#{memo}#{body}"
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()


def get_header(api_key, sign, timestamp, memo):
    return {
        "Content-Type": "application/json",
        "X-BM-KEY": api_key,
        "X-BM-SIGN": sign,
        "X-BM-TIMESTAMP": str(timestamp),
        "X-BM-MEMO": memo,
    }


def get_header_no_sign():
    return {"Content-Type": "application/json"}


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    memo: str = field(default=None)
    timeout: int = field(default=10)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    api_map = {
        "https://api-cloud.bitmart.com": {
            SpotTrade,
            SpotMarket,
            FundingAccount,
        },  # v1 API
        "https://api-cloud-v2.bitmart.com": {
            FuturesTrade,
            FuturesMarket,
            FuturesAccount,
        },  # v2 API
    }

    def __post_init__(self):
        if self.logger is None:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = self.logger

        if self.preload_product_table:
            self.ptm = ProductTableManager.get_instance(Common.BITMART)

    def _get_base_url(self, path):
        for base_url, enums in self.api_map.items():
            if type(path) in enums:
                return base_url
        raise ValueError(f"Unknown API path: {path} (type={type(path)})")

    def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if query is None:
            query = {}

        base_url = self._get_base_url(path)
        url = base_url + path.value

        if method.upper() == "GET" and query:
            params_str = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
            url = f"{url}?{params_str}"

        timestamp = generate_timestamp()

        if signed:
            if not (self.api_key and self.api_secret and self.memo):
                raise ValueError("Signed request requires API Key and Secret and Memo.")
            sign = sign_message(timestamp, self.memo, json.dumps(query), self.api_secret)
            headers = get_header(self.api_key, sign, timestamp, self.memo)
        else:
            headers = get_header_no_sign()

        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers, timeout=self.timeout)
            elif method.upper() == "POST":
                response = self.session.post(
                    url,
                    json=query if query else {},
                    headers=headers,
                    timeout=self.timeout,
                )
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if data.get("code", 0) != 1000:
                code = data.get("code", "Unknown")
                error_msg = data.get("message", "Unknown error")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"BitMart API Error: [{code}] {error_msg}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            # If http status is not 2xx (like 403, 404)
            if not response.status_code // 100 == 2:
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"HTTP Error {response.status_code}: {response.text}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            return data

        except requests.exceptions.RequestException as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {query}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )
