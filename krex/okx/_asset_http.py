from ._http_manager import HTTPManager
from .endpoints.asset import Asset


class AssetHTTP(HTTPManager):
    def get_currencies(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.CURRENCY_INFO,
            query=kwargs,
        )

    def get_balances(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_BALANCES,
            query=kwargs,
        )

    def get_non_tradable_assets(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.NON_TRADABLE_ASSETS,
            query=kwargs,
        )

    def get_asset_valuation(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.ASSET_VALUATION,
            query=kwargs,
        )

    def funds_transfer(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.FUNDS_TRANSFER,
            query=kwargs,
        )

    def transfer_state(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.TRANSFER_STATE,
            query=kwargs,
        )

    def get_bills(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.BILLS_INFO,
            query=kwargs,
        )

    def get_deposit_address(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.DEPOSIT_ADDRESS,
            query=kwargs,
        )

    def get_deposit_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.DEPOSIT_HISTORY,
            query=kwargs,
        )

    def withdrawal(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.WITHDRAWAL_COIN,
            query=kwargs,
        )

    def cancel_withdrawal(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.CANCEL_WITHDRAWAL,
            query=kwargs,
        )

    def get_withdrawal_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.WITHDRAWAL_HISTORY,
            query=kwargs,
        )

    def get_deposit_withdraw_status(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_DEPOSIT_WITHDRAW_STATUS,
            query=kwargs,
        )

    def get_exchange_list(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.EXCHANGE_LIST,
            query=kwargs,
        )

    def get_monthly_statement(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.MONTHLY_STATEMENT,
            query=kwargs,
        )

    def get_deposit_lightning(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.DEPOSIT_LIGHTNING,
            query=kwargs,
        )

    def withdrawal_lightning(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.WITHDRAWAL_LIGHTNING,
            query=kwargs,
        )
