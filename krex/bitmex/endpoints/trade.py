from enum import Enum


class Trade(str, Enum):
    PLACE_ORDER = ""

    def __str__(self) -> str:
        return self.value
