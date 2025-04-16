import requests
import json
import logging
import hmac
import base64
from dataclasses import dataclass, field
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp


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
    header = {
        "Content-Type": "application/json",
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": sign,
        "OK-ACCESS-TIMESTAMP": str(timestamp),
        "OK-ACCESS-PASSPHRASE": passphrase,
        "x-simulated-trading": flag,
    }
    return header


def parse_params_to_str(query):
    url = "?"
    for key, value in query.items():
        if value != "":
            url = url + str(key) + "=" + str(value) + "&"
    url = url[0:-1]
    return url


def get_header_no_sign(flag):
    header = {
        "Content-Type": "application/json",
        "x-simulated-trading": flag,
    }
    return header


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    passphrase: str = field(default=None)
    flag: str = field(default="1")
    base_api: str = field(default="https://www.okx.com")
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)

    def __post_init__(self):
        if self.logger is None:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = self.logger

        self.ptm = ProductTableManager.get_instance()

    def _request(self, method, path, query=None):
        if query is None:
            query = {}

        if method.upper() == "GET":
            path += parse_params_to_str(query)

        timestamp = generate_timestamp(iso_format=True)
        body = json.dumps(query) if method.upper() == "POST" else ""

        if self.api_key and self.api_secret and self.passphrase:
            sign = _sign(pre_hash(timestamp, method.upper(), path, body), self.api_secret)
            header = get_header(self.api_key, sign, timestamp, self.passphrase, self.flag)
        else:
            header = get_header_no_sign(self.flag)

        url = self.base_api + path

        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=header)
            elif method.upper() == "POST":
                response = self.session.post(url, json=body, headers=header)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            response_json = response.json()

        except requests.exceptions.RequestException as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {body}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )

        return response_json
