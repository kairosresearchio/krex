from ._http_manager import HTTPManager
from .endpoints.trade import SpotTrade
from ...utils.common import Common


class TradeHTTP(HTTPManager):
    async def place_order(
        self,
        product_symbol: str,
        side: str,
        type_: str,
        size: str = None,
        funds: str = None,
        price: str = None,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = None,
        cancelAfter: int = None,
        postOnly: bool = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol (e.g., "BTC-USDT-SPOT")
        :param side: str - "buy" or "sell"
        :param type_: str - "limit" or "market"
        :param size: str - Order size (required for limit orders, optional for market orders)
        :param funds: str - Order funds (for market orders, use either size or funds)
        :param price: str - Order price (required for limit orders)
        :param clientOid: str - Client order ID (recommended to use UUID)
        :param stp: str - Self trade prevention: "DC", "CO", "CN", "CB"
        :param tags: str - Order tag (max 20 ASCII characters)
        :param remark: str - Order remark (max 20 ASCII characters)
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param postOnly: bool - Passive order label (disabled for IOC/FOK)
        :param hidden: bool - Hidden order (not shown in order book)
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp (equal to KC-API-TIMESTAMP)
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
            "side": side,
            "type": type_,
        }

        if size is not None:
            payload["size"] = size
        if funds is not None:
            payload["funds"] = funds
        if price is not None:
            payload["price"] = price
        if clientOid is not None:
            payload["clientOid"] = clientOid
        if stp is not None:
            payload["stp"] = stp
        if tags is not None:
            payload["tags"] = tags
        if remark is not None:
            payload["remark"] = remark
        if timeInForce is not None:
            payload["timeInForce"] = timeInForce
        if cancelAfter is not None:
            payload["cancelAfter"] = cancelAfter
        if postOnly is not None:
            payload["postOnly"] = postOnly
        if hidden is not None:
            payload["hidden"] = hidden
        if iceberg is not None:
            payload["iceberg"] = iceberg
        if visibleSize is not None:
            payload["visibleSize"] = visibleSize
        if allowMaxTimeWindow is not None:
            payload["allowMaxTimeWindow"] = allowMaxTimeWindow
        if clientTimestamp is not None:
            payload["clientTimestamp"] = clientTimestamp

        res = await self._request(
            method="POST",
            path=SpotTrade.PLACE_ORDER,
            query=payload,
        )
        return res

    async def place_market_order(
        self,
        product_symbol: str,
        side: str,
        size: str = None,
        funds: str = None,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param side: str - "buy" or "sell"
        :param size: str - Order size (use either size or funds)
        :param funds: str - Order funds (use either size or funds)
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            type_="market",
            size=size,
            funds=funds,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_market_buy_order(
        self,
        product_symbol: str,
        size: str = None,
        funds: str = None,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size (use either size or funds)
        :param funds: str - Order funds (use either size or funds)
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="buy",
            size=size,
            funds=funds,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_market_sell_order(
        self,
        product_symbol: str,
        size: str = None,
        funds: str = None,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size (use either size or funds)
        :param funds: str - Order funds (use either size or funds)
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_market_order(
            product_symbol=product_symbol,
            side="sell",
            size=size,
            funds=funds,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_limit_order(
        self,
        product_symbol: str,
        side: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        postOnly: bool = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param side: str - "buy" or "sell"
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param postOnly: bool - Passive order label
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_order(
            product_symbol=product_symbol,
            side=side,
            type_="limit",
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            postOnly=postOnly,
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_limit_buy_order(
        self,
        product_symbol: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        postOnly: bool = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param postOnly: bool - Passive order label
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="buy",
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            postOnly=postOnly,
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_limit_sell_order(
        self,
        product_symbol: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        postOnly: bool = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param postOnly: bool - Passive order label
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side="sell",
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            postOnly=postOnly,
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_post_only_limit_order(
        self,
        product_symbol: str,
        side: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param side: str - "buy" or "sell"
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_limit_order(
            product_symbol=product_symbol,
            side=side,
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            postOnly=True,  # Set postOnly to True
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_post_only_limit_buy_order(
        self,
        product_symbol: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="buy",
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_post_only_limit_sell_order(
        self,
        product_symbol: str,
        size: str,
        price: str,
        clientOid: str = None,
        stp: str = None,
        tags: str = None,
        remark: str = None,
        timeInForce: str = "GTC",
        cancelAfter: int = None,
        hidden: bool = None,
        iceberg: bool = None,
        visibleSize: str = None,
        allowMaxTimeWindow: int = None,
        clientTimestamp: int = None,
    ):
        """
        :param product_symbol: str - Product symbol
        :param size: str - Order size
        :param price: str - Order price
        :param clientOid: str - Client order ID
        :param stp: str - Self trade prevention
        :param tags: str - Order tag
        :param remark: str - Order remark
        :param timeInForce: str - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
        :param cancelAfter: int - Cancel after n seconds (for GTT strategy)
        :param hidden: bool - Hidden order
        :param iceberg: bool - Iceberg order
        :param visibleSize: str - Maximum visible quantity in iceberg orders
        :param allowMaxTimeWindow: int - Order timeout in milliseconds
        :param clientTimestamp: int - Client timestamp
        """
        return await self.place_post_only_limit_order(
            product_symbol=product_symbol,
            side="sell",
            size=size,
            price=price,
            clientOid=clientOid,
            stp=stp,
            tags=tags,
            remark=remark,
            timeInForce=timeInForce,
            cancelAfter=cancelAfter,
            hidden=hidden,
            iceberg=iceberg,
            visibleSize=visibleSize,
            allowMaxTimeWindow=allowMaxTimeWindow,
            clientTimestamp=clientTimestamp,
        )

    async def place_batch_orders(
        self,
        orders: list,
    ):
        """
        :param orders: list - List of order dictionaries, each containing:
            - symbol: str (required) - Trading pair symbol
            - type: str (required) - "limit" or "market"
            - side: str (required) - "buy" or "sell"
            - size: str (required for limit, optional for market) - Order size
            - funds: str (optional for market) - Order funds (use either size or funds for market)
            - price: str (required for limit) - Order price
            - clientOid: str (optional) - Client order ID
            - stp: str (optional) - Self trade prevention: "CN", "CO", "CB", "DC"
            - tags: str (optional) - Order tag (max 20 ASCII characters)
            - remark: str (optional) - Order remark (max 20 ASCII characters)
            - timeInForce: str (optional) - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
            - cancelAfter: int (optional) - Cancel after n seconds (for GTT strategy)
            - postOnly: bool (optional) - Passive order label
            - hidden: bool (optional) - Hidden order
            - iceberg: bool (optional) - Iceberg order
            - visibleSize: str (optional) - Maximum visible quantity in iceberg orders

        Example:
            orders = [
                {
                    "symbol": "BTC-USDT",
                    "type": "limit",
                    "side": "buy",
                    "size": "0.001",
                    "price": "45000",
                    "clientOid": "uuid1"
                },
                {
                    "symbol": "ETH-USDT",
                    "type": "market",
                    "side": "sell",
                    "size": "0.01",
                    "clientOid": "uuid2"
                }
            ]
        """
        if not orders:
            raise ValueError("Orders list cannot be empty")

        if len(orders) > 20:
            raise ValueError("Maximum 20 orders can be placed simultaneously")

        processed_orders = []
        for order in orders:
            processed_order = order.copy()
            if "symbol" in processed_order:
                processed_order["symbol"] = self.ptm.get_exchange_symbol(Common.KUCOIN, processed_order["symbol"])
            processed_orders.append(processed_order)

        payload = {"orderList": processed_orders}

        res = await self._request(
            method="POST",
            path=SpotTrade.BATCH_ORDERS,
            query=payload,
        )
        return res

    async def place_batch_limit_orders(
        self,
        orders: list,
    ):
        """
        :param orders: list - List of limit order dictionaries, each containing:
            - symbol: str (required) - Trading pair symbol
            - side: str (required) - "buy" or "sell"
            - size: str (required) - Order size
            - price: str (required) - Order price
            - clientOid: str (optional) - Client order ID
            - stp: str (optional) - Self trade prevention
            - tags: str (optional) - Order tag
            - remark: str (optional) - Order remark
            - timeInForce: str (optional) - "GTC", "GTT", "IOC", "FOK" (default: "GTC")
            - cancelAfter: int (optional) - Cancel after n seconds (for GTT strategy)
            - postOnly: bool (optional) - Passive order label
            - hidden: bool (optional) - Hidden order
            - iceberg: bool (optional) - Iceberg order
            - visibleSize: str (optional) - Maximum visible quantity in iceberg orders
        """
        # Add type="limit" to all orders
        processed_orders = []
        for order in orders:
            processed_order = order.copy()
            processed_order["type"] = "limit"
            processed_orders.append(processed_order)

        return await self.place_batch_orders(processed_orders)

    async def place_batch_market_orders(
        self,
        orders: list,
    ):
        """
        :param orders: list - List of market order dictionaries, each containing:
            - symbol: str (required) - Trading pair symbol
            :param side: str (required) - "buy" or "sell"
            - size: str (optional) - Order size (use either size or funds)
            - funds: str (optional) - Order funds (use either size or funds)
            - clientOid: str (optional) - Client order ID
            - stp: str (optional) - Self trade prevention
            - tags: str (optional) - Order tag
            - remark: str (optional) - Order remark
        """
        # Add type="market" to all orders
        processed_orders = []
        for order in orders:
            processed_order = order.copy()
            processed_order["type"] = "market"
            processed_orders.append(processed_order)

        return await self.place_batch_orders(processed_orders)

    async def cancel_order(
        self,
        orderId: str,
        product_symbol: str,
    ):
        """
        :param orderId: str - The unique order ID generated by the trading system
        :param product_symbol: str - Product symbol (e.g., "BTC-USDT-SPOT")
        """
        # Format the path with orderId
        path = SpotTrade.CANCEL_ORDER.format(orderId=orderId)

        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = await self._request(
            method="DELETE",
            path=path,
            query=payload,
        )
        return res

    async def cancel_all_orders_by_symbol(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str - Product symbol
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }
        res = await self._request(
            method="DELETE",
            path=SpotTrade.CANCEL_ALL_ORDERS_BY_SYMBOL,
            query=payload,
        )
        return res

    async def cancel_all_orders(
        self,
    ):
        res = await self._request(
            method="DELETE",
            path=SpotTrade.CANCEL_ALL_ORDERS,
        )
        return res

    async def get_open_orders(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str - Optional product symbol filter
        """
        payload = {}
        if product_symbol:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol)

        res = await self._request(
            method="GET",
            path=SpotTrade.GET_OPEN_ORDERS,
            query=payload,
        )
        return res

    async def get_trade_history(
        self,
        product_symbol: str = None,
        orderId: str = None,
        startAt: int = None,
        endAt: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str - Optional product symbol filter
        :param orderId: str - Optional order ID filter
        :param startAt: int - Start time (milliseconds)
        :param endAt: int - End time (milliseconds)
        :param limit: int - Number of records to return
        """
        payload = {}
        if product_symbol:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol)
        if orderId:
            payload["orderId"] = orderId
        if startAt:
            payload["startAt"] = startAt
        if endAt:
            payload["endAt"] = endAt
        if limit:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SpotTrade.GET_TRADE_HISTORY,
            query=payload,
        )
        return res
