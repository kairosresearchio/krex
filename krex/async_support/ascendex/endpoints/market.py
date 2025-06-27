from enum import Enum


class SpotMarket(str, Enum):
    INSTRUMENT_INFO = "/api/pro/v1/cash/products"
    TICKER = "/api/pro/v1/spot/ticker"
    KLINE = "/api/pro/v1/barhist"
    ORDERBOOK = "/api/pro/v1/depth"
    PUBLIC_TRADE = "/api/pro/v1/trades"

    @property
    def hash(self):
        return self.value.split("/")[-1]

    def __str__(self) -> str:
        return self.value
