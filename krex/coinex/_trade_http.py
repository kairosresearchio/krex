from ._http_manager import HTTPManager
from .endpoints.trade import Trade


class TradeHTTP(HTTPManager):
    def place_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=kwargs,
        )
