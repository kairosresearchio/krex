from enum import Enum


class Trade(str, Enum):
    PLACE_ORDER = "/cloud/trade/v3/order/create"
    AMEND_ORDER = "/cloud/trade/v3/order/amend"
    CANCEL_ORDER = "/cloud/trade/v3/order/cancel"
    GET_OPEN_ORDERS = "/cloud/trade/v3/order/realtime"
    CANCEL_ALL_ORDERS = "/cloud/trade/v3/order/cancel-all"

    def __str__(self) -> str:
        return self.value
