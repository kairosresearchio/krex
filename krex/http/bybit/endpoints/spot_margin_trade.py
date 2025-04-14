from enum import Enum


class SpotMarginTrade(str, Enum):
    VIP_MARGIN_DATA = "/v5/spot-margin-trade/data"
    GET_COLLATERAL = "/v5/spot-margin-trade/collateral"
    HISTORICAL_INTEREST = "/v5/spot-margin-trade/interest-rate-history"
    TOGGLE_MARGIN_TRADE = "/v5/spot-margin-trade/switch-mode"
    SET_LEVERAGE = "/v5/spot-margin-trade/set-leverage"
    STATUS_AND_LEVERAGE = "/v5/spot-margin-trade/state"

    def __str__(self) -> str:
        return self.value
