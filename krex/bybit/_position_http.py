from ._http_manager import HTTPManager
from .endpoints.position import Position


class PositionHTTP(HTTPManager):
    def get_positions(
        self,
        category: str,
        symbol: str = None,
        limit: int = 20,
    ):
        # todo: dont need category after product table manager is implemented
        """
        :param category: str (inear, inverse, option)
        :param symbol: str
        :param limit: str
        """
        payload = {
            "category": category,
            "limit": limit,
        }
        if symbol is not None:
            payload["symbol"] = symbol

        return self._request(
            method="GET",
            path=Position.GET_POSITIONS,
            query=payload,
        )

    def set_leverage(
        self,
        category: str,
        symbol: str,
        leverage: str,
    ):
        # todo: dont need category after product table manager is implemented
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param buyLeverage: str
        :param sellLeverage: str
        """
        payload = {
            "category": category,
            "symbol": symbol,
            "buyLeverage": leverage,
            "sellLeverage": leverage,
        }

        return self._request(
            method="POST",
            path=Position.SET_LEVERAGE,
            query=payload,
        )

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

        return self._request(
            method="POST",
            path=Position.SWITCH_POSITION_MODE,
            query=payload,
        )

    def set_trading_stop(
        self,
        category: str,
        symbol: str,
        tpslMode: str,
        positionIdx: str,
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
        # todo: dont need category after product table manager is implemented
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

        return self._request(
            method="POST",
            path=Position.SET_TRADING_STOP,
            query=payload,
        )

    def set_auto_add_margin(
        self,
        symbol: str,
        autoAddMargin: int,
        positionIdx: int = None,
    ):
        """ "
        :param symbol: str
        :param autoAddMargin: int (0:closing, 1:opening)
        :param positionIdx: int (0: One-way position mode, 1: Buy-side two-way position mode, 2: Sell-side two-way position mode)
        """
        payload = {
            "category": "linear",
            "symbol": symbol,
            "autoAddMargin": autoAddMargin,
            "positionIdx": 0,
        }
        if positionIdx is not None:
            payload["positionIdx"] = positionIdx

        return self._request(
            method="POST",
            path=Position.SET_AUTO_ADD_MARGIN,
            query=payload,
        )

    def add_or_reduce_margin(
        self,
        category: str,
        symbol: str,
        margin: str,
    ):
        # todo: dont need category after product table manager is implemented
        """
        :param category: str
        :param symbol: str
        :param margin: str
        :param positionIdx: int
        """
        payload = {
            "category": category,
            "symbol": symbol,
            "margin": margin,
        }

        return self._request(
            method="POST",
            path=Position.ADD_MARGIN,
            query=payload,
        )

    def get_closed_pnl(
        self,
        category: str,
        symbol: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        # todo: dont need category after product table manager is implemented
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
        if symbol is not None:
            payload["symbol"] = symbol
        if startTime is not None:
            payload["startTime"] = startTime

        return self._request(
            method="GET",
            path=Position.GET_CLOSED_PNL,
            query=payload,
        )
