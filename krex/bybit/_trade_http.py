from ._http_manager import HTTPManager
from .endpoints.trade import Trade
from .endpoints.trade import SpotMarginTrade
from ..utils.common import Common


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
        positionIdx: int = None,
    ):
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
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
        if positionIdx is not None:
            payload["positionIdx"] = positionIdx

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
        positionIdx: int = None,
    ):
        return self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderType="Market",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_market_buy_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_market_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_market_sell_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_market_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
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
        positionIdx: int = None,
    ):
        return self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderType="Limit",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_limit_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_limit_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        timeInForce: str = None,
    ):
        return self.place_limit_order(
            product_symbol=product_symbol,
            side=side,
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce="PostOnly",
            isLeverage=isLeverage,
            positionIdx=None,
        )

    def place_post_only_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    def place_post_only_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
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
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
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
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
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
        product_symbol: str = None,
        limit: int = 20,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param product_symbol: str
        :param limit: int
        """
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "limit": limit,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)

        res = self._request(
            method="GET",
            path=Trade.GET_OPEN_ORDERS,
            query=payload,
        )
        return res

    def cancel_batch_orders(
        self,
        request: list,
        category: str = "linear",
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param request: list
            request=[
                {
                    "symbol": "BTCUSDT",
                    "orderId": "1666800494330512128"
                },
                {
                    "symbol": "ATOMUSDT",
                    "orderLinkId": "1666800494330512129"
                }
            ]
        """
        payload = {
            "category": category,
            "request": request,
        }

        return self._request(
            method="POST",
            path=Trade.CANCEL_BATCH_ORDERS,
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
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)

        return self._request(
            method="POST",
            path=Trade.CANCEL_ALL_ORDERS,
            query=payload,
        )

    def get_order_history(
        self,
        category: str = "linear",
        product_symbol: str = None,
        orderId: str = None,
        startTime: int = None,
        cursor: str = None,
        limit: int = None,
    ):
        """
        :param category: str (linear, option, spot, inverse)
        :param symbol: str
        :param orderId: str
        :param startTime: int
        :param cursor: str
        :param limit: int
        """
        payload = {
            "category": category,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if orderId is not None:
            payload["orderId"] = orderId
        if startTime is not None:
            payload["startTime"] = startTime
        if cursor is not None:
            payload["cursor"] = cursor
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.GET_ORDER_HISTORY,
            query=payload,
        )
        return res

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
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if startTime is not None:
            payload["startTime"] = startTime

        res = self._request(
            method="GET",
            path=Trade.GET_EXECUTION_LIST,
            query=payload,
        )
        return res

    def place_batch_order(
        self,
        request: list,
        category: str = "linear",
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
        request: list,
        category: str = "linear",
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
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
            "side": side,
        }

        res = self._request(
            method="GET",
            path=Trade.GET_BORROW_QUOTA,
            query=payload,
        )
        return res

    # spot margin trade http
    def get_vip_margin_data(
        self,
        vipLevel: str = None,
        currency: str = None,
    ):
        """
        :param vipLevel: str
        :param currency: str
        """
        payload = {}
        if vipLevel is not None:
            payload["vipLevel"] = vipLevel
        if currency is not None:
            payload["currency"] = currency

        res = self._request(
            method="GET",
            path=SpotMarginTrade.VIP_MARGIN_DATA,
            query=payload,
        )
        return res

    def get_collateral(
        self,
        currency: str = None,
    ):
        """
        :param currency: str
        """
        payload = {}
        if currency is not None:
            payload["currency"] = currency

        res = self._request(
            method="GET",
            path=SpotMarginTrade.GET_COLLATERAL,
            query=payload,
        )
        return res

    def get_historical_interest_rate(
        self,
        currency: str,
        vipLevel: str = None,
        startTime: int = None,
        endTime: int = None,
    ):
        """
        :param currency: str
        :param vipLevel: str
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "currency": currency,
        }
        if vipLevel is not None:
            payload["vipLevel"] = vipLevel
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime

        res = self._request(
            method="GET",
            path=SpotMarginTrade.HISTORICAL_INTEREST,
            query=payload,
        )
        return res

    def spot_margin_trade_toggle_margin_trade(
        self,
        spotMarginMode: str,
    ):
        """
        :param spotMarginMode: str (1: open, 0: close)
        """
        payload = {
            "spotMarginMode": spotMarginMode,
        }

        return self._request(
            method="POST",
            path=SpotMarginTrade.TOGGLE_MARGIN_TRADE,
            query=payload,
        )

    def spot_margin_trade_set_leverage(self, leverage: str):
        """
        :param leverage: str (2-10)
        """
        payload = {
            "leverage": leverage,
        }

        return self._request(
            method="POST",
            path=SpotMarginTrade.SET_LEVERAGE,
            query=payload,
        )

    def get_status_and_leverage(self):
        res = self._request(
            method="GET",
            path=SpotMarginTrade.STATUS_AND_LEVERAGE,
            query=None,
        )
        return res
