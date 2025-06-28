from krex.utils.timeframe_utils import kucoin_convert_timeframe
from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket
from ...utils.common import Common


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
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=SpotMarket.TICKER,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_all_tickers(
        self,
    ):
        payload = {}
        res = await self._request(
            method="GET",
            path=SpotMarket.ALL_TICKERS,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_orderbook(
        self,
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=SpotMarket.ORDERBOOK,
            query=payload,
        )
        return res

    async def get_spot_public_trades(
        self,
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=SpotMarket.PUBLIC_TRADES,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_kline(
        self,
        product_symbol: str,
        type_: str,
        startAt: int = None,
        endAt: int = None,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
            "type": kucoin_convert_timeframe(type_),
        }

        if startAt is not None:
            payload["startAt"] = startAt
        if endAt is not None:
            payload["endAt"] = endAt

        res = await self._request(
            method="GET",
            path=SpotMarket.KLINE,
            query=payload,
            signed=False,
        )
        return res
