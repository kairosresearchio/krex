from enum import Enum


class SpotTrade(str, Enum):
    #  https://api-cloud.bitmart.com
    SUBMIT_ORDER = "/spot/v2/submit_order"
    CANCEL_ORDER = "/spot/v3/cancel_order"
    CANCEL_ALL_ORDERS = "/spot/v4/cancel_all"
    NEW_MARGIN_ORDER = "/spot/v1/margin/submit_order"
    QUERY_ORDER_BY_ID = "/spot/v4/query/order"
    QUERY_ORDER_BY_CLIENT_ORDER_ID = "/spot/v4/query/client-order"
    CURRENT_OPEN_ORDERS = "/spot/v4/query/open-orders"
    ACCOUNT_ORDERS = "/spot/v4/query/history-orders"
    ACCOUNT_TRADE_LIST = "/spot/v4/query/trades"
    ORDER_TRADE_LIST = "/spot/v4/query/order-trades"

    def __str__(self) -> str:
        return self.value


class FuturesTrade(str, Enum):
    # https://api-cloud-v2.bitmart.com
    SUBMIT_ORDER = "/contract/private/submit-order"
    MODIFY_LIMIT_ORDER = "/contract/private/modify-limit-order"
    CANCEL_ORDER = "/contract/private/cancel-order"
    CANCEL_ALL_ORDERS = "/contract/private/cancel-orders"
    TRANSFER = "/account/v1/transfer-contract"
    SUBMIT_LEVERAGE = "/contract/private/submit-leverage"
    GET_ORDER_DETAIL = "/contract/private/order"
    GET_ORDER_HISTORY = "/contract/private/order-history"
    GET_ALL_OPEN_ORDERS = "/contract/private/get-open-orders"
    GET_CURRENT_POSITION = "/contract/private/position"
    GET_ORDER_TRADE = "/contract/private/trades"
    GET_TRANSACTION_HISTORY = "/contract/private/transaction-history"
    GET_TRANSFER_LIST = "/account/v1/transfer-contract-list"

    def __str__(self) -> str:
        return self.value
