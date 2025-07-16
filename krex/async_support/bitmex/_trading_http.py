from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.trading import Trading


class TradingHTTP(HTTPManager):
    async def get_executions(
        self,
        product_symbol: str | None = None,
        filter: str | None = None,
        columns: str | None = None,
        count: int = 100,
        start: int = 0,
        reverse: bool = False,
        startTime: str | None = None,
        endTime: str | None = None,
        targetAccountId: int | None = None,
        targetAccountIds: str | None = None,
        targetAccountIds_array: list | None = None,
    ):
        """
        :param product_symbol: str
        :param filter: str
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        :param targetAccountId: int
        :param targetAccountIds: str
        :param targetAccountIds_array: list
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
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
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId
        if targetAccountIds is not None:
            payload["targetAccountIds"] = targetAccountIds
        if targetAccountIds_array is not None:
            payload["targetAccountIds[]"] = targetAccountIds_array

        res = await self._request(
            method="GET",
            path=Trading.GET_EXECUTIONS,
            query=payload,
        )
        return res

    async def get_trade_history(
        self,
        product_symbol: str | None = None,
        filter: str | None = None,
        columns: str | None = None,
        count: int = 100,
        start: int = 0,
        reverse: bool = False,
        startTime: str | None = None,
        endTime: str | None = None,
        targetAccountId: int | None = None,
        targetAccountIds: str | None = None,
        targetAccountIds_array: list | None = None,
    ):
        """
        :param product_symbol: str
        :param filter: str
        :param columns: str
        :param count: int
        :param start: int
        :param reverse: bool
        :param startTime: str
        :param endTime: str
        :param targetAccountId: int
        :param targetAccountIds: str
        :param targetAccountIds_array: list
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if product_symbol is not None:
            assert self.ptm is not None
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol)
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
        if targetAccountId is not None:
            payload["targetAccountId"] = targetAccountId
        if targetAccountIds is not None:
            payload["targetAccountIds"] = targetAccountIds
        if targetAccountIds_array is not None:
            payload["targetAccountIds[]"] = targetAccountIds_array

        res = await self._request(
            method="GET",
            path=Trading.GET_TRADE_HISTORY,
            query=payload,
        )
        return res

    async def get_trading_volume(
        self,
    ):
        payload: dict[str, str | int | list[str] | float | bool] = {}

        res = await self._request(
            method="GET",
            path=Trading.GET_TRADING_VOLUME,
            query=payload,
        )
        return res
