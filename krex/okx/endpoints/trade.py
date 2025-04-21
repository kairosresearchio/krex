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
    ONE_CLICK_REPAY_SUPPORT = "/api/v5/trade/one-click-repay-currency-list"
    ONE_CLICK_REPAY = "/api/v5/trade/one-click-repay"
    ONE_CLICK_REPAY_HISTORY = "/api/v5/trade/one-click-repay-history"
    MASS_CANCEL = "/api/v5/trade/mass-cancel"
    CANCEL_ALL_AFTER = "/api/v5/trade/cancel-all-after"
    ACCOUNT_RATE_LIMIT = "/api/v5/trade/account-rate-limit"
