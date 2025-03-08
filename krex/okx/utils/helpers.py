import hmac
import base64
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)


def sign(message, secretKey):
    mac = hmac.new(
        bytes(secretKey, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body, debug=True):
    if debug:
        logger.debug(f"body: {body}")
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, sign, timestamp, passphrase, flag, debug=True):
    header = {
        "Content-Type": "application/json",
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": sign,
        "OK-ACCESS-TIMESTAMP": str(timestamp),
        "OK-ACCESS-PASSPHRASE": passphrase,
        "x-simulated-trading": flag,
    }
    if debug:
        logger.debug(f"header: {header}")
    return header


def get_header_no_sign(flag, debug=True):
    header = {
        "Content-Type": "application/json",
        "x-simulated-trading": flag,
    }
    if debug:
        logger.debug(f"header: {header}")
    return header


def parse_params_to_str(params):
    url = "?"
    for key, value in params.items():
        if value != "":
            url = url + str(key) + "=" + str(value) + "&"
    url = url[0:-1]
    return url


def get_timestamp():
    now = datetime.now(timezone.utc)
    t = now.isoformat(timespec="milliseconds").replace("+00:00", "Z")
    return t


def signature(timestamp, method, request_path, body, secret_key):
    if str(body) == "{}" or str(body) == "None":
        body = ""
    message = str(timestamp) + str.upper(method) + request_path + str(body)

    mac = hmac.new(
        bytes(secret_key, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    d = mac.digest()

    return base64.b64encode(d)
