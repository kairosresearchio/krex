from enum import Enum


class Trade(str, Enum):
    PLACE_ORDER = "/v5/order/create"
    AMEND_ORDER = "/v5/order/amend"
    CANCEL_ORDER = "/v5/order/cancel"
    GET_OPEN_ORDERS = "/v5/order/realtime"
    CANCEL_BATCH_ORDERS = "/v5/order/cancel-batch"
    CANCEL_ALL_ORDERS = "/v5/order/cancel-all"
    GET_ORDER_HISTORY = "/v5/order/history"
    GET_EXECUTION_LIST = "/v5/execution/list"
    BATCH_PLACE_ORDER = "/v5/order/create-batch"
    BATCH_AMEND_ORDER = "/v5/order/amend-batch"
    GET_BORROW_QUOTA = "/v5/order/spot-borrow-check"

    def __str__(self) -> str:
        return self.value


class SpotMarginTrade(str, Enum):
    VIP_MARGIN_DATA = "/v5/spot-margin-trade/data"
    GET_COLLATERAL = "/v5/spot-margin-trade/collateral"
    HISTORICAL_INTEREST = "/v5/spot-margin-trade/interest-rate-history"
    TOGGLE_MARGIN_TRADE = "/v5/spot-margin-trade/switch-mode"
    SET_LEVERAGE = "/v5/spot-margin-trade/set-leverage"
    STATUS_AND_LEVERAGE = "/v5/spot-margin-trade/state"

    def __str__(self) -> str:
        return self.value
