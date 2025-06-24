from ._http_manager import HTTPManager
from .endpoints.market import SwapMarket
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_orderbook(
        self,
        product_symbol: str,
        limit: int = None,
    ):
        """
        Get orderbook for a specific symbol

        :param product_symbol: str - Trading pair symbol
        :param limit: int - Number of order book entries (default: 100, max: 1000)
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
        Get recent public trades for a specific symbol

        :param product_symbol: str - Trading pair symbol
        :param limit: int - Number of trades to return (default: 100, max: 1000)
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
        Get kline/candlestick data for a specific symbol

        :param product_symbol: str - Trading pair symbol
        :param interval: str - Kline interval (1m, 5m, 15m, 30m, 1h, 4h, 1d, 1w, 1M)
        :param start_time: int - Start time in milliseconds
        :param end_time: int - End time in milliseconds
        :param limit: int - Number of klines to return (default: 500, max: 1000)
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

    async def get_swap_instrument_info(
        self,
        product_symbol: str = None,
    ):
        """
        Get instrument information

        :param product_symbol: str - Trading pair symbol (optional, if not provided returns all)
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

    async def get_ticker(
        self,
        product_symbol: str = None,
    ):
        """
        Get ticker information

        :param product_symbol: str - Trading pair symbol (optional, if not provided returns all)
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
