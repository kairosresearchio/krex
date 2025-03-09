from ._http_manager import HTTPManager
from .endpoints.asset import Asset


class AssetHTTP(HTTPManager):
    def get_coin_exchange_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_COIN_EXCHANGE_RECORDS,
            query=kwargs,
        )

    def get_spot_asset_info(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_SPOT_ASSET_INFO,
            query=kwargs,
        )

    def get_coins_balance(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_ALL_COINS_BALANCE,
            query=kwargs,
        )

    def get_coin_balance(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_SINGLE_COIN_BALANCE,
            query=kwargs,
        )

    def get_transferable_coin(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_TRANSFERABLE_COIN,
            query=kwargs,
        )

    def create_internal_transfer(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.CREATE_INTERNAL_TRANSFER,
            query=kwargs,
        )

    def get_internal_transfer_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_INTERNAL_TRANSFER_RECORDS,
            query=kwargs,
        )

    def get_sub_uid(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_SUB_UID,
            query=kwargs,
        )

    def create_universal_transfer(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.CREATE_UNIVERSAL_TRANSFER,
            query=kwargs,
        )

    def get_universal_transfer_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_UNIVERSAL_TRANSFER_RECORDS,
            query=kwargs,
        )

    def get_allowed_deposit_coin_info(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_ALLOWED_DEPOSIT_COIN_INFO,
            query=kwargs,
        )

    def set_deposit_account(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.SET_DEPOSIT_ACCOUNT,
            query=kwargs,
        )

    def get_deposit_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_DEPOSIT_RECORDS,
            query=kwargs,
        )

    def get_sub_deposit_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_SUB_ACCOUNT_DEPOSIT_RECORDS,
            query=kwargs,
        )

    def get_internal_deposit_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_INTERNAL_DEPOSIT_RECORDS,
            query=kwargs,
        )

    def get_master_deposit_address(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_MASTER_DEPOSIT_ADDRESS,
            query=kwargs,
        )

    def get_sub_deposit_address(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_SUB_DEPOSIT_ADDRESS,
            query=kwargs,
        )

    def get_coin_info(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_COIN_INFO,
            query=kwargs,
        )

    def get_withdrawal_records(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_WITHDRAWAL_RECORDS,
            query=kwargs,
        )

    def get_withdrawable_amount(self, **kwargs):
        return self._request(
            method="GET",
            path=Asset.GET_WITHDRAWABLE_AMOUNT,
            query=kwargs,
        )

    def withdraw(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.WITHDRAW,
            query=kwargs,
        )

    def cancel_withdrawal(self, **kwargs):
        return self._request(
            method="POST",
            path=Asset.CANCEL_WITHDRAWAL,
            query=kwargs,
        )
