import requests
import hmac
import hashlib
import logging
import json
from dataclasses import dataclass, field
from ..utils.errors import FailedRequestError
from ..utils.helpers import generate_timestamp
from ..product_table.manager import ProductTableManager


# For GET endpoints, parameters must be sent as a query string.
# For POST, PUT, and DELETE endpoints, the parameters may be sent as a query string 
# or in the request body with content type application/x-www-form-urlencoded.


# X-MBX-APIKEY


# signed (trade, user_data, and margin) endpoints require additional param
    # signature, where secretKey = key and totalParams = value for HMAC operation
    # totalparams defined as querystring concatenated with request body
    # also requires timestamp param
        # optional param recvWindow to specify # ms after timestamp the request is valid for 
        # 5000 >= recvWindow <= 60,000, default 5000

# example for signed endpoint POST /api/v3/order    

    # query string
        # $ curl -H "X-MBX-APIKEY: vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A" -X POST 'https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71'
    
    # RSA keys

        # 1. construct the payload: arrange list of params into string. sep each param with &
        # 2. compute signature: 
            # 2.1 encode as ascii
            # 2.2 Sign payload using RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function
            # 2.3 encode output as base64 string
            # 2.4 signature may contain / and =, could cause issues with sending the request. So signature has to be URL encoded
            # 2.5 curl cmd





# check these 
HTTP_URL = "https://{SUBDOMAIN}.{DOMAIN}.{TLD}"
SUBDOMAIN_TESTNET1 = "api1"
SUBDOMAIN_TESTNET2 = "api2"
SUBDOMAIN_TESTNET3 = "api3"
SUBDOMAIN_MAINNET = "api"
DOMAIN_MAIN = "binance"
TLD_MAIN = "com"


def get_header(api_key, signature, weight, timestamp, recv_window):
    return {
        "Content-Type": "application/json",
        "X-MBX-API-KEY": api_key,
        "X-MBX-SIGN": signature,
        "X-MBX-USED-WEIGHT": weight, # ip weight, num requests for all req rate limiters defined
        "X-MBX-TIMESTAMP": str(timestamp),
        "X-MBX-RECV-WINDOW": str(recv_window),
    }


def get_header_no_sign():
    return {"Content-Type": "application/json"}


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
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)

    def __post_init__(self):
        if self.logger is None:
            self._logger = logging.getLogger(__name__)
        else:
            self._logger = self.logger

        subdomain = SUBDOMAIN_TESTNET if self.testnet else SUBDOMAIN_MAINNET
        self.endpoint = HTTP_URL.format(SUBDOMAIN=subdomain, DOMAIN=self.domain, TLD=self.tld)
        self.ptm = ProductTableManager.get_instance()

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

        if self.api_key and self.api_secret:
            signature = self._auth(payload, timestamp)
            headers = get_header(self.api_key, signature, timestamp, self.recv_window)
        else:
            headers = get_header_no_sign()

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
