import hmac
import hashlib
import logging
import json
import requests
from dataclasses import dataclass, field
from ..product_table.manager import ProductTableManager
from ..utils.errors import FailedRequestError
from ..utils.helpers import generate_timestamp
from ..utils.common import Common

HTTP_URL = "https://{SUBDOMAIN}.{DOMAIN}.{TLD}"
SUBDOMAIN_MAIN = "api"
DOMAIN_MAINNET = "hyperliquid"
DOMAIN_TESTNET = "hyperliquid-testnet"
TLD_MAIN = "xyz"


def get_header_no_sign():
    return {"Content-Type": "application/json"}


@dataclass
class HTTPManager:
    testnet: bool = field(default=False)
    subdomain: str = field(default=SUBDOMAIN_MAIN)
    tld: str = field(default=TLD_MAIN)
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    timeout: int = field(default=10)
    recv_window: int = field(default=5000)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    def __post_init__(self):
        if self.logger is None:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = self.logger

        domain = DOMAIN_TESTNET if self.testnet else DOMAIN_MAINNET
        self.endpoint = HTTP_URL.format(SUBDOMAIN=self.subdomain, DOMAIN=domain, TLD=self.tld)

        if self.preload_product_table:
            self.ptm = ProductTableManager.get_instance(Common.HYPERLIQUID)

    def _auth(self, payload, timestamp):
        param_str = f"{timestamp}{self.api_key}{self.recv_window}{payload}"
        return hmac.new(self.api_secret.encode(), param_str.encode(), hashlib.sha256).hexdigest()

    def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
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
            payload = json.dumps(query)

        # if signed:
        #     if not (self.api_key and self.api_secret):
        #         raise ValueError("Signed request requires API Key and Secret.")
        #     signature = self._auth(payload, timestamp)
        #     headers = get_header(self.api_key, signature, timestamp, self.recv_window)
        # else:
        headers = get_header_no_sign()

        url = self.endpoint + path

        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers, timeout=self.timeout)
            elif method.upper() == "POST":
                response = self.session.post(url, json=query if query else {}, headers=headers, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

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
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", "Unknown"),
                time=timestamp,
                resp_headers=getattr(e.response, "headers", None),
            )
