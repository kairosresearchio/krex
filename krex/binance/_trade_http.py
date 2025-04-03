from ._http_manager import HTTPManager
from .endpoints.trade import Trade


class TradeHTTP(HTTPManager):
    def new_order(self, 
        product_symbol: str,
        side: str,
        orderType: str,
        timeInForce: str = None, 
        quantity: bool = None,
        quoteOrderQty: bool = None,
        price: bool = None,
        newClientOrderId: str = None,
        strategyId: long = None, # what is long
        strategyType: int = None,
        stopPrice: bool = None,
        trailingDelta: long = None,
        icebergQty: bool = None,
        newOrderRespType: Enum = None,
        recvWindow: int = 5000,
        timestamp = None
    ):
        """
        Send in a new order.
        Weight: 1
        """
        payload = {}

        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if quantity is not None:
            payload["quantity"] = quantity
        if quoteOrderQty is not None:    
            payload["quoteOrderQty"] = quoteOrderQty    
        if price is not None:
            payload["price"] = price
        if newClientOrderId is not None:
            payload["newClientOrderId"] = newClientOrderId
        if strategyId is not None:
            payload["strategyId"] = strategyId
        if strategyType is not None:
            payload["strategyType"] = strategyType
        if stopPrice is not None:
            payload["stopPrice"] = stopPrice
        if trailingDelta is not None:
            payload["trailingDelta"] = trailingDelta
        if icebergQty is not None:
            payload["icebergQty"] = icebergQty
        if newOrderRespType is not None:
            payload["newOrderRespType"] = newOrderRespType
        if recvWindow is not None:
            payload["recvWindow"] = recvWindow
        if timestamp is not None:
            payload["timestamp"] = timestamp
        
        # might need to add additional params
            

        return self._request(
            method="POST",
            path=Trade.NEW_ORDER,
            query=payload
        )
    def test_new_order(self, 
        product_symbol: str,
        side: str,
        orderType: str,
        timeInForce: str = None, 
        quantity: bool = None,
        quoteOrderQty: bool = None,
        price: bool = None,
        newClientOrderId: str = None,
        strategyId: long = None, # what is long
        strategyType: int = None,
        stopPrice: bool = None,
        trailingDelta: long = None,
        icebergQty: bool = None,
        newOrderRespType: Enum = None,
        recvWindow: int = 5000,
        timestamp = None
        ):
        """
        Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.
        Weight: 
        """

        payload = {}

        return self._request(
            method="GET",
            path=Trade.TEST_NEW_ORDER,
            query=payload