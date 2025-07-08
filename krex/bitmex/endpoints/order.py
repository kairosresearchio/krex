from enum import Enum


class Order(str, Enum):
    PLACE_ORDER = "/api/v2/order"
    AMEND_ORDER = "/api/v2/order"
    CANCEL_ORDER = "/api/v2/order"
    CANCEL_ALL_ORDERS = "/api/v2/order/all"
    QUERY_ORDER = "/api/v1/order"

    def __str__(self) -> str:
        return self.value
