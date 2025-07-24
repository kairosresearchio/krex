from ._http_manager import HTTPManager
from .endpoints.market import Market
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_instruments_info(
        self,
        category: str = "linear",
        product_symbol: str = None,
        status: str = None,
        baseCoin: str = None,
        limit: int = None,
    ):
        """
        :param category: str (spot, linear, inverse, option)
        :param product_symbol: str
        :param status: str
        :param baseCoin: str
        :param limit: int
        """
        payload = {
            "category": category,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.ZOOMEX, product_symbol)
        if status is not None:
            payload["status"] = status
        if baseCoin is not None:
            payload["baseCoin"] = baseCoin
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Market.GET_INSTRUMENTS_INFO,
            query=payload,
            signed=False,
        )
        return res
