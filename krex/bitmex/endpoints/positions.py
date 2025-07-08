from enum import Enum


class Positions(str, Enum):
    GET_POSITIONS = "/api/v1/position"
    SWITCH_MODE = "/api/v1/position/isolate"
    LEVERAGE = "/api/v1/position/leverage"
    MARGINING_MODE = "/api/v1/user/marginingMode"
    GET_MARGIN = "/api/v1/user/margin"

    def __str__(self) -> str:
        return self.value
