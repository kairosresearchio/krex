from ._http_manager import HTTPManager
from .endpoint.account import Account


class AccountHTTP(HTTPManager):
    def get_wallet_balance(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_WALLET_BALANCE,
            query=kwargs,
        )

    def get_transferable_amount(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_TRANSFERABLE_AMOUNT,
            query=kwargs,
        )

    def upgrade_to_unified_trading_account(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.UPGRADE_TO_UNIFIED_ACCOUNT,
            query=kwargs,
        )

    def get_borrow_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_BORROW_HISTORY,
            query=kwargs,
        )

    def repay_liability(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.REPAY_LIABILITY,
            query=kwargs,
        )

    def get_collateral_info(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_COLLATERAL_INFO,
            query=kwargs,
        )

    def set_collateral_coin(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_COLLATERAL_COIN,
            query=kwargs,
        )

    def batch_set_collateral_coin(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.BATCH_SET_COLLATERAL_COIN,
            query=kwargs,
        )

    def get_coin_greeks(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_COIN_GREEKS,
            query=kwargs,
        )

    def get_fee_rates(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_FEE_RATE,
            query=kwargs,
        )

    def get_account_info(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_ACCOUNT_INFO,
            query=kwargs,
        )

    def get_transaction_log(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_TRANSACTION_LOG,
            query=kwargs,
        )

    def set_margin_mode(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_MARGIN_MODE,
            query=kwargs,
        )

    def set_mmp(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.SET_MMP,
            query=kwargs,
        )

    def reset_mmp(self, **kwargs):
        return self._request(
            method="POST",
            path=Account.RESET_MMP,
            query=kwargs,
        )

    def get_mmp_state(self, **kwargs):
        return self._request(
            method="GET",
            path=Account.GET_MMP_STATE,
            query=kwargs,
        )
