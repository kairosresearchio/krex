import hmac
import hashlib
import logging
import httpx
import time
from dataclasses import dataclass, field
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.common import Common


def get_header(api_key):
    return {
        "X-BX-APIKEY": api_key,
    }


def get_header_no_sign():
    return {"Content-Type": "application/json"}


def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
    return signature


def parse_param(params_map):
    sorted_keys = sorted(params_map)
    params_str = "&".join(["%s=%s" % (x, params_map[x]) for x in sorted_keys])
    if params_str != "":
        return params_str + "&timestamp=" + str(int(time.time() * 1000))
    else:
        return "timestamp=" + str(int(time.time() * 1000))


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

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if self.session is None or self.session.is_closed:
            await self.async_init()

        if signed:
            if not (self.api_key and self.api_secret):
                raise ValueError("Signed request requires API Key and Secret.")

            urlpa = parse_param(query)
            url = "%s%s?%s&signature=%s" % (self.base_url, path, urlpa, get_sign(self.api_secret, urlpa))
            headers = get_header(self.api_key)
        else:
            headers = get_header_no_sign()
            url = self.base_url + path
            if query:
                sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v is not None)
                url += "?" + sorted_query if sorted_query else ""

        try:
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                if signed:
                    response = await self.session.post(url, headers=headers)
                else:
                    response = await self.session.post(url, headers=headers, json=query if query else {})
            elif method.upper() == "PUT":
                if signed:
                    response = await self.session.put(url, headers=headers)
                else:
                    response = await self.session.put(url, headers=headers, json=query if query else {})
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
                error_message = data.get("msg", "Unknown error")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"BingX API Error: [{code}] {error_message}",
                    status_code=response.status_code,
                    time=int(time.time() * 1000),
                    resp_headers=response.headers,
                )

            if not response.status_code // 100 == 2:
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"HTTP Error {response.status_code}: {response.text}",
                    status_code=response.status_code,
                    time=int(time.time() * 1000),
                    resp_headers=response.headers,
                )

            return data

        except httpx.HTTPError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {query}",
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", "Unknown"),
                time=int(time.time() * 1000),
                resp_headers=getattr(e.response, "headers", None),
            )
