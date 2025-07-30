import json
import hmac
import base64
import logging
import httpx
from dataclasses import dataclass, field
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.common import Common


def _sign(message, secretKey):
    mac = hmac.new(
        bytes(secretKey, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    d = mac.digest()
    return base64.b64encode(d).decode()


def pre_hash(timestamp, method, path, body):
    return str(timestamp) + str.upper(method) + path + body


def get_header(api_key, sign, timestamp, passphrase, flag):
    return {
        "Content-Type": "application/json",
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": sign,
        "OK-ACCESS-TIMESTAMP": str(timestamp),
        "OK-ACCESS-PASSPHRASE": passphrase,
        "x-simulated-trading": flag,
    }


def get_header_no_sign(flag):
    return {
        "Content-Type": "application/json",
        "x-simulated-trading": flag,
    }


def parse_params_to_str(query):
    url = "?"
    for key, value in query.items():
        if value != "":
            url += f"{key}={value}&"
    return url.rstrip("&")


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    passphrase: str = field(default=None)
    flag: str = field(default="0")
    base_api: str = field(default="https://www.okx.com")
    timeout: int = field(default=10)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.OKX)
        return self

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        if query is None:
            query = {}

        if method.upper() == "GET" and query:
            path += parse_params_to_str(query)

        timestamp = generate_timestamp(iso_format=True)
        body = query if method.upper() == "POST" else ""
        body_str = json.dumps(body, separators=(",", ":"), ensure_ascii=False) if isinstance(body, (dict, list)) else ""

        if signed:
            if not (self.api_key and self.api_secret and self.passphrase):
                raise ValueError("Signed request requires API Key and Secret and Passphrase.")
            sign = _sign(pre_hash(timestamp, method.upper(), path, body_str), self.api_secret)
            headers = get_header(self.api_key, sign, timestamp, self.passphrase, self.flag)
        else:
            headers = get_header_no_sign(self.flag)

        url = self.base_api + path

        try:
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=body)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if data.get("code", "0") != "0":
                code = data.get("code", "Unknown")
                error_message = data.get("msg", "Unknown error")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"OKX API Error: [{code}] {error_message}",
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
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )
