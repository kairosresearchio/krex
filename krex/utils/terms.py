from __future__ import annotations
from enum import Enum


# ---------------------------------------------------------------------------
# OrderSide
# ---------------------------------------------------------------------------

class OrderSide(str, Enum):
    """
    統一下單方向。

    用法：
        side = OrderSide.BUY
        okx_value = side.to_exchange("okx")   # "buy"
        binance_value = side.to_exchange("binance")  # "BUY"
    """

    BUY = "BUY"
    SELL = "SELL"

    @classmethod
    def from_any(cls, value: str) -> "OrderSide":
        v = value.strip().lower()
        if v == "buy":
            return cls.BUY
        if v == "sell":
            return cls.SELL
        raise ValueError(f"Unknown order side: {value!r}")

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance":     {"BUY": "BUY",  "SELL": "SELL"},
            "okx":         {"BUY": "buy",  "SELL": "sell"},
            "bybit":       {"BUY": "Buy",  "SELL": "Sell"},
            "bitmart":     {"BUY": "buy",  "SELL": "sell"},
            "gateio":      {"BUY": "buy",  "SELL": "sell"},
            "bitmex":      {"BUY": "Buy",  "SELL": "Sell"},
            "hyperliquid": {"BUY": "B",    "SELL": "A"},
            "bingx":       {"BUY": "BUY",  "SELL": "SELL"},
            "kucoin":      {"BUY": "buy",  "SELL": "sell"},
            "ascendex":    {"BUY": "buy",  "SELL": "sell"},
            "zoomex":      {"BUY": "Buy",  "SELL": "Sell"},
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            return self.value
        return exchange_map[self.name]


# ---------------------------------------------------------------------------
# OrderType
# ---------------------------------------------------------------------------

class OrderType(str, Enum):
    """
    統一下單類型。
    """

    MARKET = "MARKET"
    LIMIT = "LIMIT"
    LIMIT_MAKER = "LIMIT_MAKER"   # post-only
    FOK = "FOK"                   # fill-or-kill
    IOC = "IOC"                   # immediate-or-cancel

    @classmethod
    def from_any(cls, value: str) -> "OrderType":
        v = value.strip().upper()
        aliases = {
            "POST_ONLY": "LIMIT_MAKER",
            "POSTONLY":  "LIMIT_MAKER",
        }
        v = aliases.get(v, v)
        try:
            return cls(v)
        except ValueError:
            raise ValueError(f"Unknown order type: {value!r}")

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance": {
                "MARKET":     "MARKET",
                "LIMIT":      "LIMIT",
                "LIMIT_MAKER":"LIMIT_MAKER",
                "FOK":        "LIMIT",    # binance uses timeInForce=FOK
                "IOC":        "LIMIT",    # binance uses timeInForce=IOC
            },
            "okx": {
                "MARKET":     "market",
                "LIMIT":      "limit",
                "LIMIT_MAKER":"post_only",
                "FOK":        "fok",
                "IOC":        "ioc",
            },
            "bybit": {
                "MARKET":     "Market",
                "LIMIT":      "Limit",
                "LIMIT_MAKER":"Limit",    # bybit uses timeInForce=PostOnly
                "FOK":        "Limit",
                "IOC":        "Limit",
            },
            "bitmart": {
                "MARKET":     "market",
                "LIMIT":      "limit",
                "LIMIT_MAKER":"limit",
                "FOK":        "limit",
                "IOC":        "limit",
            },
            "gateio": {
                "MARKET":     "market",
                "LIMIT":      "limit",
                "LIMIT_MAKER":"limit",
                "FOK":        "limit",
                "IOC":        "limit",
            },
            "bitmex": {
                "MARKET":     "Market",
                "LIMIT":      "Limit",
                "LIMIT_MAKER":"Limit",
                "FOK":        "Limit",
                "IOC":        "Limit",
            },
            "bingx": {
                "MARKET":     "MARKET",
                "LIMIT":      "LIMIT",
                "LIMIT_MAKER":"LIMIT",
                "FOK":        "LIMIT",
                "IOC":        "LIMIT",
            },
            "kucoin": {
                "MARKET":     "market",
                "LIMIT":      "limit",
                "LIMIT_MAKER":"limit",
                "FOK":        "limit",
                "IOC":        "limit",
            },
            "ascendex": {
                "MARKET":     "market",
                "LIMIT":      "limit",
                "LIMIT_MAKER":"limit",
                "FOK":        "limit",
                "IOC":        "limit",
            },
            "zoomex": {
                "MARKET":     "Market",
                "LIMIT":      "Limit",
                "LIMIT_MAKER":"Limit",
                "FOK":        "Limit",
                "IOC":        "Limit",
            },
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            raise ValueError(f"No OrderType mapping for exchange: {exchange!r}")
        try:
            return exchange_map[self.name]
        except KeyError:
            raise ValueError(f"OrderType {self.name!r} has no mapping for exchange {exchange!r}")


# ---------------------------------------------------------------------------
# TimeInForce
# ---------------------------------------------------------------------------

