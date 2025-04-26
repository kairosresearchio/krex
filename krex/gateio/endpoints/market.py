from enum import Enum


class FutureMarket(str, Enum):
    GET_ALL_CONTRACTS = "/futures/{settle}/contracts"
    GET_A_SINGLE_CONTRACT = "/futures/{settle}/contracts/{contract}"
    ORDER_BOOK = "/futures/{settle}/order_book"
    GET_KLINE = "/futures/{settle}/candlesticks"
    LIST_TICKERS = "/futures/{settle}/tickers"
    FUNDING_RATE_HISTORY = "/futures/{settle}/funding_rate"

    def __str__(self) -> str:
        return self.value


class DeliveryMarket(str, Enum):
    GET_ALL_CONTRACTS = "/delivery/{settle}/contracts"
    ORDER_BOOK = "/delivery/{settle}/order_book"
    GET_KLINE = "/delivery/{settle}/candlesticks"
    LIST_TICKERS = "/delivery/{settle}/tickers"


class SpotMarket(str, Enum):
    GET_ALL_CURRENCY_PAIRS = "/spot/currency_pairs"
    ORDER_BOOK = "/spot/order_book"
    GET_KLINE = "/spot/candlesticks"
    LIST_TICKERS = "/spot/tickers"

    def __str__(self) -> str:
        return self.value
