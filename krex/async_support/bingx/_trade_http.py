from ._http_manager import HTTPManager
from .endpoints.trade import SwapTrade
from ...utils.common import Common


class TradeHTTP(HTTPManager):
    async def place_swap_order(
        self,
        product_symbol: str,
        type_: str,
        side: str,
        positionSide: str = None,
        reduceOnly: str = None,
        price: float = None,
        quantity: float = None,
        stopPrice: float = None,
        priceRate: float = None,
        stopLoss: str = None,
        takeProfit: str = None,
        workingType: str = None,
        clientOrderId: str = None,
        recvWindow: int = None,
        timeInForce: str = None,
        closePosition: str = None,
        activationPrice: float = None,
        stopGuaranteed: str = None,
        positionId: int = None,
    ):
        """
        :param product_symbol: str
        :param type_: str (MARKET, LIMIT, etc)
        :param side: str
        :param positionSide: str
        :param reduceOnly: str (true, false)
        :param price: float
        :param quantity: float
        :param stopPrice: float
        :param priceRate: float
        :param stopLoss: str
        :param takeProfit: str
        :param workingType: str
        :param clientOrderId: str
        :param recvWindow: int
        :param timeInForce: str
        :param closePosition: str (true, false)
        :param activationPrice: float
        :param stopGuaranteed: str
        :param positionId: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
            "type": type_,
            "side": side,
        }
        if positionSide is not None:
            payload["positionSide"] = positionSide
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if price is not None:
            payload["price"] = price
        if quantity is not None:
            payload["quantity"] = quantity
        if stopPrice is not None:
            payload["stopPrice"] = stopPrice
        if priceRate is not None:
            payload["priceRate"] = priceRate
        if stopLoss is not None:
            payload["stopLoss"] = stopLoss
        if takeProfit is not None:
            payload["takeProfit"] = takeProfit
        if workingType is not None:
            payload["workingType"] = workingType
        if clientOrderId is not None:
            payload["clientOrderId"] = clientOrderId
        if recvWindow is not None:
            payload["recvWindow"] = recvWindow
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if closePosition is not None:
            payload["closePosition"] = closePosition
        if activationPrice is not None:
            payload["activationPrice"] = activationPrice
        if stopGuaranteed is not None:
            payload["stopGuaranteed"] = stopGuaranteed
        if positionId is not None:
            payload["positionId"] = positionId

        res = await self._request(
            method="POST",
            path=SwapTrade.PLACE_ORDER,
            query=payload,
        )
        return res

    async def place_swap_market_order(
        self,
        product_symbol: str,
        side: str,
        quantity: float,
        clientOrderId: str = None,
        reduceOnly: bool = None,
        positionSide: str = None,
    ):
        return await self.place_swap_order(
            product_symbol=product_symbol,
            type_="MARKET",
            side=side,
            quantity=quantity,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
            positionSide=positionSide,
        )

    async def place_swap_market_buy_order(
        self,
        product_symbol: str,
        quantity: float,
        positionSide: str = "LONG",
        clientOrderId: str = None,
        reduceOnly: bool = None,
    ):
        return await self.place_swap_market_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            positionSide=positionSide,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_market_sell_order(
        self,
        product_symbol: str,
        quantity: float,
        positionSide: str = "SHORT",
        clientOrderId: str = None,
        reduceOnly: bool = None,
    ):
        return await self.place_swap_market_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            positionSide=positionSide,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_limit_order(
        self,
        product_symbol: str,
        side: str,
        quantity: float,
        price: float,
        clientOrderId: str = None,
        timeInForce: str = "GTC",
        reduceOnly: bool = None,
        positionSide: str = None,
    ):
        return await self.place_swap_order(
            product_symbol=product_symbol,
            type_="LIMIT",
            side=side,
            quantity=quantity,
            price=price,
            clientOrderId=clientOrderId,
            timeInForce=timeInForce,
            reduceOnly=reduceOnly,
            positionSide=positionSide,
        )

    async def place_swap_limit_buy_order(
        self,
        product_symbol: str,
        quantity: float,
        price: float,
        positionSide: str = "LONG",
        timeInForce: str = "GTC",
        clientOrderId: str = None,
        reduceOnly: bool = None,
    ):
        return await self.place_swap_limit_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            timeInForce=timeInForce,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_limit_sell_order(
        self,
        product_symbol: str,
        quantity: float,
        price: float,
        positionSide: str = "SHORT",
        timeInForce: str = "GTC",
        clientOrderId: str = None,
        reduceOnly: bool = None,
    ):
        return await self.place_swap_limit_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            timeInForce=timeInForce,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_post_only_order(
        self,
        product_symbol: str,
        side: str,
        quantity: float,
        price: float,
        clientOrderId: str = None,
        timeInForce: str = "PostOnly",
        reduceOnly: str = None,
        positionSide: str = None,
    ):
        return await self.place_swap_order(
            product_symbol=product_symbol,
            type_="LIMIT",
            side=side,
            quantity=quantity,
            price=price,
            clientOrderId=clientOrderId,
            timeInForce=timeInForce,
            reduceOnly=reduceOnly,
            positionSide=positionSide,
        )

    async def place_swap_post_only_buy_order(
        self,
        product_symbol: str,
        quantity: float,
        price: float,
        positionSide: str = "LONG",
        clientOrderId: str = None,
        reduceOnly: str = None,
    ):
        return await self.place_swap_post_only_order(
            product_symbol=product_symbol,
            side="BUY",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_post_only_sell_order(
        self,
        product_symbol: str,
        quantity: float,
        price: float,
        positionSide: str = "SHORT",
        clientOrderId: str = None,
        reduceOnly: str = None,
    ):
        return await self.place_swap_post_only_order(
            product_symbol=product_symbol,
            side="SELL",
            quantity=quantity,
            price=price,
            positionSide=positionSide,
            clientOrderId=clientOrderId,
            reduceOnly=reduceOnly,
        )

    async def place_swap_batch_order(
        self,
        batchOrders: list,
    ):
        """
        :param batchOrders: list of order dicts
        """
        payload = {"batchOrders": batchOrders}
        res = await self._request(
            method="POST",
            path=SwapTrade.PLACE_BATCH_ORDER,
            query=payload,
        )
        return res

    async def cancel_swap_order(
        self,
        product_symbol: str,
        orderId: int = None,
        clientOrderId: str = None,
        recvWindow: int = None,
    ):
        """
        :param product_symbol: str
        :param orderId: int
        :param clientOrderId: str
        :param recvWindow: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if clientOrderId is not None:
            payload["clientOrderId"] = clientOrderId
        if recvWindow is not None:
            payload["recvWindow"] = recvWindow

        res = await self._request(
            method="DELETE",
            path=SwapTrade.CANCEL_ORDER,
            query=payload,
        )
        return res

    async def cancel_swap_batch_order(
        self,
        product_symbol: str,
        orderIdList: list = None,
        clientOrderIdList: list = None,
    ):
        """
        :param product_symbol: str
        :param orderIdList: list of orderId
        :param clientOrderIdList: list of clientOrderId
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if orderIdList is not None:
            payload["orderIdList"] = str(orderIdList).replace("'", "").replace(" ", "")
        if clientOrderIdList is not None:
            payload["clientOrderIdList"] = str(clientOrderIdList).replace("'", "").replace(" ", "")

        res = await self._request(
            method="DELETE",
            path=SwapTrade.CANCEL_BATCH_ORDER,
            query=payload,
        )
        return res

    async def cancel_swap_all_orders(
        self,
        product_symbol: str,
        type_: str = None,
    ):
        """
        :param product_symbol: str
        :param type_: str (LIMIT, MARKET)
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if type_ is not None:
            payload["type"] = type_

        res = await self._request(
            method="DELETE",
            path=SwapTrade.CANCEL_ALL_OPEN_ORDERS,
            query=payload,
        )
        return res

    async def replace_swap_order(
        self,
        product_symbol: str,
        orderId: str,
        cancelReplaceMode: str,
        type_: str,
        side: str,
        positionSide: str,
        cancelClientOrderId: int = None,
        cancelOrderId: str = None,
        cancelRestrictions: str = None,
        reduceOnly: str = None,
        price: float = None,
        quantity: float = None,
        stopPrice: float = None,
        priceRate: float = None,
        workingType: str = None,
        stopLoss: str = None,
        takeProfit: str = None,
        clientOrderId: str = None,
        closePosition: str = None,
        activationPrice: float = None,
        stopGuaranteed: str = None,
        timeInForce: str = None,
        positionId: int = None,
    ):
        """
        :param product_symbol: str
        :param orderId: str
        :param cancelReplaceMode: str
        :param type_: str
        :param side: str
        :param positionSide: str
        :param cancelClientOrderId: str
        :param cancelOrderId: str
        :param cancelRestrictions: str
        :param reduceOnly: bool (true, false)
        :param price: float
        :param quantity: float
        :param stopPrice: float
        :param priceRate: float
        :param workingType: str
        :param stopLoss: str
        :param takeProfit: str
        :param clientOrderId: str
        :param closePosition: str
        :param activationPrice: float
        :param stopGuaranteed: str
        :param timeInForce: str
        :param positionId: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
            "orderId": orderId,
            "cancelReplaceMode": cancelReplaceMode,
            "type": type_,
            "side": side,
            "positionSide": positionSide,
        }
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if price is not None:
            payload["price"] = price
        if quantity is not None:
            payload["quantity"] = quantity
        if cancelClientOrderId is not None:
            payload["cancelClientOrderId"] = cancelClientOrderId
        if cancelOrderId is not None:
            payload["cancelOrderId"] = cancelOrderId
        if cancelRestrictions is not None:
            payload["cancelRestrictions"] = cancelRestrictions
        if stopPrice is not None:
            payload["stopPrice"] = stopPrice
        if priceRate is not None:
            payload["priceRate"] = priceRate
        if workingType is not None:
            payload["workingType"] = workingType
        if stopLoss is not None:
            payload["stopLoss"] = stopLoss
        if takeProfit is not None:
            payload["takeProfit"] = takeProfit
        if clientOrderId is not None:
            payload["clientOrderId"] = clientOrderId
        if closePosition is not None:
            payload["closePosition"] = closePosition
        if activationPrice is not None:
            payload["activationPrice"] = activationPrice
        if stopGuaranteed is not None:
            payload["stopGuaranteed"] = stopGuaranteed
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if positionId is not None:
            payload["positionId"] = positionId

        res = await self._request(
            method="POST",
            path=SwapTrade.REPLACE_ORDER,
            query=payload,
        )
        return res

    async def close_swap_position(
        self,
        positionId: str,
    ):
        """
        :param positionId: str
        """
        payload = {
            "positionId": positionId,
        }

        res = await self._request(
            method="POST",
            path=SwapTrade.CLOSE_POSITION,
            query=payload,
        )
        return res

    async def close_swap_all_positions(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)

        res = await self._request(
            method="POST",
            path=SwapTrade.CLOSE_ALL_POSITIONS,
            query=payload,
        )
        return res

    async def get_order_detail(
        self,
        product_symbol: str,
        orderId: int = None,
        clientOrderId: str = None,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if orderId is not None:
            payload["orderId"] = orderId
        if clientOrderId is not None:
            payload["clientOrderId"] = clientOrderId

        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_ORDER_DETAIL,
            query=payload,
        )
        return res

    async def get_open_orders(
        self,
        product_symbol: str = None,
        type_: str = None,
    ):
        """
        :param product_symbol: str
        :param type_: str (LIMIT, MARKET)
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)
        if type_ is not None:
            payload["type"] = type_

        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_ALL_OPEN_ORDERS,
            query=payload,
        )
        return res

    async def get_order_history(
        self,
        product_symbol: str = None,
        currency: str = None,
        orderId: int = None,
        startTime: int = None,
        endTime: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param currency: str
        :param orderId: int
        :param startTime: int
        :param endTime: int
        :param limit: int
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)
        if currency is not None:
            payload["currency"] = currency
        if orderId is not None:
            payload["orderId"] = orderId
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_ORDER_HISTORY,
            query=payload,
        )
        return res

    async def change_margin_type(
        self,
        product_symbol: str,
        marginType: str,
    ):
        """
        :param product_symbol: str
        :param marginType: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
            "marginType": marginType,
        }

        res = await self._request(
            method="POST",
            path=SwapTrade.CHANGE_MARGIN_TYPE,
            query=payload,
        )
        return res

    async def get_margin_type(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)

        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_MARGIN_TYPE,
            query=payload,
        )
        return res

    async def set_leverage(
        self,
        product_symbol: str,
        side: str,
        leverage: int,
    ):
        """
        :param product_symbol: str
        :param side: str (LONG, SHORT)
        :param leverage: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
            "side": side,
            "leverage": leverage,
        }

        res = await self._request(
            method="POST",
            path=SwapTrade.SET_LEVERAGE,
            query=payload,
        )
        return res

    async def get_leverage(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_LEVERAGE,
            query=payload,
        )
        return res

    async def set_position_mode(
        self,
        dualSidePosition: bool,
    ):
        """
        :param dualSidePosition: bool
        """
        payload = {
            "dualSidePosition": dualSidePosition,
        }

        res = await self._request(
            method="POST",
            path=SwapTrade.SET_POSITION_MODE,
            query=payload,
        )
        return res

    async def get_position_mode(
        self,
    ):
        payload = {}
        res = await self._request(
            method="GET",
            path=SwapTrade.QUERY_POSITION_MODE,
            query=payload,
        )
        return res
