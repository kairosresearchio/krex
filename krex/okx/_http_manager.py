import requests
import json
import logging
from .utils import helpers

logger = logging.getLogger(__name__)


class HTTPManager:
    def __init__(
        self,
        api_key=None,
        api_secret=None,
        passphrase=None,
        flag="1",
        base_api="https://www.okx.com",
        debug=False,
        proxy=None,
    ):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.PASSPHRASE = passphrase
        self.flag = flag
        self.domain = base_api
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}

    def _request(self, method, request_path, params=None):
        if params is None:
            params = {}

        if method.upper() == "GET":
            request_path += helpers.parse_params_to_str(params)

        timestamp = helpers.get_timestamp()

        body = json.dumps(params) if method.upper() == "POST" else ""

        if (
            self.API_KEY is not None
            and self.API_SECRET is not None
            and self.PASSPHRASE is not None
        ):
            sign = helpers.sign(
                helpers.pre_hash(
                    timestamp, method.upper(), request_path, body, self.debug
                ),
                self.API_SECRET,
            )
            header = helpers.get_header(
                self.API_KEY, sign, timestamp, self.PASSPHRASE, self.flag, self.debug
            )
        else:
            header = helpers.get_header_no_sign(self.flag, self.debug)

        url = self.domain + request_path

        if self.debug:
            logger.debug(f"Request: {method.upper()} {url}")
            logger.debug(f"Headers: {header}")
            logger.debug(f"Body: {body}")

        if method.upper() == "GET":
            response = self.session.get(url, headers=header)
        elif method.upper() == "POST":
            response = self.session.post(url, data=body, headers=header)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response.json()
