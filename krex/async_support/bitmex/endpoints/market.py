from enum import Enum


class Market(str, Enum):
    INSTRUMENT_INFO = "/api/v1/instrument/active"
    ORDERBOOK = "/api/v1/orderBook/L2"
    TRADE = "/api/v1/trade"
    TICKER = "/api/v1/quote/bucketed"
    KLINE = "/api/v1/trade/bucketed"
    FUNDING = "/api/v1/funding"

    def __str__(self) -> str:
        return self.value
