import hmac
import hashlib
import json
import requests
from dataclasses import dataclass, field
from ..utils.errors import FailedRequestError
from ..utils.helpers import generate_timestamp

HTTP_URL = "https://{SUBDOMAIN}.{DOMAIN}.{TLD}"
SUBDOMAIN_TESTNET = "api-testnet"
SUBDOMAIN_MAINNET = "api"
DOMAIN_MAIN = "bybit"
TLD_MAIN = "com"


def get_header(api_key, signature, timestamp, recv_window):
    return {
        "Content-Type": "application/json",
        "X-BAPI-API-KEY": api_key,
        "X-BAPI-SIGN": signature,
        "X-BAPI-SIGN-TYPE": "2",
        "X-BAPI-TIMESTAMP": str(timestamp),
        "X-BAPI-RECV-WINDOW": str(recv_window),
    }


@dataclass
class HTTPManager:
    testnet: bool = field(default=False)
    domain: str = field(default=DOMAIN_MAIN)
    tld: str = field(default=TLD_MAIN)
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    timeout: int = field(default=10)
    recv_window: int = field(default=5000)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)

    def __post_init__(self):
        subdomain = SUBDOMAIN_TESTNET if self.testnet else SUBDOMAIN_MAINNET
        self.endpoint = HTTP_URL.format(SUBDOMAIN=subdomain, DOMAIN=self.domain, TLD=self.tld)
        self.session = requests.Session()

    def _auth(self, payload, timestamp):
        param_str = f"{timestamp}{self.api_key}{self.recv_window}{payload}"
        return hmac.new(self.api_secret.encode(), param_str.encode(), hashlib.sha256).hexdigest()

    def _request(self, method, path, query=None):
        if query is None:
            query = {}

        timestamp = generate_timestamp()

        if method.upper() == "GET":
            if query:
                sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
                if sorted_query:
                    path += "?" + sorted_query
                payload = sorted_query
            else:
                payload = ""
        else:
            payload = json.dumps(query)

        signature = self._auth(payload, timestamp)
        headers = get_header(self.api_key, signature, timestamp, self.recv_window)
        url = self.endpoint + path

        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = self.session.post(url, json=query if query else {}, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            response_json = response.json()

        except requests.exceptions.RequestException as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )

        return response_json
