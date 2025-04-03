import hmac
import hashlib
import logging
import json
import requests
from dataclasses import dataclass, field
from ..utils.errors import FailedRequestError
from ..utils.helpers import generate_timestamp
from ..product_table.manager import ProductTableManager
import base64
import time


HTTP_URL = "https://{SUBDOMAIN}.{DOMAIN}.{TLD}"
SUBDOMAIN_FUTURES = "futures"
SUBDOMAIN_MAINNET = "api"
DOMAIN_MAIN = "kraken"
TLD_MAIN = "com"


@dataclass
class HTTPManager:
    api_key: str
    api_secret: str
    futures: bool = field(default=False)
    timeout: int = field(default=10)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    logger: logging.Logger = field(default_factory=lambda: logging.getLogger(__name__), init=False)
    base_url: str = field(init=False)

    def __post_init__(self):
        subdomain = SUBDOMAIN_FUTURES if self.futures else SUBDOMAIN_MAINNET
        self.base_url = HTTP_URL.format(SUBDOMAIN=subdomain, DOMAIN=DOMAIN_MAIN, TLD=TLD_MAIN)
        self.api_secret = self.api_secret.encode()

    def _generate_nonce(self) -> str:
        """Generates a nonce for API requests."""
        return str(int(time.time() * 1000))

    def _sign_request(self, endpoint: str, data: dict) -> dict:
        """Signs a request for Kraken's private API."""
        nonce = self._generate_nonce()
        data["nonce"] = nonce
        post_data = json.dumps(data, separators=(",", ":"))  # Ensure compact JSON format

        # Step 1: SHA-256 hash of nonce + post data
        sha256_hash = hashlib.sha256(post_data.encode()).digest()

        # Step 2: Base64 decode API secret
        secret_decoded = base64.b64decode(self.api_secret)

        # Step 3: HMAC-SHA-512 signature
        signature = hmac.new(secret_decoded, sha256_hash, hashlib.sha512).digest()
        api_sign = base64.b64encode(signature).decode()

        headers = {
            "API-Key": self.api_key,
            "API-Sign": api_sign,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        return headers

    def _request(self, method: str, endpoint: str, data: dict = None, auth: bool = False):
        """Handles Kraken API requests."""
        url = f"{self.base_url}/0/private/{endpoint}" if auth else f"{self.base_url}/0/public/{endpoint}"
        data = data or {}
        headers = {}

        if auth:
            headers = self._sign_request(endpoint, data)

        try:
            if method.upper() == "GET":
                response = self.session.get(url, params=data, headers=headers, timeout=self.timeout)
            else:  # POST requests
                response = self.session.post(url, json=data, headers=headers, timeout=self.timeout)

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            return {"error": str(e)}

    def get_public_data(self, endpoint: str, params: dict = None):
        """Fetch public API data (e.g., ticker info)."""
        return self._request("GET", endpoint, params, auth=False)

    def get_private_data(self, endpoint: str, params: dict = None):
        """Fetch private API data (e.g., account balances, open orders)."""
        return self._request("POST", endpoint, params, auth=True)

