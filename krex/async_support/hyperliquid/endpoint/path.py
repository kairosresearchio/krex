from enum import Enum


class Path(str, Enum):
    INFO = "/info"
    EXCHANGE = "/exchange"

    def __str__(self) -> str:
        return self.value
