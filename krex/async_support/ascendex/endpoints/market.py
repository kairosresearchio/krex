from enum import Enum


class SpotMarket(str, Enum):
    INSTRUMENT_INFO = {
        "route": "/api/pro/v1/cash/products",
    }
    TICKER = {
        "route": "/api/pro/v1/spot/ticker",
    }
    KLINE = {
        "route": "/api/pro/v1/barhist",
    }
    ORDERBOOK = {
        "route": "/api/pro/v1/depth",
    }
    PUBLIC_TRADE = {
        "route": "/api/pro/v1/trades",
    }

    def __str__(self) -> str:
        return self.value
