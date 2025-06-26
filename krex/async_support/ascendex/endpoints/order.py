from enum import Enum


class SpotOrder(Enum):
    PLACE_ORDER = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order",
        "hash": "order",
    }
    CANCEL_ORDER = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order",
        "hash": "order",
    }
    CANCEL_ALL_ORDERS = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order/all",
        "hash": "order/all",
    }

    PLACE_BATCH_ORDERS = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order/batch",
        "hash": "order/batch",
    }
    CANCEL_BATCH_ORDERS = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order/batch",
        "hash": "order/batch",
    }

    QUERY_ORDER = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order/status",
        "hash": "order/status",
    }
    LIST_OPEN_ORDERS = {
        "route": "/{ACCOUNT_GROUP}/api/pro/v1/cash/order/open",
        "hash": "order/open",
    }
    LIST_ORDER_HISTORY = {
        "route": "/api/pro/data/v2/order/hist",
        "hash": "data/v2/order/hist",
    }

    @property
    def route(self):
        return self.value["route"]

    @property
    def hash(self):
        return self.value["hash"]

    def __str__(self) -> str:
        return self.value
