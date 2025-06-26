import hmac
import hashlib
import time
import base64
import httpx
import logging
from dataclasses import dataclass, field
from urllib.parse import urlencode
from .endpoints.market import SpotMarket
from .endpoints.trade import SpotTrade
from .endpoints.account import SpotAccount
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.common import Common


def _sign(message: str, secret_key: str) -> str:
    """KuCoin signature generation"""
    mac = hmac.new(
        bytes(secret_key, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    return base64.b64encode(mac.digest()).decode()


def _get_kucoin_signature(timestamp: str, method: str, path: str, body: str, secret_key: str) -> str:
    """Generate KuCoin API signature"""
    message = f"{timestamp}{method.upper()}{path}{body}"
    return _sign(message, secret_key)


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    passphrase: str = field(default=None)
    timeout: int = field(default=10)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(default=None, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    # KuCoin API base URL
    base_url: str = field(default="https://api.kucoin.com")

    # API path mapping for different endpoints
    api_map = {
        "https://api.kucoin.com": {
            SpotMarket,
            SpotTrade,
            SpotAccount,
        },
    }

    async def async_init(self):
        """Initialize async HTTP manager"""
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.KUCOIN)
        return self

    def _get_base_url(self, path):
        """Get base URL for the given API path"""
        for base_url, enums in self.api_map.items():
            if type(path) in enums:
                return base_url
        raise ValueError(f"Unknown API path: {path} (type={type(path)})")

    def _headers(self, signed: bool = False, timestamp: str = None, signature: str = None, passphrase: str = None):
        """Generate headers for KuCoin API requests"""
        headers = {
            "Content-Type": "application/json",
        }
        
        if signed and self.api_key and signature and passphrase:
            headers.update({
                "KC-API-KEY": self.api_key,
                "KC-API-SIGN": signature,
                "KC-API-TIMESTAMP": timestamp,
                "KC-API-PASSPHRASE": passphrase,
                "KC-API-KEY-VERSION": "2",  # KuCoin API v2
            })
        
        return headers

    async def _request(self, method: str, path: str, query: dict = None, signed: bool = True):
        """Make HTTP request to KuCoin API"""
        if not self.session:
            await self.async_init()

        if query is None:
            query = {}

        # Prepare request data
        timestamp = str(int(time.time() * 1000))
        body = ""
        
        if method.upper() == "GET":
            if query:
                path += f"?{urlencode(query)}"
        elif method.upper() in ["POST", "PUT", "DELETE"]:
            body = str(query) if query else ""

        # Generate signature if needed
        signature = ""
        passphrase_encrypted = ""
        
        if signed:
            if not (self.api_key and self.api_secret and self.passphrase):
                raise ValueError("Signed request requires API Key, Secret, and Passphrase.")
            
            signature = _get_kucoin_signature(timestamp, method, path, body, self.api_secret)
            # Encrypt passphrase for KuCoin API v2
            passphrase_encrypted = _sign(self.passphrase, self.api_secret)

        response = None
        try:
            base_url = self._get_base_url(path)
            url = f"{base_url}{path}"
            
            headers = self._headers(signed, timestamp, signature, passphrase_encrypted)
            
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=query)
            elif method.upper() == "PUT":
                response = await self.session.put(url, headers=headers, json=query)
            elif method.upper() == "DELETE":
                response = await self.session.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            timestamp = generate_timestamp(iso_format=True)

            # Check for KuCoin API errors
            if isinstance(data, dict) and data.get("code") != "200000":
                code = data.get("code", "Unknown")
                error_message = data.get("msg", "Unknown error")
                raise FailedRequestError(
                    request=f"{method} {url} | Body: {query}",
                    message=f"KUCOIN API Error: [{code}] {error_message}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            # Check HTTP status code
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
                request=f"{method.upper()} {url} | Body: {query}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )

    async def close(self):
        """Close the HTTP session"""
        if self.session:
            await self.session.aclose() 