from ._http_manager import HTTPManager
from .endpoints.trade import Trade


class TradeHTTP(HTTPManager):
    def place_order(
        self,
        product_symbol: str,
        side: str,
        orderType: str,
        qty: str,
        price: str = None,
        isLeverage: int = None,
        marketUnit: str = None,
        triggerDirection: int = None,
        orderFilter: str = None,
        triggerPrice: str = None,
        triggerBy: str = None,
        orderIv: str = None,
        timeInForce: str = None,
        takeProfit: str = None,
        stopLoss: str = None,
        tpTriggerBy: str = None,
        slTriggerBy: str = None,
        reduceOnly: bool = None,
        closeOnTrigger: bool = None,
        tpslMode: str = None,
        tpLimitPrice: str = None,
        slLimitPrice: str = None,
        tpOrderType: str = None,
        slOrderType: str = None,
    ):
        payload = {
            "category": self.ptm.get_product_type(product_symbol, "bybit"),
            "symbol": self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            "side": side,
            "orderType": orderType,
            "qty": qty,
        }
        if price is not None:
            payload["price"] = price
        if isLeverage is not None:
            payload["isLeverage"] = isLeverage
        if marketUnit is not None:
            payload["marketUnit"] = marketUnit
        if triggerDirection is not None:
            payload["triggerDirection"] = triggerDirection
        if orderFilter is not None:
            payload["orderFilter"] = orderFilter
        if triggerPrice is not None:
            payload["triggerPrice"] = triggerPrice
        if triggerBy is not None:
            payload["triggerBy"] = triggerBy
        if orderIv is not None:
            payload["orderIv"] = orderIv
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if takeProfit is not None:
            payload["takeProfit"] = takeProfit
        if stopLoss is not None:
            payload["stopLoss"] = stopLoss
        if tpTriggerBy is not None:
            payload["tpTriggerBy"] = tpTriggerBy
        if slTriggerBy is not None:
            payload["slTriggerBy"] = slTriggerBy
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if closeOnTrigger is not None:
            payload["closeOnTrigger"] = closeOnTrigger
        if tpslMode is not None:
            payload["tpslMode"] = tpslMode
        if tpLimitPrice is not None:
            payload["tpLimitPrice"] = tpLimitPrice
        if slLimitPrice is not None:
            payload["slLimitPrice"] = slLimitPrice
        if tpOrderType is not None:
            payload["tpOrderType"] = tpOrderType
        if slOrderType is not None:
            payload["slOrderType"] = slOrderType

        return self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=payload,
        )

    def place_market_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side=side,
            orderType="Market",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
        )

    def place_market_buy_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_market_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Buy",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
        )

    def place_market_sell_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_market_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Sell",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
        )

    def place_limit_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
    ):
        return self.place_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side=side,
            orderType="Limit",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
        )

    def place_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
    ):
        return self.place_limit_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
        )

    def place_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
    ):
        return self.place_limit_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
        )

    def place_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_limit_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side=side,
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce="PostOnly",
            isLeverage=isLeverage,
        )

    def place_post_only_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_post_only_limit_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
        )

    def place_post_only_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
    ):
        return self.place_post_only_limit_order(
            category=self.ptm.get_product_type(product_symbol, "bybit"),
            symbol=self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
        )

    def amend_order(
        self,
        product_symbol: str,
        orderId: str = None,
        orderLinkId: str = None,
        orderIv: str = None,
        triggerPrice: str = None,
        qty: str = None,
        price: str = None,
        tpslMode: str = None,
        takeProfit: str = None,
        stopLoss: str = None,
        tpTriggerBy: str = None,
        slTriggerBy: str = None,
        triggerBy: str = None,
        tpLimitPrice: str = None,
        slLimitPrice: str = None,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        """
        payload = {
            "category": self.ptm.get_product_type(product_symbol, "bybit"),
            "symbol": self.ptm.get_exchange_symbol(product_symbol, "bybit"),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if orderLinkId is not None:
            payload["orderLinkId"] = orderLinkId
        if orderIv is not None:
            payload["orderIv"] = orderIv
        if triggerPrice is not None:
            payload["triggerPrice"] = triggerPrice
        if qty is not None:
            payload["qty"] = qty
        if price is not None:
            payload["price"] = price
        if tpslMode is not None:
            payload["tpslMode"] = tpslMode
        if takeProfit is not None:
            payload["takeProfit"] = takeProfit
        if stopLoss is not None:
            payload["stopLoss"] = stopLoss
        if tpTriggerBy is not None:
            payload["tpTriggerBy"] = tpTriggerBy
        if slTriggerBy is not None:
            payload["slTriggerBy"] = slTriggerBy
        if triggerBy is not None:
            payload["triggerBy"] = triggerBy
        if tpLimitPrice is not None:
            payload["tpLimitPrice"] = tpLimitPrice
        if slLimitPrice is not None:
            payload["slLimitPrice"] = slLimitPrice

        return self._request(
            method="POST",
            path=Trade.AMEND_ORDER,
            query=payload,
        )

    def cancel_order(
        self,
        product_symbol: str,
        orderId: str = None,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        :param orderId: str
        """
        payload = {
            "category": self.ptm.get_product_type(product_symbol, "bybit"),
            "symbol": self.ptm.get_exchange_symbol(product_symbol, "bybit"),
        }
        if orderId is not None:
            payload["orderId"] = orderId

        return self._request(
            method="POST",
            path=Trade.CANCEL_ORDER,
            query=payload,
        )

    def get_open_orders(
        self,
        category: str,
        symbol: str = None,
        limit: int = 20,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        :param limit: int
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if symbol is not None:
            payload["symbol"] = symbol

        return self._request(
            method="GET",
            path=Trade.GET_OPEN_ORDERS,
            query=payload,
        )

    def cancel_all_orders(
        self,
        category: str = "linear",
        product_symbol: str = None,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        """
        payload = {
            "category": category,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, "bybit")
            payload["category"] = self.ptm.get_product_type(product_symbol, "bybit")

        return self._request(
            method="POST",
            path=Trade.CANCEL_ALL_ORDERS,
            query=payload,
        )

    def get_order_history(
        self,
        category: str = "linear",
        product_symbol: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, "bybit")
            payload["category"] = self.ptm.get_product_type(product_symbol, "bybit")
        if startTime is not None:
            payload["startTime"] = startTime

        return self._request(
            method="GET",
            path=Trade.GET_ORDER_HISTORY,
            query=payload,
        )

    def get_execution_list(
        self,
        category: str = "linear",
        product_symbol: str = None,
        startTime: int = None,
        limit: int = 50,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, "bybit")
            payload["category"] = self.ptm.get_product_type(product_symbol, "bybit")
        if startTime is not None:
            payload["startTime"] = startTime

        return self._request(
            method="GET",
            path=Trade.GET_EXECUTION_LIST,
            query=payload,
        )

    def place_batch_order(
        self,
        category: str,
        request: list,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param request: list
            request=[
                {
                    "symbol": "BTCUSDT",
                    "side": "Buy",
                    "orderType": "Limit",
                    "isLeverage": 0,
                    "qty": "0.05",
                    "price": "30000",
                    "timeInForce": "GTC",
                    "orderLinkId": "spot-btc-03"
                },
            ]
        """
        payload = {
            "category": category,
            "request": request,
        }

        return self._request(
            method="POST",
            path=Trade.BATCH_PLACE_ORDER,
            query=payload,
        )

    def amend_batch_order(
        self,
        category: str,
        request: list,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param request: list
            request=[
                {
                    "category": "option",
                    "symbol": "ETH-30DEC22-500-C",
                    "orderIv": "6.8",
                    "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"
                },
            ]
        """
        payload = {
            "category": category,
            "request": request,
        }

        return self._request(
            method="POST",
            path=Trade.BATCH_AMEND_ORDER,
            query=payload,
        )

    def cancel_batch_order(
        self,
        category: str,
        request: list,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param request: list
            request=[
                {
                    "symbol": "BTCUSDT",
                    "orderId": "1666800494330512128"
                },
            ]
        """
        payload = {
            "category": category,
            "request": request,
        }

        return self._request(
            method="POST",
            path=Trade.BATCH_CANCEL_ORDER,
            query=payload,
        )

    def get_borrow_quota(
        self,
        product_symbol: str,
        side: str,
    ):
        """
        :param symbol: str
        :param side: str
        """
        payload = {
            "category": "spot",
            "symbol": self.ptm.get_exchange_symbol(product_symbol, "bybit"),
            "side": side,
        }

        return self._request(
            method="GET",
            path=Trade.GET_BORROW_QUOTA,
            query=payload,
        )

    def set_dcp(
        self,
        timeWindow: int,
        product: str = None,
    ):
        """
        :param timeWindow: int
        :param product: str
        """
        payload = {
            "timeWindow": timeWindow,
        }
        if product is not None:
            payload["product"] = product

        return self._request(
            method="POST",
            path=Trade.SET_DCP,
            query=payload,
        )
