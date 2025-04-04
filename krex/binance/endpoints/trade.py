from enum import Enum


class FuturesTrade(str, Enum):
    # https://fapi.binance.com
    PLACE_ORDER = "/fapi/v1/order"
    CANCEL_ORDER = "/fapi/v1/order"
    CANCEL_ALL_OPEN_ORDERS = "/fapi/v1/allOpenOrders"
    QUERY_ORDER = "/fapi/v1/order"
    QUERY_ALL_ORDERS = "/fapi/v1/allOrders"
    QUERY_OPEN_ORDER = "/fapi/v1/openOrder"
    QUERY_OPEN_ORDERS = "/fapi/v1/openOrders"
    POSITION_INFO = "/fapi/v3/positionRisk"

    def __str__(self) -> str:
        return self.value
