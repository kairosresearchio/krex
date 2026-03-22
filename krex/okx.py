import json
import hmac
import base64
import logging
import requests
from dataclasses import dataclass, field
from .product_table.manager import ProductTableManager
from .utils.errors import FailedRequestError
from .utils.helpers import generate_timestamp
from .utils.common import Common
from .utils.terms import OrderSide, OrderType, PositionSide, MarginMode


def _to_okx(value, enum_cls):
    """Convert str or Enum to the OKX-specific string value."""
    if isinstance(value, enum_cls):
        return value.to_exchange(Common.OKX)
    if isinstance(value, str):
        return enum_cls.from_any(value).to_exchange(Common.OKX)
    return value

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

class _Account:
    GET_INSTRUMENTS         = "/api/v5/account/instruments"
    ACCOUNT_INFO            = "/api/v5/account/balance"
    POSITION_INFO           = "/api/v5/account/positions"
    POSITIONS_HISTORY       = "/api/v5/account/positions-history"
    POSITION_RISK           = "/api/v5/account/account-position-risk"
    BILLS_DETAIL            = "/api/v5/account/bills"
    BILLS_ARCHIVE           = "/api/v5/account/bills-archive"
    BILLS_HISTORY_ARCHIVE   = "/api/v5/account/bills-history-archive"
    ACCOUNT_CONFIG          = "/api/v5/account/config"
    POSITION_MODE           = "/api/v5/account/set-position-mode"
    SET_LEVERAGE            = "/api/v5/account/set-leverage"
    MAX_TRADE_SIZE          = "/api/v5/account/max-size"
    MAX_AVAIL_SIZE          = "/api/v5/account/max-avail-size"
    GET_LEVERAGE            = "/api/v5/account/leverage-info"
    GET_ADJUST_LEVERAGE     = "/api/v5/account/adjust-leverage-info"
    MAX_LOAN                = "/api/v5/account/max-loan"
    FEE_RATES               = "/api/v5/account/trade-fee"
    INTEREST_ACCRUED        = "/api/v5/account/interest-accrued"
    INTEREST_RATE           = "/api/v5/account/interest-rate"
    SET_GREEKS              = "/api/v5/account/set-greeks"
    SET_ISOLATED_MODE       = "/api/v5/account/set-isolated-mode"
    MAX_WITHDRAWAL          = "/api/v5/account/max-withdrawal"
    INTEREST_LIMITS         = "/api/v5/account/interest-limits"
    SET_AUTO_LOAN           = "/api/v5/account/set-auto-loan"


class _Asset:
    CURRENCY_INFO               = "/api/v5/asset/currencies"
    GET_BALANCES                = "/api/v5/asset/balances"
    ASSET_VALUATION             = "/api/v5/asset/asset-valuation"
    FUNDS_TRANSFER              = "/api/v5/asset/transfer"
    TRANSFER_STATE              = "/api/v5/asset/transfer-state"
    BILLS_INFO                  = "/api/v5/asset/bills"
    DEPOSIT_ADDRESS             = "/api/v5/asset/deposit-address"
    DEPOSIT_HISTORY             = "/api/v5/asset/deposit-history"
    WITHDRAWAL_COIN             = "/api/v5/asset/withdrawal"
    CANCEL_WITHDRAWAL           = "/api/v5/asset/cancel-withdrawal"
    WITHDRAWAL_HISTORY          = "/api/v5/asset/withdrawal-history"
    GET_DEPOSIT_WITHDRAW_STATUS = "/api/v5/asset/deposit-withdraw-status"
    EXCHANGE_LIST               = "/api/v5/asset/exchange-list"
    MONTHLY_STATEMENT           = "/api/v5/asset/monthly-statement"
    GET_CURRENCIES              = "/api/v5/asset/convert/currencies"
    CONVERT_HISTORY             = "/api/v5/asset/convert/history"


class _Market:
    GET_KLINE         = "/api/v5/market/candles"
    GET_ORDERBOOK     = "/api/v5/market/books"
    GET_TICKERS       = "/api/v5/market/tickers"
    GET_PUBLIC_TRADES = "/api/v5/market/trades"


class _Public:
    GET_INSTRUMENT_INFO      = "/api/v5/public/instruments"
    GET_FUNDING_RATE         = "/api/v5/public/funding-rate"
    GET_FUNDING_RATE_HISTORY = "/api/v5/public/funding-rate-history"
    GET_POSITION_TIERS       = "/api/v5/public/position-tiers"


