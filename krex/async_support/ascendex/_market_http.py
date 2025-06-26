from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket
from ...utils.timeframe_utils import bybit_convert_timeframe


class MarketHTTP(HTTPManager):
    async def get_spot_instrument_info(
        self,
    ):
        payload = {}
        res = await self._request(
            method="GET",
            path=SpotMarket.INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_ticker(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol)

        res = await self._request(
            method="GET",
            path=SpotMarket.TICKER,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_kline(
        self,
        product_symbol: str,
        interval: str,
        to_timestamp: int = None,
        from_timestamp: int = None,
        n: int = None,
    ):
        """
        :param product_symbol: str
        :param interval: str
        :param to_timestamp: int
        :param from_timestamp: int
        :param n: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
            "interval": bybit_convert_timeframe(interval),
        }
        if to_timestamp is not None:
            payload["to"] = to_timestamp
        if from_timestamp is not None:
            payload["from"] = from_timestamp
        if n is not None:
            payload["n"] = n

        res = await self._request(
            method="GET",
            path=SpotMarket.KLINE,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_orderbook(
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
            path=SpotMarket.ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_public_trade(
        self,
        product_symbol: str,
        n: int = None,
    ):
        """
        :param product_symbol: str
        :param n: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.ASCENDEX, product_symbol),
        }
        if n is not None:
            payload["n"] = n

        res = await self._request(
            method="GET",
            path=SpotMarket.PUBLIC_TRADE,
            query=payload,
            signed=False,
        )
        return res
