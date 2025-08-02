from ._http_manager import HTTPManager
from .endpoints.market import Market
from ...utils.common import Common
from ...utils.timeframe_utils import bybit_convert_timeframe


class MarketHTTP(HTTPManager):
    async def get_instruments_info(
        self,
        category: str = "linear",
        product_symbol: str = None,
        status: str = None,
        baseCoin: str = None,
        limit: int = None,
        cursor: str = None,
    ):
        """
        :param category: str (spot, linear, inverse, option)
        :param product_symbol: str
        :param status: str
        :param baseCoin: str
        :param limit: int
        :param cursor: str
        """
        payload = {
            "category": category,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if status is not None:
            payload["status"] = status
        if baseCoin is not None:
            payload["baseCoin"] = baseCoin
        if limit is not None:
            payload["limit"] = limit
        if cursor is not None:
            payload["cursor"] = cursor

        res = await self._request(
            method="GET",
            path=Market.GET_INSTRUMENTS_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_kline(
        self,
        product_symbol: str,
        interval: str,
        startTime: int = None,
        limit: int = None,
    ):
        """
        :param symbol: str
        :param interval: str
        :param category: str (spot, linear, inverse) async default is linear
        :param startTime: int
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "interval": bybit_convert_timeframe(interval),
        }
        if startTime is not None:
            payload["start"] = startTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Market.GET_KLINE,
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
        :param category: str (linear, inverse)
        :param symbol: str
        :param limit: int
        """
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
        }
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Market.GET_ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    async def get_tickers(
        self,
        category: str = "linear",
        product_symbol: str = None,
        baseCoin: str = None,
    ):
        """
        :param category: str (spot, linear, inverse, option)
        :param symbol: str
        :param baseCoin: str
        """
        payload = {
            "category": category,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if baseCoin is not None:
            payload["baseCoin"] = baseCoin

        res = await self._request(
            method="GET",
            path=Market.GET_TICKERS,
            query=payload,
            signed=False,
        )
        return res

    async def get_funding_rate_history(
        self,
        product_symbol: str,
        startTime: int = None,
        limit: int = None,
    ):
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
        }
        if startTime is not None:
            payload["startTime"] = startTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Market.GET_FUNDING_RATE_HISTORY,
            query=payload,
            signed=False,
        )
        return res

    async def get_public_trade_history(
        self,
        product_symbol: str,
        limit: int = None,
    ):
        """
        :param category: str (linear, spot)
        :param symbol: str
        :param limit: int
        """
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
        }
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Market.GET_PUBLIC_TRADE_HISTORY,
            query=payload,
            signed=False,
        )
        return res