class _Trade:
    PLACE_ORDER             = "/api/v5/trade/order"
    PLACE_BATCH_ORDERS      = "/api/v5/trade/batch-orders"
    CANCEL_ORDER            = "/api/v5/trade/cancel-order"
    CANCEL_BATCH_ORDERS     = "/api/v5/trade/cancel-batch-orders"
    AMEND_ORDER             = "/api/v5/trade/amend-order"
    AMEND_BATCH_ORDER       = "/api/v5/trade/amend-batch-orders"
    CLOSE_POSITION          = "/api/v5/trade/close-position"
    ORDER_INFO              = "/api/v5/trade/order"
    ORDERS_PENDING          = "/api/v5/trade/orders-pending"
    ORDERS_HISTORY          = "/api/v5/trade/orders-history"
    ORDERS_HISTORY_ARCHIVE  = "/api/v5/trade/orders-history-archive"
    ORDER_FILLS             = "/api/v5/trade/fills"
    ORDERS_FILLS_HISTORY    = "/api/v5/trade/fills-history"
    ACCOUNT_RATE_LIMIT      = "/api/v5/trade/account-rate-limit"


# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def _sign(message: str, secret_key: str) -> str:
    mac = hmac.new(
        bytes(secret_key, encoding="utf8"),
        bytes(message, encoding="utf-8"),
        digestmod="sha256",
    )
    return base64.b64encode(mac.digest()).decode()


def _pre_hash(timestamp: str, method: str, path: str, body: str) -> str:
    return str(timestamp) + str.upper(method) + path + body


def _build_header(api_key: str, sign: str, timestamp: str, passphrase: str, flag: str) -> dict:
    return {
        "Content-Type": "application/json",
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": sign,
        "OK-ACCESS-TIMESTAMP": str(timestamp),
        "OK-ACCESS-PASSPHRASE": passphrase,
        "x-simulated-trading": flag,
    }


def _build_header_no_sign(flag: str) -> dict:
    return {
        "Content-Type": "application/json",
        "x-simulated-trading": flag,
    }


def _params_to_str(query: dict) -> str:
    url = "?"
    for key, value in query.items():
        if value != "":
            url += f"{key}={value}&"
    return url.rstrip("&")


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

