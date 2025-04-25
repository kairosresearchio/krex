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
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT)
            payload["category"] = self.ptm.get_product_type(product_symbol, Common.BYBIT)
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
            "category": self.ptm.get_product_type(product_symbol, Common.BYBIT),
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT),
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
        mode: str,
        symbol: str = None,
        coin: str = None,
    ):
        """
        :param mode: str. 0: Merged Single. 3: Both Sides
        :param symbol: str
        :param coin: str
        """
        payload = {
            "category": "linear",
            "mode": mode,
        }
        if symbol is not None:
            payload["symbol"] = symbol
        if coin is not None:
            payload["coin"] = coin

        res = self._request(
            method="POST",
            path=Position.SWITCH_POSITION_MODE,
            query=payload,
        )
        return res

    def set_trading_stop( # currently no need to be tested
        self,
        category: str,
        symbol: str,
        tpslMode: str,
        # positionIdx: str,
        takeProfit: str = None,
        stopLoss: str = None,
        tpSize: str = None,
        slSize: str = None,
        tpLimitPrice: str = None,
        slLimitPrice: str = None,
        tpOrderType: str = None,
        slOrderType: str = None,
    ):
        """
        :param symbol: str
        :param tpslMode: str. `Full`: entire position TP/SL, `Partial`: partial position TP/SL
        :param takeProfit: str
        :param stopLoss: str
        :param tpSize: str
        :param slSize: str
        :param tpLimitPrice: str
        :param slLimitPrice: str
        :param tpOrderType: str
        :param slOrderType: str
        """
        payload = {
            "category": category,
            "symbol": symbol,
            "tpslMode": tpslMode,
            "positionIdx": 0,
        }
        if takeProfit is not None:
            payload["takeProfit"] = takeProfit
        if stopLoss is not None:
            payload["stopLoss"] = stopLoss
        if tpSize is not None:
            payload["tpSize"] = tpSize
        if slSize is not None:
            payload["slSize"] = slSize
        if tpLimitPrice is not None:
            payload["tpLimitPrice"] = tpLimitPrice
        if slLimitPrice is not None:
            payload["slLimitPrice"] = slLimitPrice
        if tpOrderType is not None:
            payload["tpOrderType"] = tpOrderType
        if slOrderType is not None:
            payload["slOrderType"] = slOrderType

        res = self._request(
            method="POST",
            path=Position.SET_TRADING_STOP,
            query=payload,
        )
        return res

    def set_auto_add_margin( # currently no need to be tested
        self,
        product_symbol: str,
        autoAddMargin: int,
        # positionIdx: int = None,
    ):
        """ "
        :param symbol: str
        :param autoAddMargin: int (0:closing, 1:opening)
        :param positionIdx: int (0: One-way position mode, 1: Buy-side two-way position mode, 2: Sell-side two-way position mode)
        """
        payload = {
            "category": "linear",
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT),
            "autoAddMargin": autoAddMargin,
            "positionIdx": 0,
        }

        res = self._request(
            method="POST",
            path=Position.SET_AUTO_ADD_MARGIN,
            query=payload,
        )
        return res

    def add_or_reduce_margin( # currently no need to be tested
        self,
        product_symbol: str,
        margin: str,
    ):
        """
        :param category: str
        :param symbol: str
        :param margin: str
        """
        payload = {
            "category": self.ptm.get_product_type(product_symbol, Common.BYBIT),
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT),
            "margin": margin,
        }

        res = self._request(
            method="POST",
            path=Position.ADD_MARGIN,
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
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT)
            payload["category"] = self.ptm.get_product_type(product_symbol, Common.BYBIT)
        if startTime is not None:
            payload["startTime"] = startTime

        res = self._request(
            method="GET",
            path=Position.GET_CLOSED_PNL,
            query=payload,
        )
        return res
