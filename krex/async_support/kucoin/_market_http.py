from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket


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
