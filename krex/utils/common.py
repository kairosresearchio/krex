from enum import Enum


class Common(str, Enum):
    BYBIT = "bybit"
    OKX = "okx"
    BITMART = "bitmart"

    def __str__(self) -> str:
        return self.value
