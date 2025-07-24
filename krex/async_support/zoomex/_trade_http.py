from ._http_manager import HTTPManager
from .endpoints.trade import Trade
from ...utils.common import Common


class TradeHTTP(HTTPManager):
    async def place_order(
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
            "category": self.ptm.get_exchange_type(Common.ZOOMEX, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol),
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

        return await self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=payload,
        )

    async def place_market_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderType="Market",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_market_buy_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_market_sell_order(
        self,
        product_symbol: str,
        qty: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_limit_order(
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
        return await self.place_order(
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

    async def place_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        timeInForce: str = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce=timeInForce,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side=side,
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            timeInForce="PostOnly",
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_post_only_limit_buy_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="Buy",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def place_post_only_limit_sell_order(
        self,
        product_symbol: str,
        qty: str,
        price: str,
        reduceOnly: bool = None,
        isLeverage: int = None,
        positionIdx: int = None,
    ):
        return await self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="Sell",
            qty=qty,
            price=price,
            reduceOnly=reduceOnly,
            isLeverage=isLeverage,
            positionIdx=positionIdx,
        )

    async def amend_order(
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
            "category": self.ptm.get_exchange_type(Common.ZOOMEX, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol),
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

        return await self._request(
            method="POST",
            path=Trade.AMEND_ORDER,
            query=payload,
        )

    async def cancel_order(
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
            "category": self.ptm.get_exchange_type(Common.ZOOMEX, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId

        return await self._request(
            method="POST",
            path=Trade.CANCEL_ORDER,
            query=payload,
        )

    async def cancel_all_orders(
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
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.ZOOMEX, product_symbol)

        return await self._request(
            method="POST",
            path=Trade.CANCEL_ALL_ORDERS,
            query=payload,
        )
