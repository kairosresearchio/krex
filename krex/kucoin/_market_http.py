from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket
from ..utils.common import Common

class MarketHTTP(HTTPManager):
    def get_spot_instrument_info(
        self,
    ):
        payload = {}
        res = self._request(
            method="GET",
            path=SpotMarket.INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    def get_spot_ticker(
        self,
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = self._request(
            method="GET",
            path=SpotMarket.TICKER,
            query=payload,
            signed=False,
        )
        return res

    def get_spot_all_tickers(
        self,
    ):
        payload = {}
        res = self._request(
            method="GET",
            path=SpotMarket.ALL_TICKERS,
            query=payload,
            signed=False,
        )
        return res

    def get_spot_orderbook(
        self,
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = self._request(
            method="GET",
            path=SpotMarket.ORDERBOOK,
            query=payload,
            signed=True,
        )
        return res

    def get_spot_public_trades(
        self,
        product_symbol: str,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
        }

        res = self._request(
            method="GET",
            path=SpotMarket.PUBLIC_TRADES,
            query=payload,
            signed=False,
        )
        return res

    def get_spot_kline(
        self,
        product_symbol: str,
        type: str,
        startAt: int = None,
        endAt: int = None,
    ):
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.KUCOIN, product_symbol),
            "type": type, # 1min, 5min, 15min, 30min, 1hour, 4hour, 1day
        }
        
        if startAt is not None:
            payload["startAt"] = startAt
        if endAt is not None:
            payload["endAt"] = endAt

        res = self._request(
            method="GET",
            path=SpotMarket.KLINE,
            query=payload,
            signed=False,
        )
        return res 