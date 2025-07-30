import hmac
import time
import base64
import httpx
import logging
import json
import hashlib
from dataclasses import dataclass, field
from urllib.parse import urlencode

from krex.utils.common import Common
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp


def _sign(plain: bytes, key: bytes) -> str:
    """KuCoin signature generation using HMAC-SHA256"""
    hm = hmac.new(key, plain, hashlib.sha256)
    return base64.b64encode(hm.digest()).decode()


@dataclass
class HTTPManager:
    base_url: str = field(default="https://api.kucoin.com")
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    passphrase: str = field(default=None)
    timeout: int = field(default=10)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(default=None, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)
    _encrypted_passphrase: str = field(default=None, init=False)

    async def async_init(self):
        """Initialize async HTTP manager"""
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)

        # Encrypt passphrase if credentials are provided
        if self.passphrase and self.api_secret:
            self._encrypted_passphrase = _sign(self.passphrase.encode("utf-8"), self.api_secret.encode("utf-8"))

        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.KUCOIN)
        return self

    def _generate_headers(self, timestamp: str, signature: str) -> dict:
        """Generate headers for KuCoin API requests"""
        headers = {
            "Content-Type": "application/json",
        }

        if self.api_key and signature and self._encrypted_passphrase:
            headers.update(
                {
                    "KC-API-KEY": self.api_key,
                    "KC-API-SIGN": signature,
                    "KC-API-TIMESTAMP": timestamp,
                    "KC-API-PASSPHRASE": self._encrypted_passphrase,
                    "KC-API-KEY-VERSION": "2",
                }
            )

        return headers

    def _create_signature_payload(self, timestamp: str, method: str, path: str, body: str) -> str:
        """Create the payload for signature generation according to KuCoin API v2"""
        # For KuCoin API v2, the signature payload is: timestamp + method + path + body
        return f"{timestamp}{method.upper()}{path}{body}"

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        """Make HTTP request to KuCoin API"""
        if self.session is None or self.session.is_closed:
            await self.async_init()

        # Prepare request data
        timestamp = str(int(time.time() * 1000))
        body = ""
        request_path = path
        signature_path = path

        # Handle different HTTP methods
        if method.upper() == "GET":
            if query:
                request_path = f"{path}?{urlencode(query)}"
                signature_path = f"{path}?{urlencode(query)}"  # GET: include query params in signature
        elif method.upper() in ["POST", "PUT"]:
            body = json.dumps(query) if query else ""
            # POST/PUT/DELETE: don't include query params in signature path
            signature_path = path
        elif method.upper() == "DELETE":
            if query:
                query_string = urlencode(query)
                request_path = f"{path}?{query_string}"
                signature_path = f"{path}?{query_string}"
            else:
                request_path = path
                signature_path = path

        # Generate signature if needed
        signature = ""
        if signed:
            if not (self.api_key and self.api_secret and self.passphrase):
                raise ValueError("Signed request requires API Key, Secret, and Passphrase.")

            # Create signature payload
            payload = self._create_signature_payload(timestamp, method, signature_path, body)
            signature = _sign(payload.encode("utf-8"), self.api_secret.encode("utf-8"))

        response = None
        try:
            url = f"{self.base_url}{request_path}"
            headers = self._generate_headers(timestamp, signature)

            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, content=body)
            elif method.upper() == "PUT":
                response = await self.session.put(url, headers=headers, content=body)
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
