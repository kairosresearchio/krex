from enum import Enum


class FutureTrade(str, Enum):
    LIST_ALL_POSITIONS = "/futures/{settle}/positions"
    GET_SINGLE_POSITION = "/futures/{settle}/positions/{contract}"
    UPDATE_POSITION_LEVERAGE = "/futures/{settle}/positions/{contract}/leverage"
    DUAL_MODE_SWITCH = "/futures/{settle}/dual_mode"
    CREATE_FUTURES_ORDER = "/futures/{settle}/orders"
    LIST_FUTURES_ORDER = "/futures/{settle}/orders"
    CANCEL_ALL_OPEN_ORDERS_MATCHED = "/futures/{settle}/orders"
    CREATE_BATCH_FUTURES_ORDERS = "/futures/{settle}/batch_orders"
    GET_SINGLE_ORDER = "/futures/{settle}/orders/{order_id}"
    CANCEL_SINGLE_ORDER = "/futures/{settle}/orders/{order_id}"
    AMEND_ORDER = "/futures/{settle}/orders/{order_id}"
    LIST_PERSONAL_TRADING_HISTORY = "/futures/{settle}/my_trades"
    LIST_POSITION_CLOSE_HISTORY = "/futures/{settle}/position_close"
    LIST_AUTODELEVERAGING_HISTORY = "/futures/{settle}/auto_deleverages"
    
    
    def __str__(self) -> str:
        return self.value


class DeliveryTrade(str, Enum):
    LIST_ALL_POSITIONS = "/delivery/{settle}/positions"
    GET_SINGLE_POSITION = "/delivery/{settle}/positions/{contract}"
    UPDATE_POSITION_LEVERAGE = "/delivery/{settle}/positions/{contract}/leverage"
    CREATE_FUTURES_ORDER = "/delivery/{settle}/orders"
    LIST_FUTURES_ORDER = "/delivery/{settle}/orders"
    CANCEL_ALL_OPEN_ORDERS_MATCHED = "/delivery/{settle}/orders"
    GET_SINGLE_ORDER = "/delivery/{settle}/orders/{order_id}"
    CANCEL_SINGLE_ORDER = "/delivery/{settle}/orders/{order_id}"
    LIST_PERSONAL_TRADING_HISTORY = "/delivery/{settle}/my_trades"
    LIST_POSITION_CLOSE_HISTORY = "/delivery/{settle}/position_close"


class SpotTrade(str, Enum):
    LIST_ALL_POSITIONS = "/delivery/{settle}/positions"
    GET_SINGLE_POSITION = "/delivery/{settle}/positions/{contract}"
    UPDATE_POSITION_LEVERAGE = "/delivery/{settle}/positions/{contract}/leverage"
    CREATE_BATCH_ORDERS = "/spot/batch_orders"
    CREATE_SPOT_ORDER = "/spot/orders"
    CLOSE_POSITION_WHEN_CROSSCURRENCY_DISABLED = "/spot/cross_liquidate_orders"
    LIST_SPOT_ORDER = "/spot/orders"
    CANCEL_ALL_OPEN_ORDERS_MATCHED = "/spot/orders"
    GET_SINGLE_ORDER = "/spot/orders/{order_id}"
    AMEND_ORDER = "/spot/orders/{order_id}"
    CANCEL_SINGLE_ORDER = "/spot/orders/{order_id}"
    LIST_PERSONAL_TRADING_HISTORY = "/spot/my_trades"
    LIST_POSITION_CLOSE_HISTORY = "/delivery/{settle}/position_close"
    
    def __str__(self) -> str:
        return self.value