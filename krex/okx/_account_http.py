from ._http_manager import HTTPManager
from .endpoint.account import Account


class AccountHTTP(HTTPManager):
    def get_instruments(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_INSTRUMENTS,
            query=kwargs,
        )

    def get_account_balance(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.ACCOUNT_INFO,
            query=kwargs,
        )

    def get_positions(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.POSITION_INFO,
            query=kwargs,
        )

    def get_positions_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.POSITIONS_HISTORY,
            query=kwargs,
        )

    def get_position_risk(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.POSITION_RISK,
            query=kwargs,
        )

    def get_account_bills(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.BILLS_DETAIL,
            query=kwargs,
        )

    def get_account_bills_archive(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.BILLS_ARCHIVE,
            query=kwargs,
        )

    def get_account_bills_history_archive(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.BILLS_HISTORY_ARCHIVE,
            query=kwargs,
        )

    def get_account_config(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.ACCOUNT_CONFIG,
            query=kwargs,
        )

    def set_position_mode(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.POSITION_MODE,
            query=kwargs,
        )

    def set_leverage(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_LEVERAGE,
            query=kwargs,
        )

    def get_max_order_size(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.MAX_TRADE_SIZE,
            query=kwargs,
        )

    def get_max_avail_size(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.MAX_AVAIL_SIZE,
            query=kwargs,
        )

    def adjustment_margin(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.ADJUSTMENT_MARGIN,
            query=kwargs,
        )

    def get_leverage(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_LEVERAGE,
            query=kwargs,
        )

    def get_adjust_leverage(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_ADJUST_LEVERAGE,
            query=kwargs,
        )

    def get_max_loan(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.MAX_LOAN,
            query=kwargs,
        )

    def get_fee_rates(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.FEE_RATES,
            query=kwargs,
        )

    def get_interest_accrued(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.INTEREST_ACCRUED,
            query=kwargs,
        )

    def get_interest_rate(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.INTEREST_RATE,
            query=kwargs,
        )

    def set_greeks(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_GREEKS,
            query=kwargs,
        )

    def get_max_withdrawal(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.MAX_WITHDRAWAL,
            query=kwargs,
        )

    def get_account_position_risk(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.ACCOUNT_RISK,
            query=kwargs,
        )

    def get_quick_borrow_repay(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.QUICK_BORROW_REPAY,
            query=kwargs,
        )

    def get_quick_borrow_repay_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.QUICK_BORROW_REPAY_HISTORY,
            query=kwargs,
        )

    def get_interest_limits(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.INTEREST_LIMITS,
            query=kwargs,
        )

    def spot_manual_borrow_repay(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.MANUAL_REBORROW_REPAY,
            query=kwargs,
        )

    def set_auto_repay(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_AUTO_REPAY,
            query=kwargs,
        )

    def spot_borrow_repay_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_BORROW_REPAY_HISTORY,
            query=kwargs,
        )

    def position_builder(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.POSITION_BUILDER,
            query=kwargs,
        )

    def set_risk_offset_amt(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_RISK_OFFSET_AMT,
            query=kwargs,
        )

    def get_greeks(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GREEKS,
            query=kwargs,
        )

    def get_account_position_tiers(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_PM_LIMIT,
            query=kwargs,
        )

    def activate_option(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.ACTIVSTE_OPTION,
            query=kwargs,
        )

    def set_auto_loan(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_AUTO_LOAN,
            query=kwargs,
        )

    def preset_account_level_switch(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.PRESET_ACCOUNT_LEVEL_SWITCH,
            query=kwargs,
        )

    def precheck_account_level_switch(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.PRECHECK_ACCOUNT_LEVEL_SWITCH,
            query=kwargs,
        )

    def set_account_level(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_ACCOUNT_LEVEL,
            query=kwargs,
        )

    def account_mmp_reset(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.ACCOUNT_MMP_RESET,
            query=kwargs,
        )

    def account_mmp_config_get(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.ACCOUNT_MMP_CONFIG,
            query=kwargs,
        )

    def account_mmp_config_post(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.ACCOUNT_MMP_CONFIG,
            query=kwargs,
        )
