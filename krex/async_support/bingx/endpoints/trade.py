from enum import Enum


class SwapTrade(str, Enum):
    PLACE_ORDER = "/openApi/swap/v2/trade/order"
    PLACE_BATCH_ORDER = "/openApi/swap/v2/trade/batchOrders"
    CANCEL_ORDER = "/openApi/swap/v2/trade/order"
    CANCEL_BATCH_ORDER = "/openApi/swap/v2/trade/batchOrders"
    CANCEL_ALL_OPEN_ORDERS = "/openApi/swap/v2/trade/allOpenOrders"
    REPLACE_ORDER = "/openApi/swap/v1/trade/cancelReplace"
    CLOSE_POSITION = "/openApi/swap/v1/trade/closePosition"
    CLOSE_ALL_POSITIONS = "/openApi/swap/v2/trade/closeAllPositions"

    QUERY_ORDER_DETAIL = "/openApi/swap/v2/trade/order"
    QUERY_ALL_OPEN_ORDERS = "/openApi/swap/v2/trade/openOrders"
    QUERY_ORDER_HISTORY = "/openApi/swap/v2/trade/allOrders"

    CHANGE_MARGIN_TYPE = "/openApi/swap/v2/trade/marginType"
    QUERY_MARGIN_TYPE = "/openApi/swap/v2/trade/marginType"
    SET_LEVERAGE = "/openApi/swap/v2/trade/leverage"
    QUERY_LEVERAGE = "/openApi/swap/v2/trade/leverage"
    SET_POSITION_MODE = "/openApi/swap/v1/positionSide/dual"
    QUERY_POSITION_MODE = "/openApi/swap/v1/positionSide/dual"

    def __str__(self) -> str:
        return self.value
