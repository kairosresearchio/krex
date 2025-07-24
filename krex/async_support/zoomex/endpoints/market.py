from enum import Enum


class Market(str, Enum):
    GET_INSTRUMENTS_INFO = "/cloud/trade/v3/market/instruments-info"

    def __str__(self) -> str:
        return self.value
