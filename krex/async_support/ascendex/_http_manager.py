import hmac
import hashlib
import logging
import json
import httpx
from dataclasses import dataclass, field

from krex.utils.common import Common
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from .endpoints.account import CashAccount

HTTP_URL = "https://ascendex.com"


def get_header(api_key, signature, timestamp):
    return {
        "Content-Type": "application/json",
        "x-auth-key": str(api_key),
        "x-auth-timestamp": str(timestamp),
        "x-auth-signature": str(signature),
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
    account_group: str = field(default=None)

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.ASCENDEX)
        self.endpoint = HTTP_URL

        return self

    def _auth(self, path, timestamp):
        """Generate signature for AscendEX API
        Signature format: HMAC-SHA256(timestamp + path, secret_key)
        """
        param_str = f"{timestamp}+{path}"
        return hmac.new(self.api_secret.encode(), param_str.encode(), hashlib.sha256).hexdigest()

    async def _fetch_account_group_raw(self):
        url = self.endpoint + CashAccount.ACCOUNT_INFO
        timestamp = generate_timestamp()
        sign_path = CashAccount.ACCOUNT_INFO.hash
        signature = self._auth(sign_path, timestamp)
        headers = get_header(self.api_key, signature, timestamp)
        async with httpx.AsyncClient(timeout=self.timeout) as session:
            response = await session.get(url, headers=headers)
            data = response.json()
            if data.get("code", 0) == 0 and "data" in data:
                return data["data"].get("accountGroup")
            else:
                raise ValueError("Failed to fetch account group: " + str(data))

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
        hash_path: str = None,
    ):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        path = await self._resolve_path(path)

        timestamp = generate_timestamp()

        url = self.endpoint + path
        payload = ""

        if method.upper() == "GET" or method.upper() == "DELETE":
            if query:
                sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
                url += "?" + sorted_query if sorted_query else ""
                payload = sorted_query
        else:
            payload = json.dumps(query, separators=(",", ":"), ensure_ascii=False)

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")

            sign_path = hash_path if hash_path else path
            signature = self._auth(sign_path, timestamp)
            headers = get_header(self.api_key, signature, timestamp)
        else:
            headers = get_header_no_sign()

        try:
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=query if query else {})
            elif method.upper() == "DELETE":
                response = await self.session.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if data.get("code", 0) != 0:
                code = data.get("code", "Unknown")
                error_message = data.get("message", "Unknown error")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"AscendEX API Error: [{code}] {error_message}",
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

        except httpx.ConnectError as e:
            # Handle connection errors specifically
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Connection failed: {str(e)}",
                status_code="Connection Error",
                time=timestamp,
                resp_headers=None,
            )
        except httpx.HTTPError as e:
            # Handle other HTTP errors
            status_code = getattr(e.request, "status_code", "Unknown") if hasattr(e, "response") else "Unknown"
            resp_headers = getattr(e.request, "headers", None) if hasattr(e, "response") else None

            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Request failed: {str(e)}",
                status_code=status_code,
                time=timestamp,
                resp_headers=resp_headers,
            )

    async def _resolve_path(self, path: str) -> str:
        """Resolve dynamic path parameters like {ACCOUNT_GROUP}"""
        if "{ACCOUNT_GROUP}" in path:
            if not self.account_group:
                self.account_group = await self._fetch_account_group_raw()
            return path.replace("{ACCOUNT_GROUP}", str(self.account_group))
        return path
