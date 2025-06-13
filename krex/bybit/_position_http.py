from ._http_manager import HTTPManager
from .endpoints.position import Position
from ..utils.common import Common


class PositionHTTP(HTTPManager):
    def get_positions(
        self,
        category: str = "linear",
        product_symbol: str = None,
        settleCoin: str = None,
        limit: int = 20,
    ):
        """
        :param category: str (linear, inverse, option)
        :param symbol: str
        :param limit: str
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if settleCoin is not None:
            payload["settleCoin"] = settleCoin

        res = self._request(
            method="GET",
            path=Position.GET_POSITIONS,
            query=payload,
        )
        return res

    def set_leverage(
        self,
        product_symbol: str,
        leverage: str,
    ):
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param buyLeverage: str
        :param sellLeverage: str
        """
        payload = {
            "category": self.ptm.get_exchange_type(Common.BYBIT, product_symbol),
            "symbol": self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol),
            "buyLeverage": leverage,
            "sellLeverage": leverage,
        }

        res = self._request(
            method="POST",
            path=Position.SET_LEVERAGE,
            query=payload,
        )
        return res

    def switch_position_mode(
        self,
        mode: int,
        product_symbol: str = None,
        coin: str = None,
    ):
        """
        :param mode: int. 0: Merged Single. 3: Both Sides
        :param product_symbol: str
        :param coin: str
        """
        payload = {
            "category": "linear",
            "mode": mode,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
        if coin is not None:
            payload["coin"] = coin

        res = self._request(
            method="POST",
            path=Position.SWITCH_POSITION_MODE,
            query=payload,
        )
        return res

    def get_closed_pnl(
        self,
        category: str = "linear",
        product_symbol: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param category: str
        :param symbol: str
        :param margin: str
        :param positionIdx: int
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BYBIT, product_symbol)
            payload["category"] = self.ptm.get_exchange_type(Common.BYBIT, product_symbol)
        if startTime is not None:
            payload["startTime"] = startTime

        res = self._request(
            method="GET",
            path=Position.GET_CLOSED_PNL,
            query=payload,
        )
        return res
