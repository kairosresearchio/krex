from ._http_manager import HTTPManager
from .endpoints.position import Position


class PositionHTTP(HTTPManager):
    def get_positions(self, **kwargs):
        return self._request(
            method="GET",
            path=Position.GET_POSITIONS,
            query=kwargs,
        )

    def set_leverage(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.SET_LEVERAGE,
            query=kwargs,
        )

    def set_tp_sl_mode(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.SET_TP_SL_MODE,
            query=kwargs,
        )

    def switch_position_mode(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.SWITCH_POSITION_MODE,
            query=kwargs,
        )

    def set_trading_stop(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.SET_TRADING_STOP,
            query=kwargs,
        )

    def set_auto_add_margin(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.SET_AUTO_ADD_MARGIN,
            query=kwargs,
        )

    def add_or_reduce_margin(self, **kwargs):
        return self._request(
            method="POST",
            path=Position.ADD_MARGIN,
            query=kwargs,
        )

    def get_executions(self, **kwargs):
        return self._request(
            method="GET",
            path=Position.GET_EXECUTIONS,
            query=kwargs,
        )

    def get_closed_pnl(self, **kwargs):
        return self._request(
            method="GET",
            path=Position.GET_CLOSED_PNL,
            query=kwargs,
        )