@dataclass
class Client:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    passphrase: str = field(default=None)
    flag: str = field(default="0")
    base_api: str = field(default="https://www.okx.com")
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    def __post_init__(self):
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = ProductTableManager.get_instance(Common.OKX)

    # -----------------------------------------------------------------------
    # Core request
    # -----------------------------------------------------------------------

    def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if query is None:
            query = {}

        if method.upper() == "GET" and query:
            path += _params_to_str(query)

        timestamp = generate_timestamp(iso_format=True)
        body = query if method.upper() == "POST" else ""
        body_str = json.dumps(body) if isinstance(body, (dict, list)) else body

        if signed:
            if not (self.api_key and self.api_secret and self.passphrase):
                raise ValueError("Signed request requires API Key, Secret, and Passphrase.")
            sign = _sign(_pre_hash(timestamp, method.upper(), path, body_str), self.api_secret)
            headers = _build_header(self.api_key, sign, timestamp, self.passphrase, self.flag)
        else:
            headers = _build_header_no_sign(self.flag)

        url = self.base_api + path
        response = None

        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = self.session.post(url, json=body, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if data.get("code", "0") != "0":
                code = data.get("code", "Unknown")
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"OKX API Error: [{code}] {data.get('msg', 'Unknown error')}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            if response.status_code // 100 != 2:
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
                request=f"{method.upper()} {url} | Body: {body}",
                message=f"Request failed: {str(e)}",
                status_code=response.status_code if response else "Unknown",
                time=timestamp,
                resp_headers=response.headers if response else None,
            )

    # -----------------------------------------------------------------------
    # Market
    # -----------------------------------------------------------------------

    def get_kline(
        self,
        product_symbol: str,
        bar: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if bar is not None:
            payload["bar"] = bar
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit
        return self._request("GET", _Market.GET_KLINE, payload, signed=False)

    def get_orderbook(self, product_symbol: str, sz: str = None):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if sz is not None:
            payload["sz"] = sz
        return self._request("GET", _Market.GET_ORDERBOOK, payload, signed=False)

    def get_ticker(self, instType: str, uly: str = None, instFamily: str = None):
        payload = {"instType": instType}
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        return self._request("GET", _Market.GET_TICKERS, payload, signed=False)

    def get_public_trades(self, product_symbol: str, limit: int = None):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if limit is not None:
            payload["limit"] = str(limit)
        return self._request("GET", _Market.GET_PUBLIC_TRADES, payload, signed=False)

    # -----------------------------------------------------------------------
    # Public
    # -----------------------------------------------------------------------

    def get_instruments(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
    ):
        payload = {"instType": instType}
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        return self._request("GET", _Public.GET_INSTRUMENT_INFO, payload, signed=False)

    def get_funding_rate(self, product_symbol: str):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        return self._request("GET", _Public.GET_FUNDING_RATE, payload, signed=False)

    def get_funding_rate_history(
        self,
        product_symbol: str,
        before: str = None,
        after: str = None,
        limit: str = None,
    ):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit
        return self._request("GET", _Public.GET_FUNDING_RATE_HISTORY, payload, signed=False)

    # -----------------------------------------------------------------------
    # Trade
    # -----------------------------------------------------------------------

    def place_order(
        self,
        product_symbol: str,
        tdMode: str,
        side: OrderSide | str,
        ordType: OrderType | str,
        sz: str,
        ccy: str = None,
        clOrdId: str = None,
        posSide: PositionSide | str = None,
        px: str = None,
        pxUsd: str = None,
        pxVol: str = None,
        reduceOnly: bool = False,
        tgtCcy: str = None,
        banAmend: bool = False,
        quickMgnType: str = None,
        stpId: str = None,
        stpMode: str = None,
    ):
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
            "tdMode": tdMode,
            "side": _to_okx(side, OrderSide),
            "ordType": _to_okx(ordType, OrderType),
            "sz": sz,
            "tag": "29570c5e4c71BCDE",
        }
        if ccy is not None:
            payload["ccy"] = ccy
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        if posSide is not None:
            payload["posSide"] = _to_okx(posSide, PositionSide)
        if px is not None:
            payload["px"] = px
        if pxUsd is not None:
            payload["pxUsd"] = pxUsd
        if pxVol is not None:
            payload["pxVol"] = pxVol
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if tgtCcy is not None:
            payload["tgtCcy"] = tgtCcy
        if banAmend is not None:
            payload["banAmend"] = banAmend
        if quickMgnType is not None:
            payload["quickMgnType"] = quickMgnType
        if stpId is not None:
            payload["stpId"] = stpId
        if stpMode is not None:
            payload["stpMode"] = stpMode
        return self._request("POST", _Trade.PLACE_ORDER, payload)

    def amend_order(
        self,
        product_symbol: str,
        ordId: str = None,
        clOrdId: str = None,
        newSz: str = None,
        newPx: str = None,
        newPxUsd: str = None,
        newPxVol: str = None,
        cxlOnFail: str = None,
        reqId: str = None,
    ):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        if newSz is not None:
            payload["newSz"] = newSz
        if newPx is not None:
            payload["newPx"] = newPx
        if newPxUsd is not None:
            payload["newPxUsd"] = newPxUsd
        if newPxVol is not None:
            payload["newPxVol"] = newPxVol
        if cxlOnFail is not None:
            payload["cxlOnFail"] = cxlOnFail
        if reqId is not None:
            payload["reqId"] = reqId
        return self._request("POST", _Trade.AMEND_ORDER, payload)

    def close_positions(
        self,
        product_symbol: str,
        mgnMode: MarginMode | str,
        posSide: PositionSide | str = None,
        autoCxl: bool = None,
        ccy: str = None,
    ):
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
            "mgnMode": _to_okx(mgnMode, MarginMode),
            "tag": "29570c5e4c71BCDE",
        }
        if posSide is not None:
            payload["posSide"] = _to_okx(posSide, PositionSide)
        if autoCxl is not None:
            payload["autoCxl"] = autoCxl
        if ccy is not None:
            payload["ccy"] = ccy
        return self._request("POST", _Trade.CLOSE_POSITION, payload)

    def get_order(self, product_symbol: str, ordId: str = None, clOrdId: str = None):
        payload = {"instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol)}
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        return self._request("GET", _Trade.ORDER_INFO, payload)

    def get_order_list(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordType: str = None,
        state: str = None,
        limit: str = None,
    ):
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordType is not None:
            payload["ordType"] = ordType
        if state is not None:
            payload["state"] = state
        if limit is not None:
            payload["limit"] = limit
        return self._request("GET", _Trade.ORDERS_PENDING, payload)

    def get_orders_history(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordType: str = None,
        state: str = None,
        category: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        payload = {"instType": instType}
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordType is not None:
            payload["ordType"] = ordType
        if state is not None:
            payload["state"] = state
        if category is not None:
            payload["category"] = category
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit
        return self._request("GET", _Trade.ORDERS_HISTORY, payload)

    # -----------------------------------------------------------------------
    # Account
    # -----------------------------------------------------------------------

    def get_positions(self, instType: str = None, product_symbol: str = None):
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        return self._request("GET", _Account.POSITION_INFO, payload)

    def get_account_config(self):
        return self._request("GET", _Account.ACCOUNT_CONFIG)

    def set_position_mode(self, posMode: str):
        return self._request("POST", _Account.POSITION_MODE, {"posMode": posMode})

    def set_leverage(
        self,
        lever: str,
        mgnMode: MarginMode | str,
        product_symbol: str = None,
        ccy: str = None,
        posSide: PositionSide | str = None,
    ):
        payload = {"lever": lever, "mgnMode": _to_okx(mgnMode, MarginMode)}
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy
        if posSide is not None:
            payload["posSide"] = _to_okx(posSide, PositionSide)
        return self._request("POST", _Account.SET_LEVERAGE, payload)

    # -----------------------------------------------------------------------
    # Asset
    # -----------------------------------------------------------------------

    def get_balances(self, ccy: str = None):
        payload = {}
        if ccy is not None:
            payload["ccy"] = ",".join(ccy)
        return self._request("GET", _Asset.GET_BALANCES, payload)
