import json
from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.market import Market


class MarketHTTP(HTTPManager):
    def get_instrument_info(
        self,
        product_symbol: str | None = None,
        filter: dict | None = None,
        count: int | None = None,
    ):
        """
        :param product_symbol: str
        :param filter: dict
        :param count: int
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}
        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
        if filter is not None:
            payload["filter"] = json.dumps(filter)
        if count is not None:
            payload["count"] = count

        res = self._request(
            method="GET",
            path=Market.INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    def get_orderbook(
        self,
        product_symbol: str,
        depth: int | None = None,
    ):
        """
        :param product_symbol: str
        :param depth: int
        """
        assert self.ptm is not None
        payload: dict[str, str | int | list[str] | float | bool] = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol),
        }
        if depth is not None:
            payload["depth"] = depth

        res = self._request(
            method="GET",
            path=Market.ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    def get_trades(
        self,
        product_symbol: str | None = None,
        filter: dict | None = None,
        columns: str | None = None,
        count: int | None = None,
        start: int | None = None,
        reverse: bool | None = None,
        startTime: str | None = None,
        endTime: str | None = None,
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
        payload: dict[str, str | int | list[str] | float | bool] = {}
        if product_symbol is not None:
            assert self.ptm is not None
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

        res = self._request(
            method="GET",
            path=Market.TRADE,
            query=payload,
            signed=False,
        )
        return res

    def get_ticker(
        self,
        binSize: str | None = None,
        partial: bool | None = None,
        symbol: str | None = None,
        filter: dict | None = None,
        columns: str | None = None,
        count: int | None = None,
        start: int | None = None,
        reverse: bool | None = None,
        startTime: str | None = None,
        endTime: str | None = None,
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
        payload: dict[str, str | int | list[str] | float | bool] = {}
        if binSize is not None:
            payload["binSize"] = binSize
        if partial is not None:
            payload["partial"] = partial
        if symbol is not None:
            assert self.ptm is not None
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

        res = self._request(
            method="GET",
            path=Market.TICKER,
            query=payload,
            signed=False,
        )
        return res

    def get_kline(
        self,
        binSize: str | None = None,
        partial: bool | None = None,
        symbol: str | None = None,
        filter: dict | None = None,
        columns: str | None = None,
        count: int | None = None,
        start: int | None = None,
        reverse: bool | None = None,
        startTime: str | None = None,
        endTime: str | None = None,
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
        payload: dict[str, str | int | list[str] | float | bool] = {}
        if binSize is not None:
            payload["binSize"] = binSize
        if partial is not None:
            payload["partial"] = partial
        if symbol is not None:
            assert self.ptm is not None
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

        res = self._request(
            method="GET",
            path=Market.KLINE,
            query=payload,
            signed=False,
        )
        return res

    def get_funding(
        self,
        product_symbol: str | None = None,
        filter: dict | None = None,
        columns: str | None = None,
        count: int | None = None,
        start: int | None = None,
        reverse: bool | None = None,
        startTime: str | None = None,
        endTime: str | None = None,
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
        payload: dict[str, str | int | list[str] | float | bool] = {}
        if product_symbol is not None:
            assert self.ptm is not None
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

        res = self._request(
            method="GET",
            path=Market.FUNDING,
            query=payload,
            signed=False,
        )
        return res
