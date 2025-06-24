from .endpoints.trade import FuturesTrade, SpotTrade
from ._http_manager import HTTPManager
from ..utils.common import Common
import time


class TradeHTTP(HTTPManager):
    def set_leverage(
        self,
        product_symbol: str,
        leverage: int,
    ):
        """
        :param product_symbol: str
        :param leverage: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
            "leverage": leverage,
        }

        res = self._request(
            method="POST",
            path=FuturesTrade.SET_LEVERAGE,
            query=payload,
        )
        return res

    def place_future_order(
        self,
        product_symbol: str,
        side: str,
        type_: str,
        quantity: str = None,
        price: str = None,
        timeInForce: str = None,
        positionSide: str = None,
        reduceOnly: str = None,
        stopPrice: str = None,
        closePosition: str = None,
        activationPrice: str = None,
        callbackRate: str = None,
        workingType: str = None,
        priceProtect: str = None,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
        priceMatch: str = None,
        selfTradePreventionMode: str = None,
        goodTillDate: int = None,
    ):
        """
        :param product_symbol: str
        :param side: str
        :param type_: str
        :param quantity: str
        :param price: str
        :param timeInForce: str
        :param positionSide: str
        :param reduceOnly: str
        :param stopPrice: str
        :param closePosition: str
        :param activationPrice: str
        :param callbackRate: str
        :param workingType: str
        :param priceProtect: str
        :param newClientOrderId: str
        :param newOrderRespType: str
        :param priceMatch: str
        :param selfTradePreventionMode: str
        :param goodTillDate: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
            "side": side,
            "type": type_,
        }

        if quantity is not None:
            payload["quantity"] = quantity
        if price is not None:
            payload["price"] = price
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if positionSide is not None:
            payload["positionSide"] = positionSide
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if stopPrice is not None:
            payload["stopPrice"] = stopPrice
        if closePosition is not None:
            payload["closePosition"] = closePosition
        if activationPrice is not None:
            payload["activationPrice"] = activationPrice
        if callbackRate is not None:
            payload["callbackRate"] = callbackRate
        if workingType is not None:
            payload["workingType"] = workingType
        if priceProtect is not None:
            payload["priceProtect"] = priceProtect
        if newClientOrderId is not None:
            payload["newClientOrderId"] = newClientOrderId
        if newOrderRespType is not None:
            payload["newOrderRespType"] = newOrderRespType
        if priceMatch is not None:
            payload["priceMatch"] = priceMatch
        if selfTradePreventionMode is not None:
            payload["selfTradePreventionMode"] = selfTradePreventionMode
        if goodTillDate is not None:
            payload["goodTillDate"] = goodTillDate

        res = self._request(
            method="POST",
            path=FuturesTrade.PLACE_CANCEL_QUERY_ORDER,
            query=payload,
        )
        return res

    def place_future_market_order(
        self,
        product_symbol: str,
        side: str,
        quantity: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_order(
            product_symbol=product_symbol,
            side=side,
            type_="MARKET",
            quantity=quantity,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_market_buy_order(
        self,
        product_symbol: str,
        quantity: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_market_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_market_sell_order(
        self,
        product_symbol: str,
        quantity: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_market_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_limit_order(
        self,
        product_symbol: str,
        side: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_order(
            product_symbol=product_symbol,
            side=side,
            type_="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_limit_buy_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_limit_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_limit_sell_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_limit_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        quantity: str,
        price: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_order(
            product_symbol=product_symbol,
            side=side,
            type_="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTX",  # GTX = Post Only
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_post_only_limit_buy_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_post_only_limit_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def place_future_post_only_limit_sell_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        positionSide: str = None,
        reduceOnly: str = None,
    ):
        return self.place_future_post_only_limit_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            reduceOnly=reduceOnly,
        )

    def cancel_future_order(
        self,
        product_symbol: str,
        orderId: int = None,
        origClientOrderId: str = None,
    ):
        """
        :param product_symbol: str
        :param orderId: int
        :param origClientOrderId: str

        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if origClientOrderId is not None:
            payload["origClientOrderId"] = origClientOrderId

        res = self._request(
            method="DELETE",
            path=FuturesTrade.PLACE_CANCEL_QUERY_ORDER,
            query=payload,
        )
        return res

    def get_future_order(
        self,
        product_symbol: str,
        orderId: int = None,
        origClientOrderId: str = None,
    ):
        """
        :param product_symbol: str
        :param orderId: int
        :param origClientOrderId: str

        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if origClientOrderId is not None:
            payload["origClientOrderId"] = origClientOrderId

        res = self._request(
            method="GET",
            path=FuturesTrade.PLACE_CANCEL_QUERY_ORDER,
            query=payload,
        )
        return res

    def cancel_all_future_open_order(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str

        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }

        res = self._request(
            method="DELETE",
            path=FuturesTrade.CANCEL_ALL_OPEN_ORDERS,
            query=payload,
        )
        return res

    def get_future_all_order(
        self,
        product_symbol: str,
        orderId: int = None,
        startTime: int = None,
        endTime: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param orderId: int
        :param startTime: int
        :param endTime: int
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=FuturesTrade.QUERY_ALL_ORDERS,
            query=payload,
        )
        return res

    def get_future_open_order(
        self,
        product_symbol: str,
        orderId: int = None,
        origClientOrderId: str = None,
    ):
        """
        :param product_symbol: str

        EitherorderId or origClientOrderId must be sent
        :param orderId: int
        :param origClientOrderId: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if origClientOrderId is not None:
            payload["origClientOrderId"] = origClientOrderId

        res = self._request(
            method="GET",
            path=FuturesTrade.QUERY_OPEN_ORDER,
            query=payload,
        )
        return res

    def get_future_all_open_order(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
        }

        res = self._request(
            method="GET",
            path=FuturesTrade.QUERY_OPEN_ORDERS,
            query=payload,
        )
        return res

    def get_future_position(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol),
        }

        res = self._request(
            method="GET",
            path=FuturesTrade.POSITION_INFO,
            query=payload,
        )
        return res

    """
    ---------------------------------------------------------
    """

    def place_spot_order(
        self,
        product_symbol: str,
        side: str,
        type_: str,
        quantity: float = None,
        quoteOrderQty: float = None,
        price: float = None,
        timeInForce: str = None,
        newClientOrderId: str = None,
        strategyId: int = None,
        strategyType: int = None,
        stopPrice: float = None,
        trailingDelta: int = None,
        icebergQty: float = None,
        newOrderRespType: str = None,
        selfTradePreventionMode: str = None,
        recvWindow: int = None,
        timestamp: int = int(time.time() * 1000),
    ):
        """
        Place a spot order on Binance
        :param product_symbol: str
        :param side: str
        :param type_: str
        :param quantity: float
        :param quoteOrderQty: float
        :param price: float
        :param timeInForce: str
        :param newClientOrderId: str
        :param strategyId: int
        :param strategyType: int
        :param stopPrice: float
        :param trailingDelta: int
        :param icebergQty: float
        :param newOrderRespType: str
        :param selfTradePreventionMode: str
        :param recvWindow: int
        :param timestamp: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
            "side": side,
            "type": type_,
            "timestamp": timestamp,
        }

        # Required parameters based on order type
        if quantity is not None:
            payload["quantity"] = quantity
        if quoteOrderQty is not None:
            payload["quoteOrderQty"] = quoteOrderQty
        if price is not None:
            payload["price"] = price
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
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
        if selfTradePreventionMode is not None:
            payload["selfTradePreventionMode"] = selfTradePreventionMode
        if recvWindow is not None:
            payload["recvWindow"] = recvWindow

        res = self._request(
            method="POST",
            path=SpotTrade.PLACE_SPOT_ORDER,
            query=payload,
        )
        return res

    def place_spot_market_order(
        self,
        product_symbol: str,
        side: str,
        quantity: float = None,
        quoteOrderQty: float = None,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a market order

        :param product_symbol: str - Trading pair symbol
        :param side: str - BUY or SELL
        :param quantity: float - Amount of base asset to buy/sell
        :param quoteOrderQty: float - Amount of quote asset to buy/sell
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_order(
            product_symbol=product_symbol,
            side=side,
            type_="MARKET",
            quantity=quantity,
            quoteOrderQty=quoteOrderQty,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_market_buy_order(
        self,
        product_symbol: str,
        quantity: str = None,
        quoteOrderQty: str = None,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a market buy order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to buy
        :param quoteOrderQty: str - Amount of quote asset to spend
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_market_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            quoteOrderQty=quoteOrderQty,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_market_sell_order(
        self,
        product_symbol: str,
        quantity: float = None,
        quoteOrderQty: float = None,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a market sell order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to sell
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_market_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            quoteOrderQty=quoteOrderQty,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_limit_order(
        self,
        product_symbol: str,
        side: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a limit order

        :param product_symbol: str - Trading pair symbol
        :param side: str - BUY or SELL
        :param quantity: str - Amount of base asset to buy/sell
        :param price: str - Order price
        :param timeInForce: str - GTC, IOC, FOK
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_order(
            product_symbol=product_symbol,
            side=side,
            type_="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_limit_buy_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a limit buy order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to buy
        :param price: str - Order price
        :param timeInForce: str - GTC, IOC, FOK
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_limit_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_limit_sell_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        timeInForce: str = "GTC",
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a limit sell order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to sell
        :param price: str - Order price
        :param timeInForce: str - GTC, IOC, FOK
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_limit_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        quantity: str,
        price: str,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a post-only limit order (LIMIT_MAKER)

        :param product_symbol: str - Trading pair symbol
        :param side: str - BUY or SELL
        :param quantity: str - Amount of base asset to buy/sell
        :param price: str - Order price
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_order(
            product_symbol=product_symbol,
            side=side,
            type_="LIMIT_MAKER",
            quantity=quantity,
            price=price,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_post_only_limit_buy_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a post-only limit buy order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to buy
        :param price: str - Order price
        :param newClientOrderId: str - Unique order ID
        :param icebergQty: str - Used to create iceberg orders
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_post_only_limit_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def place_spot_post_only_limit_sell_order(
        self,
        product_symbol: str,
        quantity: str,
        price: str,
        newClientOrderId: str = None,
        newOrderRespType: str = None,
    ):
        """
        Place a post-only limit sell order

        :param product_symbol: str - Trading pair symbol
        :param quantity: str - Amount of base asset to sell
        :param price: str - Order price
        :param newClientOrderId: str - Unique order ID
        :param newOrderRespType: str - Set response JSON: ACK, RESULT, or FULL
        """
        return self.place_spot_post_only_limit_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            newClientOrderId=newClientOrderId,
            newOrderRespType=newOrderRespType,
        )

    def cancel_spot_order(
        self,
        product_symbol: str,
        orderId: int = None,
        origClientOrderId: str = None,
        timestamp: int = int(time.time() * 1000),
    ):
        """
        Cancel an active spot order on Binance.

        :param product_symbol: str - Trading pair symbol, e.g., 'BTCUSDT'
        :param orderId: int - Binance internal order ID (preferred for performance)
        :param origClientOrderId: str - The client order ID used when placing the order
        :param newClientOrderId: str - Unique ID for this cancel request (optional)
        :param cancelRestrictions: str - 'ONLY_NEW' or 'ONLY_PARTIALLY_FILLED' (optional)
        :param recvWindow: int - Optional timeout window in ms (max: 60000)
        :return: Binance API response
        """
        payload = {"symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol), "timestamp": timestamp}

        # 至少要提供 orderId 或 origClientOrderId 其中之一
        if orderId is not None:
            payload["orderId"] = orderId
        elif origClientOrderId is not None:
            payload["origClientOrderId"] = origClientOrderId
        else:
            raise ValueError("Must provide either orderId or origClientOrderId to cancel an order.")

        # 發送 DELETE 請求
        res = self._request(method="DELETE", path=SpotTrade.PLACE_SPOT_ORDER, query=payload)
        return res

    def cancel_all_spot_orders(self, product_symbol: str, timestamp: int = int(time.time() * 1000)):
        """
        Cancel all active spot orders for a symbol on Binance.

        :param product_symbol: str - Trading pair symbol (e.g., "BTCUSDT")
        :param timestamp: int - Optional request timeout (max 60000)
        """
        payload = {"symbol": self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol), "timestamp": timestamp}

        res = self._request(
            method="DELETE",
            path=SpotTrade.CANCEL_ALL_SPOT_ORDERS,
            query=payload,
        )
        return res
