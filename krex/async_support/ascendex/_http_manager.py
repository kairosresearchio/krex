import hmac
import hashlib
import logging
import json
import httpx
from dataclasses import dataclass, field
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.common import Common

HTTP_URL = "https://ascendex.com"


def get_header(api_key, signature, timestamp):
    return {
        "Content-Type": "application/json",
        "x-auth-key": api_key,
        "x-auth-timestamp": timestamp,
        "x-auth-signature": signature,
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

        # Fetch account group if API credentials are provided
        if self.api_key and self.api_secret:
            await self._fetch_account_group()

        return self

    async def _fetch_account_group(self):
        """Fetch the account group required for authenticated endpoints"""
        try:
            # Use the account info endpoint to get account group
            from .endpoints.account import CashAccount

            response = await self._request(
                method="GET",
                path=CashAccount.ACCOUNT_INFO,
                signed=True,
            )

            # Extract account group from response
            if response and "data" in response:
                self.account_group = response["data"].get("accountGroup")
                if not self.account_group:
                    raise ValueError("Account group not found in API response")
                self._logger.info(f"Account group fetched: {self.account_group}")
            else:
                raise ValueError("Invalid response format when fetching account group")

        except Exception as e:
            self._logger.error(f"Failed to fetch account group: {e}")
            raise ValueError(f"Could not initialize AscendEX client: {e}")

    def _resolve_path(self, path: str) -> str:
        """Resolve dynamic path parameters like {ACCOUNT_GROUP}"""
        if "{ACCOUNT_GROUP}" in path:
            if not self.account_group:
                raise ValueError("Account group not available. Ensure client is properly initialized.")
            return path.replace("{ACCOUNT_GROUP}", self.account_group)
        return path

    def _auth(self, path, timestamp):
        param_str = f"{timestamp}{path}"
        return hmac.new(self.api_secret.encode(), param_str.encode(), hashlib.sha256).hexdigest()

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

        if method.upper() == "GET":
            if query:
                sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
                path += "?" + sorted_query if sorted_query else ""
                payload = sorted_query
            else:
                payload = ""
        else:
            payload = json.dumps(query, separators=(",", ":"), ensure_ascii=False)

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")
            if self.account_group is None:
                await self._fetch_account_group()
            signature = self._auth(path["hash"], timestamp)
            headers = get_header(self.api_key, signature, timestamp)
            route = self._resolve_path(path["route"])
        else:
            headers = get_header_no_sign()
            route = path["route"]

        url = self.endpoint + route

        try:
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=query if query else {})
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            # Note: AscendEX uses different error format than Bybit
            # Adjust error handling based on AscendEX API documentation
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

        except httpx.HTTPError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", "Unknown"),
                time=timestamp,
                resp_headers=getattr(e.response, "headers", None),
            )
