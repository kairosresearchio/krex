from enum import Enum


class Market(str, Enum):
    GET_INSTRUMENTS_INFO = "/v5/market/instruments-info"
    GET_KLINE = "/v5/market/kline"
    GET_ORDERBOOK = "/v5/market/orderbook"
    GET_PUBLIC_TRADE_HISTORY = "/v5/market/recent-trade"
    GET_TICKERS = "/v5/market/tickers"
    GET_FUNDING_RATE_HISTORY = "/v5/market/funding/history"
    GET_PUBLIC_TRADING_HISTORY = "/v5/market/recent-trade"

    def __str__(self) -> str:
        return self.value
