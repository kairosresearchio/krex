from enum import Enum


class Trade(str, Enum):
    ADD_ORDER = "/0/private/AddOrder"
    ADD_ORDER_BATCH = "/0/private/AddOrderBatch"
    AMEND_ORDER = "/0/private/AmendOrder"
    # EDIT_ORDER = "/0/private/EditOrder" # updated amend order resolves caveats in this, with additional performance gains
    CANCEL_ORDER = "/0/private/CancelOrder"
    CANCEL_ALL_ORDER = "/0/private/CancelAll"
    CANCEL_ALL_ORDERS_AFTER = "/0/private/CancelAllOrdersAfter"
    CANCEL_ORDER_BATCH = "/0/private/CancelOrderBatch"
    GET_WEBSOCKETS_TOKEN = "/0/private/GetWebSocketsToken"
   
    def __str__(self) -> str:
        return self.value
