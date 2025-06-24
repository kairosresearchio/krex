from enum import Enum


class SwapMarket(str, Enum):
    INSTRUMENT_INFO = "/openApi/swap/v2/quote/contracts"
    ORDERBOOK = "/openApi/swap/v2/quote/depth"
    PUBLIC_TRADE = "/openApi/swap/v2/quote/trades"
    KLINE = "/openApi/swap/v3/quote/klines"
    TICKER = "/openApi/swap/v2/quote/ticker"

    def __str__(self) -> str:
        return self.value
