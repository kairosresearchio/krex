from ._http_manager import HTTPManager
from .endpoints.spot_margin_trade import SpotMarginTrade


class SpotMarginTradeHTTP(HTTPManager):
    def spot_margin_trade_get_vip_margin_data(
        self,
        vipLevel: str = None,
        currency: str = None,
    ):
        """
        :param vipLevel: str
        :param currency: str
        """
        payload = {}
        if vipLevel is not None:
            payload["vipLevel"] = vipLevel
        if currency is not None:
            payload["currency"] = currency

        return self._request(
            method="GET",
            path=SpotMarginTrade.VIP_MARGIN_DATA,
            query=payload,
        )

    def get_collateral(
        self,
        currency: str = None,
    ):
        """
        :param currency: str
        """
        payload = {}
        if currency is not None:
            payload["currency"] = currency

        return self._request(
            method="GET",
            path=SpotMarginTrade.GET_COLLATERAL,
            query=payload,
        )

    def spot_margin_trade_get_historical_interest_rate(
        self,
        currency: str,
        vipLevel: str = None,
        startTime: int = None,
        endTime: int = None,
    ):
        """
        :param currency: str
        :param vipLevel: str
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "currency": currency,
        }
        if vipLevel is not None:
            payload["vipLevel"] = vipLevel
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime

        return self._request(
            method="GET",
            path=SpotMarginTrade.HISTORICAL_INTEREST,
            query=payload,
        )

    def spot_margin_trade_toggle_margin_trade(
        self,
        spotMarginMode: str,
    ):
        """
        :param spotMarginMode: str (1: open, 0: close)
        """
        payload = {
            "spotMarginMode": spotMarginMode,
        }

        return self._request(
            method="POST",
            path=SpotMarginTrade.TOGGLE_MARGIN_TRADE,
            query=payload,
        )

    def spot_margin_trade_set_leverage(self, leverage: str):
        """
        :param leverage: str (2-10)
        """
        payload = {
            "leverage": leverage,
        }

        return self._request(
            method="POST",
            path=SpotMarginTrade.SET_LEVERAGE,
            query=payload,
        )

    def spot_margin_trade_get_status_and_leverage(self):
        return self._request(
            method="GET",
            path=SpotMarginTrade.STATUS_AND_LEVERAGE,
            query=None,
        )
