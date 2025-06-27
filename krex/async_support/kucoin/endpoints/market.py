from enum import Enum


class SpotMarket(str, Enum):
    INSTRUMENT_INFO = "/api/v2/symbols"
    TICKER = "/api/v1/market/orderbook/level1"
    ALL_TICKERS = "/api/v1/market/allTickers"
    ORDERBOOK = "/api/v3/market/orderbook/level2"
    PUBLIC_TRADES = "/api/v1/market/histories"
    KLINE = "/api/v1/market/candles"

    def __str__(self) -> str:
        return self.value
