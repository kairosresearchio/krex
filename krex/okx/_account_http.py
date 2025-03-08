from ._http_manager import HTTPManager
from .endpoint.account import Account


class AccountHTTP(HTTPManager):
    def get_instruments(self, **kwargs):
        return self._request("GET", Account.GET_INSTRUMENTS, kwargs)

    def get_account_balance(self, **kwargs):
        return self._request("GET", Account.ACCOUNT_INFO, kwargs)

    def get_positions(self, **kwargs):
        return self._request("GET", Account.POSITION_INFO, kwargs)

    def get_positions_history(self, **kwargs):
        return self._request("GET", Account.POSITIONS_HISTORY, kwargs)

    def get_position_risk(self, **kwargs):
        return self._request("GET", Account.POSITION_RISK, kwargs)

    def get_account_bills(self, **kwargs):
        return self._request("GET", Account.BILLS_DETAIL, kwargs)

    def get_account_bills_archive(self, **kwargs):
        return self._request("GET", Account.BILLS_ARCHIVE, kwargs)

    def get_account_config(self, **kwargs):
        return self._request("GET", Account.ACCOUNT_CONFIG, kwargs)

    def set_position_mode(self, **kwargs):
        return self._request("POST", Account.POSITION_MODE, kwargs)

    def set_leverage(self, **kwargs):
        return self._request("POST", Account.SET_LEVERAGE, kwargs)

    def get_max_order_size(self, **kwargs):
        return self._request("GET", Account.MAX_TRADE_SIZE, kwargs)

    def get_max_avail_size(self, **kwargs):
        return self._request("GET", Account.MAX_AVAIL_SIZE, kwargs)

    def adjustment_margin(self, **kwargs):
        return self._request("POST", Account.ADJUSTMENT_MARGIN, kwargs)

    def get_leverage(self, **kwargs):
        return self._request("GET", Account.GET_LEVERAGE, kwargs)

    def get_max_loan(self, **kwargs):
        return self._request("GET", Account.MAX_LOAN, kwargs)

    def get_fee_rates(self, **kwargs):
        return self._request("GET", Account.FEE_RATES, kwargs)

    def get_interest_accrued(self, **kwargs):
        return self._request("GET", Account.INTEREST_ACCRUED, kwargs)

    def get_interest_rate(self, **kwargs):
        return self._request("GET", Account.INTEREST_RATE, kwargs)

    def set_greeks(self, **kwargs):
        return self._request("POST", Account.SET_GREEKS, kwargs)

    def set_isolated_mode(self, **kwargs):
        return self._request("POST", Account.ISOLATED_MODE, kwargs)

    def get_max_withdrawal(self, **kwargs):
        return self._request("GET", Account.MAX_WITHDRAWAL, kwargs)

    def get_account_position_risk(self, **kwargs):
        return self._request("GET", Account.ACCOUNT_RISK, kwargs)

    def get_interest_limits(self, **kwargs):
        return self._request("GET", Account.INTEREST_LIMITS, kwargs)

    def spot_manual_borrow_repay(self, **kwargs):
        return self._request("POST", Account.MANUAL_REBORROW_REPAY, kwargs)

    def set_auto_repay(self, **kwargs):
        return self._request("POST", Account.SET_AUTO_REPAY, kwargs)

    def spot_borrow_repay_history(self, **kwargs):
        return self._request("GET", Account.GET_BORROW_REPAY_HISTORY, kwargs)

    def position_builder(self, **kwargs):
        return self._request("POST", Account.POSITION_BUILDER, kwargs)

    def get_greeks(self, **kwargs):
        return self._request("GET", Account.GREEKS, kwargs)

    def get_account_position_tiers(self, **kwargs):
        return self._request("GET", Account.GET_PM_LIMIT, kwargs)

    def activate_option(self, **kwargs):
        return self._request("POST", Account.ACTIVSTE_OPTION, kwargs)

    def set_auto_loan(self, **kwargs):
        return self._request("POST", Account.SET_AUTO_LOAN, kwargs)

    def set_account_level(self, **kwargs):
        return self._request("POST", Account.SET_ACCOUNT_LEVEL, kwargs)

    def get_simulated_margin(self, **kwargs):
        return self._request("POST", Account.SIMULATED_MARGIN, kwargs)

    def borrow_repay(self, **kwargs):
        return self._request("POST", Account.BORROW_REPAY, kwargs)

    def borrow_repay_history(self, **kwargs):
        return self._request("GET", Account.BORROW_REPAY_HISTORY, kwargs)

    def get_vip_interest_accrued_data(self, **kwargs):
        return self._request("GET", Account.GET_VIP_INTEREST_ACCRUED_DATA, kwargs)

    def get_vip_interest_deducted_data(self, **kwargs):
        return self._request("GET", Account.GET_VIP_INTEREST_DEDUCTED_DATA, kwargs)

    def get_vip_loan_order_list(self, **kwargs):
        return self._request("GET", Account.GET_VIP_LOAN_ORDER_LIST, kwargs)

    def get_vip_loan_order_detail(self, **kwargs):
        return self._request("GET", Account.GET_VIP_LOAN_ORDER_DETAIL, kwargs)
