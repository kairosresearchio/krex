from typing import Union, List
from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.order import Order
import json


class TradeHTTP(HTTPManager):
    async def place_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: int | None = None,
        ordType: str = "Limit",
        price: float | None = None,
        stopPx: float | None = None,
        clOrdID: str | None = None,
        clOrdLinkID: str | None = None,
        contingencyType: str | None = None,
        displayQty: int | None = None,
        execInst: str | None = None,
        pegOffsetValue: float | None = None,
        pegPriceType: str | None = None,
        timeInForce: str | None = None,
        text: str | None = None,
        targetAccountId: int | None = None,
    ):
        """
        :param product_symbol: str - Trading symbol (required)
        :param side: str - Order side ("Buy", "Sell")
        :param orderQty: int - Order quantity (in contracts)
        :param ordType: str - Order type:
            - "Limit": Limit order (default)
            - "Market": Market order
            - "Stop": Stop market order
            - "StopLimit": Stop limit order
            - "MarketIfTouched": Market if touched order
            - "LimitIfTouched": Limit if touched order
            - "Pegged": Pegged order
            - "Block": Iceberg order
            - "MarketWithLeftOverAsLimit": Market with leftover as limit
        :param price: float - Limit price (for Limit, StopLimit, LimitIfTouched orders)
        :param stopPx: float - Trigger price (for Stop, StopLimit, MarketIfTouched, LimitIfTouched orders)
        :param clOrdID: str - Client order ID (max 36 characters)
        :param clOrdLinkID: str - Client order link ID (for order relationships)
        :param contingencyType: str - Contingency order type:
            - "OneCancelsTheOther": OCO order
            - "OneTriggersTheOther": OTO order
        :param displayQty: int - Display quantity (0 for fully hidden)
        :param execInst: str - Execution instructions:
            - "ParticipateDoNotInitiate": Post-only
            - "AllOrNone": Fill or kill
            - "MarkPrice": Use mark price
            - "IndexPrice": Use index price
            - "LastPrice": Use last price
            - "Close": Close position
            - "ReduceOnly": Reduce only
            - "Fixed": Fixed price (for pegged orders)
            - "LastWithinMark": Last price within mark price
        :param pegOffsetValue: float - Peg offset value
        :param pegPriceType: str - Peg price type:
            - "MarketPeg": Relative to far touch price
            - "PrimaryPeg": Relative to near touch price
            - "TrailingStopPeg": Trailing stop peg
            - "MidPricePeg": Mid price peg
            - "LastPeg": Last price peg
        :param timeInForce: str - Time in force:
            - "Day": Day only
            - "GoodTillCancel": Good till cancelled (default)
            - "ImmediateOrCancel": Immediate or cancel
            - "FillOrKill": Fill or kill
            - "AtTheClose": At the close
        :param text: str - Order annotation
        :param targetAccountId: int - Target account ID
        """
        assert self.ptm is not None
        payload: dict[str, str | int | list[str] | float | bool] = {}

        payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        payload["side"] = side
        payload["ordType"] = ordType

        if orderQty is not None:
            payload["orderQty"] = orderQty
        if price is not None:
            payload["price"] = price
        if stopPx is not None:
            payload["stopPx"] = stopPx
        if clOrdID is not None:
            payload["clOrdID"] = clOrdID
        if clOrdLinkID is not None:
            payload["clOrdLinkID"] = clOrdLinkID
        if contingencyType is not None:
            payload["contingencyType"] = contingencyType
        if displayQty is not None:
            payload["displayQty"] = displayQty
        if execInst is not None:
            payload["execInst"] = execInst
        if pegOffsetValue is not None:
            payload["pegOffsetValue"] = pegOffsetValue
        if pegPriceType is not None:
            payload["pegPriceType"] = pegPriceType
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if text is not None:
            payload["text"] = text
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId

        res = await self._request(
            method="POST",
            path=Order.PLACE_ORDER,
            query=payload,
        )
        return res

    async def place_market_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: int,
        clOrdID: str | None = None,
    ):
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderQty=orderQty,
            ordType="Market",
            clOrdID=clOrdID,
        )

    async def place_market_buy_order(
        self,
        product_symbol: str,
        orderQty: int,
        clOrdID: str | None = None,
    ):
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="Buy",
            orderQty=orderQty,
            clOrdID=clOrdID,
        )

    async def place_market_sell_order(
        self,
        product_symbol: str,
        orderQty: int,
        clOrdID: str | None = None,
    ):
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="Sell",
            orderQty=orderQty,
            clOrdID=clOrdID,
        )

    async def place_limit_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
        timeInForce: str = "GoodTillCancel",
    ):
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderQty=orderQty,
            ordType="Limit",
            price=price,
            clOrdID=clOrdID,
            timeInForce=timeInForce,
        )

    async def place_limit_buy_order(
        self,
        product_symbol: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
    ):
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="Buy",
            orderQty=orderQty,
            price=price,
            clOrdID=clOrdID,
        )

    async def place_limit_sell_order(
        self,
        product_symbol: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
    ):
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="Sell",
            orderQty=orderQty,
            price=price,
            clOrdID=clOrdID,
        )

    async def place_post_only_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
        execInst: str = "ParticipateDoNotInitiate",
    ):
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            orderQty=orderQty,
            ordType="Limit",
            price=price,
            clOrdID=clOrdID,
            execInst=execInst,
        )

    async def place_post_only_buy_order(
        self,
        product_symbol: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
    ):
        return await self.place_post_only_order(
            product_symbol=product_symbol,
            side="Buy",
            orderQty=orderQty,
            price=price,
            clOrdID=clOrdID,
        )

    async def place_post_only_sell_order(
        self,
        product_symbol: str,
        orderQty: int,
        price: float,
        clOrdID: str | None = None,
    ):
        return await self.place_post_only_order(
            product_symbol=product_symbol,
            side="Sell",
            orderQty=orderQty,
            price=price,
            clOrdID=clOrdID,
        )

    async def amend_order(
        self,
        orderID: str | None = None,
        origClOrdID: str | None = None,
        product_symbol: str | None = None,
        clOrdID: str | None = None,
        leavesQty: int | None = None,
        orderQty: int | None = None,
        price: float | None = None,
        stopPx: float | None = None,
        pegOffsetValue: float | None = None,
        text: str | None = None,
        targetAccountId: int | None = None,
    ):
        """
        :param orderID: str - Order ID to amend (required if origClOrdID not provided)
        :param origClOrdID: str - Client Order ID to amend (required if orderID not provided)
        :param product_symbol: str - Instrument symbol e.g. 'XBTUSD'
        :param clOrdID: str - Optional new Client Order ID, requires origClOrdID
        :param leavesQty: int - Optional leaves quantity in units of the instrument. Useful for amending partially filled orders
        :param orderQty: int - Optional order quantity in units of the instrument
        :param price: float - Optional limit price for 'Limit', 'StopLimit', and 'LimitIfTouched' orders
        :param stopPx: float - Optional trigger price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders
        :param pegOffsetValue: float - Optional trailing offset from the current price for 'Stop', 'StopLimit', 'MarketIfTouched', and 'LimitIfTouched' orders
        :param text: str - Optional order annotation. e.g. 'Take profit'
        :param targetAccountId: int - Target account ID
        """
        if orderID is None and origClOrdID is None:
            raise ValueError("Either orderID or origClOrdID must be provided")

        payload: dict[str, str | int | list[str] | float | bool] = {}

        if orderID is not None:
            payload["orderID"] = orderID
        if origClOrdID is not None:
            payload["origClOrdID"] = origClOrdID
        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if clOrdID is not None:
            payload["clOrdID"] = clOrdID
        if leavesQty is not None:
            payload["leavesQty"] = leavesQty
        if orderQty is not None:
            payload["orderQty"] = orderQty
        if price is not None:
            payload["price"] = price
        if stopPx is not None:
            payload["stopPx"] = stopPx
        if pegOffsetValue is not None:
            payload["pegOffsetValue"] = pegOffsetValue
        if text is not None:
            payload["text"] = text
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId

        res = await self._request(
            method="PUT",
            path=Order.AMEND_ORDER,
            query=payload,
        )
        return res

    async def cancel_order(
        self,
        orderID: Union[str, List[str]] | None = None,
        clOrdID: Union[str, List[str]] | None = None,
        targetAccountId: int | None = None,
        text: str | None = None,
    ):
        """
        :param orderID: Union[str, List[str]] - Order ID(s) to cancel
        :param clOrdID: Union[str, List[str]] - Client Order ID(s) to cancel
        :param targetAccountId: int - Account ID on which to cancel these orders
        :param text: str - Optional order annotation. e.g. 'Take profit'
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if orderID is not None:
            payload["orderID"] = orderID
        if clOrdID is not None:
            payload["clOrdID"] = clOrdID
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId
        if text is not None:
            payload["text"] = text

        res = await self._request(
            method="DELETE",
            path=Order.CANCEL_ORDER,
            query=payload,
        )
        return res

    async def cancel_all_orders(
        self,
        product_symbol: str | None = None,
        filter: dict | None = None,
        targetAccountId: int | None = None,
        targetAccountIds: list | None = None,
        text: str | None = None,
    ):
        """
        :param product_symbol: str
        :param filter: dict (Optional filter for cancellation. Use to only cancel some orders, e.g. {"side": "Buy"}.)
        :param targetAccountId: int
        :param targetAccountIds: list
        :param text: str (Optional cancellation annotation. e.g. 'Spread Exceeded')
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if filter is not None:
            payload["filter"] = json.dumps(filter)
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId
        if targetAccountIds is not None:
            payload["targetAccountIds"] = targetAccountIds
        if text is not None:
            payload["text"] = text

        res = await self._request(
            method="DELETE",
            path=Order.CANCEL_ALL_ORDERS,
            query=payload,
        )
        return res

    async def get_order(
        self,
        product_symbol: str | None = None,
        targetAccountId: int | None = None,
        filter: str | None = None,
        columns: str | None = None,
        count: int | None = 100,
        start: int | None = 0,
        reverse: bool | None = False,
        startTime: str | None = None,
        endTime: str | None = None,
        targetAccountIds: str | None = None,
        targetAccountIds_array: list | None = None,
    ):
        """
        :param product_symbol: str
        :param targetAccountId: int
        :param filter: str
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        :param targetAccountIds: str
        :param targetAccountIds_array: list
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId
        if filter is not None:
            payload["filter"] = filter
        if columns is not None:
            payload["columns"] = columns
        if count is not None:
            payload["count"] = count
        if start is not None:
            payload["start"] = start
        if reverse is not None:
            payload["reverse"] = reverse
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if targetAccountIds is not None:
            payload["targetAccountIds"] = targetAccountIds
        if targetAccountIds_array is not None:
            payload["targetAccountIds[]"] = targetAccountIds_array

        res = await self._request(
            method="GET",
            path=Order.QUERY_ORDER,
            query=payload,
        )
        return res
