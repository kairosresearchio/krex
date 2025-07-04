from enum import Enum


class Market(str, Enum):
    GET_KLINE = "/api/v5/market/candles"
    GET_ORDERBOOK = "/api/v5/market/books"
    GET_TICKERS = "/api/v5/market/tickers"
    GET_PUBLIC_TRADES = "/api/v5/market/trades"

    def __str__(self) -> str:
        return self.value
