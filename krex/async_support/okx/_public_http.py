from ._http_manager import HTTPManager
from .endpoints.public import Public
from ...utils.common import Common


class PublicHTTP(HTTPManager):
    async def get_public_instruments(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
    ):
        """
        :param instType: str
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)

        res = await self._request(
            method="GET",
            path=Public.GET_INSTRUMENT_INFO,
            query=payload,
            signed=False,
        )
        return res

    async def get_funding_rate(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=Public.GET_FUNDING_RATE,
            query=payload,
            signed=False,
        )
        return res

    async def get_funding_rate_history(
        self,
        product_symbol: str,
        before: str = None,
        after: str = None,
        limit: str = None,
    ):
        """
        :param product_symbol: str
        :param before: str
        :param after: str
        :param limit: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Public.GET_FUNDING_RATE_HISTORY,
            query=payload,
            signed=False,
        )
        return res
