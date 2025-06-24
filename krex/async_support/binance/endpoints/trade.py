from enum import Enum


class SpotTrade(str, Enum):
    PLACE_CANCEL_QUERY_ORDER = "/api/v3/order"
    PLACE_SPOT_ORDER = "/api/v3/order"
    CANCEL_ALL_ORDERS = "/api/v3/openOrders"
    CANCEL_ALL_SPOT_ORDERS = "/api/v3/openOrders"
    QUERY_OPEN_ORDER = "/api/v3/openOrders"

    def __str__(self) -> str:
        return self.value


class FuturesTrade(str, Enum):
    SET_LEVERAGE = "/fapi/v1/leverage"
    PLACE_CANCEL_QUERY_ORDER = "/fapi/v1/order"
    CANCEL_ALL_OPEN_ORDERS = "/fapi/v1/allOpenOrders"
    QUERY_ALL_ORDERS = "/fapi/v1/allOrders"
    QUERY_OPEN_ORDER = "/fapi/v1/openOrder"
    QUERY_OPEN_ORDERS = "/fapi/v1/openOrders"
    POSITION_INFO = "/fapi/v3/positionRisk"

    def __str__(self) -> str:
        return self.value
