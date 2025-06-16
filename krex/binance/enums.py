from enum import Enum


class BinanceExchangeType(str, Enum):
    SPOT = "spot"
    SWAP = "swap"

    def __str__(self) -> str:
        return self.value
