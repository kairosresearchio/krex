from ._http_manager import HTTPManager
from .endpoints.market import SwapMarket
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_swap_instrument_info(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)

        res = await self._request(
            method="GET",
            path=SwapMarket.INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_orderbook(
        self,
        product_symbol: str,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SwapMarket.ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    async def get_public_trades(
        self,
        product_symbol: str,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
        }
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SwapMarket.PUBLIC_TRADE,
            query=payload,
            signed=False,
        )
        return res

    async def get_kline(
        self,
        product_symbol: str,
        interval: str,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param interval: str
        :param start_time: int
        :param end_time: int
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BINGX, product_symbol),
            "interval": interval,
        }
        if start_time is not None:
            payload["startTime"] = start_time
        if end_time is not None:
            payload["endTime"] = end_time
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SwapMarket.KLINE,
            query=payload,
            signed=False,
        )
        return res

    async def get_ticker(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)

        res = await self._request(
            method="GET",
            path=SwapMarket.TICKER,
            query=payload,
            signed=False,
        )
        return res
