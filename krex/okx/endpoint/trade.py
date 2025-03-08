from enum import Enum


class Trade(str, Enum):
    PLACE_ORDER = "/api/v5/trade/order"
    BATCH_ORDERS = "/api/v5/trade/batch-orders"
    CANCEL_ORDER = "/api/v5/trade/cancel-order"
    CANCEL_BATCH_ORDERS = "/api/v5/trade/cancel-batch-orders"
    AMEND_ORDER = "/api/v5/trade/amend-order"
    AMEND_BATCH_ORDER = "/api/v5/trade/amend-batch-orders"
    CLOSE_POSITION = "/api/v5/trade/close-position"
    ORDER_INFO = "/api/v5/trade/order"
    ORDERS_PENDING = "/api/v5/trade/orders-pending"
    ORDERS_HISTORY = "/api/v5/trade/orders-history"
    ORDERS_HISTORY_ARCHIVE = "/api/v5/trade/orders-history-archive"
    ORDER_FILLS = "/api/v5/trade/fills"
    ORDERS_FILLS_HISTORY = "/api/v5/trade/fills-history"
    EASY_CONVERT_CURRENCY_LIST = "/api/v5/trade/easy-convert-currency-list"
    EASY_CONVERT = "/api/v5/trade/easy-convert"
    CONVERT_EASY_HISTORY = "/api/v5/trade/easy-convert-history"
    ONE_CLICK_REPAY_SUPPORT = "/api/v5/trade/one-click-repay-currency-list"
    ONE_CLICK_REPAY = "/api/v5/trade/one-click-repay"
    ONE_CLICK_REPAY_HISTORY = "/api/v5/trade/one-click-repay-history"
    MASS_CANCEL = "/api/v5/trade/mass-cancel"  # Need to add
    CANCEL_ALL_AFTER = "/api/v5/trade/cancel-all-after"  # Need to add
    ACCOUNT_RATE_LIMIT = "/api/v5/trade/account-rate-limit"  # Need to add
    ORDER_PRECHECK = "/api/v5/trade/order-precheck"  # Need to add
    PLACE_ALGO_ORDER = "/api/v5/trade/order-algo"
    CANCEL_ALGOS = "/api/v5/trade/cancel-algos"
    AMEND_ALGO_ORDER = "/api/v5/trade/amend-algos"
    CANCEL_ADVANCE_ALGOS = "/api/v5/trade/cancel-advance-algos"
    GET_ALGO_ORDER_DETAILS = "/api/v5/trade/order-algo"
    ORDERS_ALGO_PENDING = "/api/v5/trade/orders-algo-pending"
    ORDERS_ALGO_HISTORY = "/api/v5/trade/orders-algo-history"