class TimeInForce(str, Enum):
    """
    訂單的有效期類型。
    """

    GTC = "GTC"   # good-till-cancel
    IOC = "IOC"   # immediate-or-cancel
    FOK = "FOK"   # fill-or-kill
    GTX = "GTX"   # good-till-crossing (post-only)

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance": {"GTC": "GTC", "IOC": "IOC", "FOK": "FOK", "GTX": "GTX"},
            "okx":     {"GTC": "",    "IOC": "",    "FOK": "",    "GTX": ""},   # OKX encodes TIF in ordType
            "bybit":   {"GTC": "GTC", "IOC": "IOC", "FOK": "FOK", "GTX": "PostOnly"},
            "bitmex":  {"GTC": "GoodTillCancel", "IOC": "ImmediateOrCancel", "FOK": "FillOrKill", "GTX": "ParticipateDoNotInitiate"},
            "bingx":   {"GTC": "GTC", "IOC": "IOC", "FOK": "FOK", "GTX": "GTX"},
            "kucoin":  {"GTC": "GTC", "IOC": "IOC", "FOK": "FOK", "GTX": "GTX"},
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            return self.value
        return exchange_map.get(self.name, self.value)


# ---------------------------------------------------------------------------
# PositionSide
# ---------------------------------------------------------------------------

class PositionSide(str, Enum):
    """
    倉位方向（用於雙向持倉模式）。
    """

    LONG = "LONG"
    SHORT = "SHORT"
    NET = "NET"    # 單向倉位 / both

    @classmethod
    def from_any(cls, value: str) -> "PositionSide":
        v = value.strip().upper()
        aliases = {"BOTH": "NET", "ONE_WAY": "NET"}
        v = aliases.get(v, v)
        try:
            return cls(v)
        except ValueError:
            raise ValueError(f"Unknown position side: {value!r}")

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance": {"LONG": "LONG",  "SHORT": "SHORT", "NET": "BOTH"},
            "okx":     {"LONG": "long",  "SHORT": "short", "NET": "net"},
            "bybit":   {"LONG": "Buy",   "SHORT": "Sell",  "NET": ""},
            "bitmex":  {"LONG": "Buy",   "SHORT": "Sell",  "NET": ""},
            "bingx":   {"LONG": "LONG",  "SHORT": "SHORT", "NET": "BOTH"},
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            return self.value
        return exchange_map.get(self.name, self.value)


# ---------------------------------------------------------------------------
# MarginMode
# ---------------------------------------------------------------------------

class MarginMode(str, Enum):
    """
    保證金模式。
    """

    CROSS = "CROSS"
    ISOLATED = "ISOLATED"

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance": {"CROSS": "CROSSED",   "ISOLATED": "ISOLATED"},
            "okx":     {"CROSS": "cross",      "ISOLATED": "isolated"},
            "bybit":   {"CROSS": "REGULAR_MARGIN", "ISOLATED": "ISOLATED_MARGIN"},
            "bitmart": {"CROSS": "cross",      "ISOLATED": "isolated"},
            "gateio":  {"CROSS": "cross",      "ISOLATED": "isolated"},
            "bitmex":  {"CROSS": "cross",      "ISOLATED": "isolated"},
            "bingx":   {"CROSS": "CROSSED",    "ISOLATED": "ISOLATED"},
            "kucoin":  {"CROSS": "CROSS",      "ISOLATED": "ISOLATED"},
            "zoomex":  {"CROSS": "REGULAR_MARGIN", "ISOLATED": "ISOLATED_MARGIN"},
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            return self.value
        return exchange_map.get(self.name, self.value)


# ---------------------------------------------------------------------------
# ProductType
# ---------------------------------------------------------------------------

class ProductType(str, Enum):
    """
    商品類型。
    """

    SPOT = "SPOT"
    SWAP = "SWAP"         # perpetual
    FUTURES = "FUTURES"
    MARGIN = "MARGIN"
    OPTION = "OPTION"

    def to_exchange(self, exchange: str) -> str:
        _map: dict[str, dict[str, str]] = {
            "binance": {
                "SPOT":    "SPOT",
                "SWAP":    "PERPETUAL",
                "FUTURES": "DELIVERING",
                "MARGIN":  "MARGIN",
                "OPTION":  "OPTION",
            },
            "okx": {
                "SPOT":    "SPOT",
                "SWAP":    "SWAP",
                "FUTURES": "FUTURES",
                "MARGIN":  "MARGIN",
                "OPTION":  "OPTION",
            },
            "bybit": {
                "SPOT":    "spot",
                "SWAP":    "linear",
                "FUTURES": "linear",
                "MARGIN":  "spot",
                "OPTION":  "option",
            },
            "bitmart": {
                "SPOT":    "spot",
                "SWAP":    "swap",
                "FUTURES": "futures",
                "MARGIN":  "margin",
                "OPTION":  "option",
            },
            "gateio": {
                "SPOT":    "spot",
                "SWAP":    "perpetual",
                "FUTURES": "futures",
                "MARGIN":  "margin",
                "OPTION":  "option",
            },
            "bitmex": {
                "SPOT":    "SPOT",
                "SWAP":    "FFWCSX",
                "FUTURES": "FFCCSX",
                "MARGIN":  "SPOT",
                "OPTION":  "OPTIONCO",
            },
            "bingx": {
                "SPOT":    "SPOT",
                "SWAP":    "PERPETUAL",
                "FUTURES": "FUTURES",
                "MARGIN":  "MARGIN",
                "OPTION":  "OPTION",
            },
        }
        exchange_map = _map.get(exchange.lower())
        if exchange_map is None:
            return self.value
        return exchange_map.get(self.name, self.value)
