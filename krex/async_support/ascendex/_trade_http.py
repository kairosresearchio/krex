from krex.utils.common import Common
from krex.utils.helpers import generate_timestamp
from ._http_manager import HTTPManager
from .endpoints.order import SpotOrder


class TradeHTTP(HTTPManager):
    async def place_spot_order(
        self,
        product_symbol: str,
        orderQty: str,
        orderType: str,
        side: str,
        time: int = generate_timestamp(),
        id: str = None,
        orderPrice: str = None,
        stopPrice: str = None,
        postOnly: bool = None,
        timeInForce: str = None,
        respInst: str = None,
    ):
        """
        :param product_symbol: str
        :param orderQty: str
        :param orderType: str ("market", "limit", "stop_market", "stop_limit")
        :param side: str ("buy", "sell")
        :param time: int (milliseconds)
        :param id: str (>=9 chars, optional)
        :param orderPrice: str (optional)
        :param stopPrice: str (optional)
        :param postOnly: bool (optional)
        :param timeInForce: str ("GTC", "IOC", "FOK")
        :param respInst: str ("ACK", "ACCEPT", "DONE")
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
            "orderQty": orderQty,
            "orderType": orderType,
            "side": side,
            "time": time,
        }
        if id is not None:
            payload["id"] = id
        if orderPrice is not None:
            payload["orderPrice"] = orderPrice
        if stopPrice is not None:
            payload["stopPrice"] = stopPrice
        if postOnly is not None:
            payload["postOnly"] = postOnly
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if respInst is not None:
            payload["respInst"] = respInst

        res = await self._request(
            method="POST",
            path=SpotOrder.PLACE_ORDER.route,
            hash_path=SpotOrder.PLACE_ORDER.hash,
            query=payload,
        )
        return res

    async def place_spot_market_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_order(
            product_symbol=product_symbol,
            orderQty=orderQty,
            orderType="market",
            side=side,
            id=id,
            respInst=respInst,
        )

    async def place_spot_market_buy_order(
        self,
        product_symbol: str,
        orderQty: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_market_order(
            product_symbol=product_symbol,
            side="buy",
            orderQty=orderQty,
            id=id,
            respInst=respInst,
        )

    async def place_spot_market_sell_order(
        self,
        product_symbol: str,
        orderQty: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_market_order(
            product_symbol=product_symbol,
            side="sell",
            orderQty=orderQty,
            id=id,
            respInst=respInst,
        )

    async def place_spot_limit_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        timeInForce: str = "GTC",
        respInst: str = None,
    ):
        return await self.place_spot_order(
            product_symbol=product_symbol,
            orderQty=orderQty,
            orderType="limit",
            side=side,
            orderPrice=orderPrice,
            id=id,
            timeInForce=timeInForce,
            respInst=respInst,
        )

    async def place_spot_limit_buy_order(
        self,
        product_symbol: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        timeInForce: str = "GTC",
        respInst: str = None,
    ):
        return await self.place_spot_limit_order(
            product_symbol=product_symbol,
            side="buy",
            orderQty=orderQty,
            orderPrice=orderPrice,
            id=id,
            timeInForce=timeInForce,
            respInst=respInst,
        )

    async def place_spot_limit_sell_order(
        self,
        product_symbol: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        timeInForce: str = "GTC",
        respInst: str = None,
    ):
        return await self.place_spot_limit_order(
            product_symbol=product_symbol,
            side="sell",
            orderQty=orderQty,
            orderPrice=orderPrice,
            id=id,
            timeInForce=timeInForce,
            respInst=respInst,
        )

    async def place_spot_post_only_order(
        self,
        product_symbol: str,
        side: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_order(
            product_symbol=product_symbol,
            orderQty=orderQty,
            orderType="limit",
            side=side,
            orderPrice=orderPrice,
            postOnly=True,
            id=id,
            respInst=respInst,
        )

    async def place_spot_post_only_buy_order(
        self,
        product_symbol: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_post_only_order(
            product_symbol=product_symbol,
            side="buy",
            orderQty=orderQty,
            orderPrice=orderPrice,
            id=id,
            respInst=respInst,
        )

    async def place_spot_post_only_sell_order(
        self,
        product_symbol: str,
        orderQty: str,
        orderPrice: str,
        id: str = None,
        respInst: str = None,
    ):
        return await self.place_spot_post_only_order(
            product_symbol=product_symbol,
            side="sell",
            orderQty=orderQty,
            orderPrice=orderPrice,
            id=id,
            respInst=respInst,
        )

    async def cancel_spot_order(
        self,
        orderId: str,
        product_symbol: str,
        time: int = generate_timestamp(),
        id: str = None,
    ):
        """
        :param orderId: str
        :param product_symbol: str
        :param time: int
        :param id: str
        """
        payload = {
            "orderId": orderId,
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
            "time": time,
        }
        if id is not None:
            payload["id"] = id

        res = await self._request(
            method="DELETE",
            path=SpotOrder.CANCEL_ORDER.route,
            hash_path=SpotOrder.CANCEL_ORDER.hash,
            query=payload,
        )
        return res

    async def cancel_all_spot_orders(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
        }

        res = await self._request(
            method="DELETE",
            path=SpotOrder.CANCEL_ALL_ORDERS.route,
            hash_path=SpotOrder.CANCEL_ALL_ORDERS.hash,
            query=payload,
        )
        return res

    async def place_spot_batch_orders(
        self,
        orders: list,
    ):
        """
        :param orders: list
        """
        payload = {
            "orders": orders,
        }

        res = await self._request(
            method="POST",
            path=SpotOrder.PLACE_BATCH_ORDERS.route,
            hash_path=SpotOrder.PLACE_BATCH_ORDERS.hash,
            query=payload,
        )
        return res

    async def cancel_spot_batch_orders(
        self,
        orders: list,
    ):
        """
        :param orders: list
        """
        payload = {
            "orders": orders,
        }

        res = await self._request(
            method="DELETE",
            path=SpotOrder.CANCEL_BATCH_ORDERS.route,
            hash_path=SpotOrder.CANCEL_BATCH_ORDERS.hash,
            query=payload,
        )
        return res

    async def get_order_status(
        self,
        orderId: str = None,
    ):
        """
        :param orderId: str
        """
        payload = {}
        if orderId is not None:
            payload["orderId"] = orderId

        res = await self._request(
            method="GET",
            path=SpotOrder.QUERY_ORDER.route,
            hash_path=SpotOrder.QUERY_ORDER.hash,
            query=payload,
        )
        return res

    async def get_list_open_orders(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=SpotOrder.LIST_OPEN_ORDERS.route,
            hash_path=SpotOrder.LIST_OPEN_ORDERS.hash,
            query=payload,
        )
        return res

    async def get_list_order_history(
        self,
        product_symbol: str,
        account: str = "cash",
        start_time: int = None,
        end_time: int = None,
        seqNum: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param account: str (cash, margin, future)
        :param start_time: int
        :param end_time: int
        :param seqNum: int
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
            "account": account,
        }
        if start_time is not None:
            payload["startTime"] = start_time
        if end_time is not None:
            payload["endTime"] = end_time
        if seqNum is not None:
            payload["seqNum"] = seqNum
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SpotOrder.LIST_ORDER_HISTORY.route,
            hash_path=SpotOrder.LIST_ORDER_HISTORY.hash,
            query=payload,
        )
        return res
