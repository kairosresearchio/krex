from enum import Enum


class Common(str, Enum):
    BYBIT = "bybit"
    OKX = "okx"
    BITMART = "bitmart"
    GATEIO = "gateio"

    def __str__(self) -> str:
        return self.value
