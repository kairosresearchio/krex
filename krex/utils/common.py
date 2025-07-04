from enum import Enum


class Common(str, Enum):
    BYBIT = "bybit"
    OKX = "okx"
    BITMART = "bitmart"
    GATEIO = "gateio"
    BINANCE = "binance"
    HYPERLIQUID = "hyperliquid"
    BINGX = "bingx"
    KUCOIN = "kucoin"
    ASCENDEX = "ascendex"

    def __str__(self) -> str:
        return self.value
