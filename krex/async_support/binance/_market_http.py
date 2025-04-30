from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket, FuturesMarket
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_spot_exchange_info(
        self,
        product_symbol: str = None,
        product_symbols: list = None,
        symbolStatus: str = None,
    ):
        """
        :param product_symbol: str
        :param product_symbols: list
        :param symbolStatus: str (Filters symbols that have this tradingStatus. Valid values: TRADING, HALT, BREAK Cannot be used in combination with symbols or symbol.)
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE)
        if product_symbols is not None:
            formatted_symbols = [self.ptm.get_exchange_symbol(symbol, Common.BINANCE) for symbol in product_symbols]
            payload["symbols"] = str(formatted_symbols).replace("'", '"')
        if symbolStatus is not None:
            payload["symbolStatus"] = symbolStatus

        res = await self._request(
            method="GET",
            path=SpotMarket.EXCHANGE_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_futures_exchange_info(
        self,
    ):
        res = await self._request(
            method="GET",
            path=FuturesMarket.EXCHANGE_INFO,
            query=None,
            signed=False,
        )
        return res

    async def get_futures_ticker(
        self,
        product_symbol: str = None,
    ):
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE)

        res = await self._request(
            method="GET",
            path=FuturesMarket.BOOK_TICKER,
            query=payload,
            signed=False,
        )
        return res

    async def get_futures_kline(
        self,
        product_symbol: str,
        interval: str,
        startTime: int = None,
        endTime: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param interval: str
        :param startTime: int
        :param endTime: int
        :param limit: int (async default 500; max 1500.
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE),
            "interval": interval,
        }
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=FuturesMarket.KLINE,
            query=payload,
            signed=False,
        )
        return res

    async def get_futures_premium_index(
        self,
        product_symbol: str = None,
    ):
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE)

        res = await self._request(
            method="GET",
            path=FuturesMarket.PREMIUM_INDEX,
            query=payload,
            signed=False,
        )
        return res

    async def get_futures_funding_rate(
        self,
        product_symbol: str = None,
        startTime: int = None,
        endTime: int = None,
        limit: int = None,
    ):
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BINANCE)
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=FuturesMarket.FUNDING_RATE_HISTORY,
            query=payload,
            signed=False,
        )
        return res
