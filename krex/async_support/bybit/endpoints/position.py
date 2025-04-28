from enum import Enum


class Position(str, Enum):
    GET_POSITIONS = "/v5/position/list"
    SET_LEVERAGE = "/v5/position/set-leverage"
    SWITCH_POSITION_MODE = "/v5/position/switch-mode"
    GET_CLOSED_PNL = "/v5/position/closed-pnl"

    def __str__(self) -> str:
        return self.value
