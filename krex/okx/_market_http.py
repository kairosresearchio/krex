from ._http_manager import HTTPManager
from .endpoints.market import Market
from ..utils.common import Common


class MarketHTTP(HTTPManager):
    def get_candles_ticks(
        self,
        product_symbol: str,
        bar: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param product_symbol: str
        :param bar: str
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if bar is not None:
            payload["bar"] = bar
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Market.GET_KLINE,
            query=payload,
            signed=False,
        )
        return res

    def get_orderbook(
        self,
        product_symbol: str,
        sz: str = None,
    ):
        """
        :param product_symbol: str
        :param sz: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if sz is not None:
            payload["sz"] = sz

        res = self._request(
            method="GET",
            path=Market.GET_ORDERBOOK,
            query=payload,
            signed=False,
        )
        return res

    def get_tickers(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
    ):
        """
        :param instType: str (SPOT, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily

        res = self._request(
            method="GET",
            path=Market.GET_TICKERS,
            query=payload,
            signed=False,
        )
        return res
