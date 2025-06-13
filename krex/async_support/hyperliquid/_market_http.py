from ._http_manager import HTTPManager
from .endpoint.path import Path
from .endpoint.market import Market
from ...utils.common import Common
import json


class MarketHTTP(HTTPManager):
    async def meta(
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

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def spot_meta(
        self,
    ):
        payload = {
            "type": Market.SPOTMETA,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def meta_and_asset_ctxs(
        self,
    ):
        payload = {
            "type": Market.METAANDASSETCTXS,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def spot_meta_and_asset_ctxs(
        self,
    ):
        payload = {
            "type": Market.SPOTMETAANDASSETCTXS,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def l2book(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str (e.g. BTC-USDC-SWAP)
        """
        payload = {
            "type": Market.L2BOOK,
            "coin": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[0],
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def candle_snapshot(
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
                "coin": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[0],
                "interval": interval,
                "startTime": startTime,
            },
        }

        if endTime is not None:
            payload["req"]["endTime"] = endTime

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def funding_rate_history(
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
            "coin": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[0],
            "startTime": startTime,
        }

        if endTime is not None:
            payload["endTime"] = endTime

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
