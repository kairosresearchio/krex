from enum import Enum


class Trade(str, Enum):
    # PLACE_ORDER = ""
    # general endpoints - not sure where to place yet
    # TEST_CONNECTIVITY = "/api/v3/ping" # get
    # CHECK_SERVER_TIME = "/api/v3/time"
    # EXCHANGE_INFO = "/api/v3/exchangeInfo"

    # trade endpoints
    NEW_ORDER = "/api/v3/order" # post, send in a new order
    TEST_NEW_ORDER = "/api/v3/order/test" # post, test new order creation and signature/recvWindow 
    QUERY_ORDER = "/api/v3/order" # get, check an order's status
    CANCEL_ORDER = "/api/v3/order" # delete, cancel an active order
    CANCEL_ALL_OPEN_ORDERS = "/api/v3/openOrders" # delete, cancel all active orders on a symbol. This includes orders that are a part of an order list
    CANCEL_AND_SEND_NEW_ORDER = "/api/v3/order/oco" # post, cancel an order and send a new one on the same symbol
    CURRENT_OPEN_ORDERS = "/api/v3/openOrders" # get, get all open orders on a symbol
    ALL_ORDERS = "/api/v3/allOrders" # get, get all account orders; active, canceled, or filled 
    NEW_OCO_DEPRECATED = "/api/v3/order/oco" # post, send in a new oco
    NEW_ORDER_LIST_OCO = "/api/v3/orderList/oco" # post, send in an oco pair, where activation of one order immediately cancels the other
    NEW_ORDER_LIST_OTO = "/api/v3/orderList/oto" # post, places an oto (working, pending)
    NEW_ORDER_LIST_OTOCO = "/api/v3/orderList/otoco" # post, places an otoco (working, pending oco pair)
    CANCEL_ORDER_LIST = "/api/v3/orderList" # delete, cancel an entire order list
    QUERY_ORDER_LIST = "/api/v3/orderList" # get, retrieves a specific order list 
    QUERY_ALL_ORDER_LISTS = "/api/v3/allOrderList" # get, retrieves all order lists 
    QUERY_OPEN_ORDER_LISTS = "/api/v3/openOrderList" # get, retrieves all open order lists
    NEW_ORDER_SOR = "/api/v3/sor/order" # post, send in a new SOR (smart order routing) order
    TEST_NEW_ORDER_SOR = "/api/v3/sor/order/test" # post, test new SOR order creation and signature/recvWindow. . Creates and validates a new order but does not send it into the matching engine.
    

    def __str__(self) -> str:
        return self.value

