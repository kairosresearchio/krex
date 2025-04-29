from .endpoints.trade import FuturesTrade
from ._http_manager import HTTPManager
from ..utils.common import Common


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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
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
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
        }

        res = self._request(
            method="GET",
            path=FuturesTrade.POSITION_INFO,
            query=payload,
        )
        return res
