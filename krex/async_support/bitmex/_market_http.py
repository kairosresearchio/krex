import json
from ._http_manager import HTTPManager
from .endpoints.market import Market
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_instrument_info(
        self,
        product_symbol: str = None,
        filter: dict = None,
        count: int = None,
    ):
        """
        :param product_symbol: str
        :param filter: dict
        :param count: int
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if filter is not None:
            payload["filter"] = json.dumps(filter)
        if count is not None:
            payload["count"] = count

        res = await self._request(
            method="GET",
            path=Market.INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_orderbook(
        self,
        product_symbol: str,
        depth: int = None,
    ):
        """
        :param product_symbol: str
        :param depth: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol),
        }
        if depth is not None:
            payload["depth"] = depth

        res = await self._request(
            method="GET",
            path=Market.ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    async def get_trades(
        self,
        product_symbol: str = None,
        filter: dict = None,
        columns: str = None,
        count: int = None,
        start: int = None,
        reverse: bool = None,
        startTime: str = None,
        endTime: str = None,
    ):
        """
        :param product_symbol: str
        :param filter: dict
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if filter is not None:
            payload["filter"] = str(filter)
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

        res = await self._request(
            method="GET",
            path=Market.TRADE,
            query=payload,
            signed=False,
        )
        return res

    async def get_ticker(
        self,
        binSize: str = None,
        partial: bool = None,
        symbol: str = None,
        filter: dict = None,
        columns: str = None,
        count: int = None,
        start: int = None,
        reverse: bool = None,
        startTime: str = None,
        endTime: str = None,
    ):
        """
        :param binSize: str
        :param partial: bool
        :param symbol: str
        :param filter: dict
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        """
        payload = {}
        if binSize is not None:
            payload["binSize"] = binSize
        if partial is not None:
            payload["partial"] = partial
        if symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, symbol)
        if filter is not None:
            payload["filter"] = str(filter)
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

        res = await self._request(
            method="GET",
            path=Market.TICKER,
            query=payload,
            signed=False,
        )
        return res

    async def get_kline(
        self,
        binSize: str = None,
        partial: bool = None,
        symbol: str = None,
        filter: dict = None,
        columns: str = None,
        count: int = None,
        start: int = None,
        reverse: bool = None,
        startTime: str = None,
        endTime: str = None,
    ):
        """
        :param binSize: str
        :param partial: bool
        :param symbol: str
        :param filter: dict
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        """
        payload = {}
        if binSize is not None:
            payload["binSize"] = binSize
        if partial is not None:
            payload["partial"] = partial
        if symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, symbol)
        if filter is not None:
            payload["filter"] = str(filter)
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

        res = await self._request(
            method="GET",
            path=Market.KLINE,
            query=payload,
            signed=False,
        )
        return res

    async def get_funding(
        self,
        product_symbol: str = None,
        filter: dict = None,
        columns: str = None,
        count: int = None,
        start: int = None,
        reverse: bool = None,
        startTime: str = None,
        endTime: str = None,
    ):
        """
        :param product_symbol: str
        :param filter: dict
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if filter is not None:
            payload["filter"] = str(filter)
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

        res = await self._request(
            method="GET",
            path=Market.FUNDING,
            query=payload,
            signed=False,
        )
        return res

    async def get_stats(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)

        res = await self._request(
            method="GET",
            path=Market.STATS,
            query=payload,
            signed=False,
        )
        return res
