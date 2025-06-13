from ._http_manager import HTTPManager
from .endpoints.path import Path
from .endpoints.market import Market
from ..utils.common import Common


class MarketHTTP(HTTPManager):
    def meta(
        self,
        dex: str = None,
    ):
        """
        :param dex: str
        """
        payload = {
            "type": Market.META,
        }

        if dex is not None:
            payload["dex"] = dex

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def spot_meta(
        self,
    ):
        payload = {
            "type": Market.SPOTMETA,
        }

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def meta_and_asset_ctxs(
        self,
    ):
        payload = {
            "type": Market.METAANDASSETCTXS,
        }

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def spot_meta_and_asset_ctxs(
        self,
    ):
        payload = {
            "type": Market.SPOTMETAANDASSETCTXS,
        }

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def l2book(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str (e.g. BTC-USDC-SWAP)
        """

        payload = {
            "type": Market.L2BOOK,
            "coin": self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol),
        }

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def candle_snapshot(
        self,
        product_symbol: str,
        interval: str,
        startTime: int,
        endTime: int = None,
    ):
        """
        :param product_symbol: str (e.g. BTC-USDC-SWAP)
        :param interval: str (e.g. 1m, 5m, 15m, 1h, 4h, 1d)
        :param startTime: int (timestamp in milliseconds)
        :param endTime: int (timestamp in milliseconds, optional)
        """
        payload = {
            "type": Market.CANDLESNAPSHOT,
            "req": {
                "coin": self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol),
                "interval": interval,
                "startTime": startTime,
            },
        }

        if endTime is not None:
            payload["req"]["endTime"] = endTime

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def funding_rate_history(
        self,
        product_symbol: str,
        startTime: int,
        endTime: int = None,
    ):
        """
        :param product_symbol: str (e.g. BTC-USDC-SWAP)
        :param startTime: int (timestamp in milliseconds)
        :param endTime: int (timestamp in milliseconds, optional)
        """
        payload = {
            "type": Market.FUNDINGHISTORY,
            "coin": self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol),
            "startTime": startTime,
        }

        if endTime is not None:
            payload["endTime"] = endTime

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
