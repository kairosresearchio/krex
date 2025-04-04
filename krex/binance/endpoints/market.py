from enum import Enum


class FuturesMarket(str, Enum):
    # https://fapi.binance.com
    BOOK_TICKER = "/fapi/v1/ticker/bookTicker"
    KLINE = "/fapi/v1/klines"
    PREMIUM_INDEX = "/fapi/v1/premiumIndex"

    def __str__(self) -> str:
        return self.value
