from ._http_manager import HTTPManager
from .endpoint.asset import Asset


class AssetHTTP(HTTPManager):
    def get_currencies(self, **kwargs):
        return self._request("GET", Asset.CURRENCY_INFO, kwargs)

    def get_balances(self, **kwargs):
        return self._request("GET", Asset.GET_BALANCES, kwargs)

    def get_non_tradable_assets(self, **kwargs):
        return self._request("GET", Asset.NON_TRADABLE_ASSETS, kwargs)

    def get_asset_valuation(self, **kwargs):
        return self._request("GET", Asset.ASSET_VALUATION, kwargs)

    def funds_transfer(self, **kwargs):
        return self._request("POST", Asset.FUNDS_TRANSFER, kwargs)

    def transfer_state(self, **kwargs):
        return self._request("GET", Asset.TRANSFER_STATE, kwargs)

    def get_bills(self, **kwargs):
        return self._request("GET", Asset.BILLS_INFO, kwargs)

    def get_deposit_address(self, **kwargs):
        return self._request("GET", Asset.DEPOSIT_ADDRESS, kwargs)

    def get_deposit_history(self, **kwargs):
        return self._request("GET", Asset.DEPOSIT_HISTORY, kwargs)

    def withdrawal(self, **kwargs):
        return self._request("POST", Asset.WITHDRAWAL_COIN, kwargs)

    def cancel_withdrawal(self, **kwargs):
        return self._request("POST", Asset.CANCEL_WITHDRAWAL, kwargs)

    def get_withdrawal_history(self, **kwargs):
        return self._request("GET", Asset.WITHDRAWAL_HISTORY, kwargs)

    def get_deposit_withdraw_status(self, **kwargs):
        return self._request("GET", Asset.GET_DEPOSIT_WITHDRAW_STATUS, kwargs)

    def get_deposit_lightning(self, **kwargs):
        return self._request("GET", Asset.DEPOSIT_LIGHTNING, kwargs)

    def withdrawal_lightning(self, **kwargs):
        return self._request("POST", Asset.WITHDRAWAL_LIGHTNING, kwargs)
