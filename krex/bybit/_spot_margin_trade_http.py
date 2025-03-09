from ._http_manager import HTTPManager
from .endpoint.spot_margin_trade import SpotMarginTrade


class SpotMarginTradeHTTP(HTTPManager):
    def spot_margin_trade_get_vip_margin_data(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.VIP_MARGIN_DATA,
            query=kwargs,
        )

    def spot_margin_trade_toggle_margin_trade(self, **kwargs):
        return self._request(
            method="POST",
            path=SpotMarginTrade.TOGGLE_MARGIN_TRADE,
            query=kwargs,
        )

    def spot_margin_trade_set_leverage(self, **kwargs):
        return self._request(
            method="POST",
            path=SpotMarginTrade.SET_LEVERAGE,
            query=kwargs,
        )

    def spot_margin_trade_get_status_and_leverage(self):
        return self._request(
            method="GET",
            path=SpotMarginTrade.STATUS_AND_LEVERAGE,
        )

    def spot_margin_trade_get_historical_interest_rate(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.HISTORICAL_INTEREST,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_vip_margin_data(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_MARGIN_COIN_INFO,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_margin_coin_info(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_MARGIN_COIN_INFO,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_borrowable_coin_info(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_BORROWABLE_COIN_INFO,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_interest_quota(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_INTEREST_QUOTA,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_loan_account_info(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_LOAN_ACCOUNT_INFO,
            query=kwargs,
        )

    def spot_margin_trade_normal_borrow(self, **kwargs):
        return self._request(
            method="POST",
            path=SpotMarginTrade.NORMAL_BORROW,
            query=kwargs,
        )

    def spot_margin_trade_normal_repay(self, **kwargs):
        return self._request(
            method="POST",
            path=SpotMarginTrade.NORMAL_REPAY,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_borrow_order_detail(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_BORROW_ORDER_DETAIL,
            query=kwargs,
        )

    def spot_margin_trade_normal_get_repayment_order_detail(self, **kwargs):
        return self._request(
            method="GET",
            path=SpotMarginTrade.NORMAL_GET_REPAYMENT_ORDER_DETAIL,
            query=kwargs,
        )

    def spot_margin_trade_normal_toggle_margin_trade(self, **kwargs):
        return self._request(
            method="POST",
            path=SpotMarginTrade.NORMAL_TOGGLE_MARGIN_TRADE,
            query=kwargs,
        )
