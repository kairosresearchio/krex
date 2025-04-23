from ._http_manager import HTTPManager
from .endpoints.account import FundingAccount, FuturesAccount


class AccountHTTP(HTTPManager):
    def get_account_balance(
        self,
        currency: str = None,
        needUsdValuation: bool = False,
    ):
        """
        :param currency: str
        :param needUsdValuation: bool
        """
        payload = {
            "needUsdValuation": needUsdValuation,
        }
        if currency is not None:
            payload["currency"] = currency

        res = self._request(
            method="GET",
            path=FundingAccount.GET_ACCOUNT_BALANCE,
            query=payload,
        )
        return res

    def get_account_currencies(
        self,
        currencies: str = None,
    ):
        """
        :param currencies: str
        """
        payload = {}
        if currencies is not None:
            coinName = ",".join(currencies)
            payload = {
                "currencies": coinName,
            }

        res = self._request(
            method="GET",
            path=FundingAccount.GET_ACCOUNT_CURRENCIES,
            query=payload,
        )
        return res

    def get_spot_wallet(self):
        res = self._request(
            method="GET",
            path=FundingAccount.GET_SPOT_WALLET_BALANCE,
            query=None,
        )
        return res

    def get_deposit_address(
        self,
        currency: str,
    ):
        """
        :param currency: str
        """
        payload = {
            "currency": currency,
        }

        res = self._request(
            method="GET",
            path=FundingAccount.DEPOSIT_ADDRESS,
            query=payload,
        )
        return res

    def get_withdraw_charge(
        self,
        currency: str,
    ):
        """
        :param currency: str
        """
        payload = {
            "currency": currency,
        }

        res = self._request(
            method="GET",
            path=FundingAccount.WITHDRAW_QUOTA,
            query=payload,
        )
        return res

    def post_withdraw_apply(
        self,
        currency: str,
        amount: str,
    ):
        """
        :param currency: str
        :param amount: str
        """
        payload = {
            "currency": currency,
            "amount": amount,
        }

        res = self._request(
            method="POST",
            path=FundingAccount.WITHDRAW,
            query=payload,
        )
        return res

    def get_deposit_withdraw_history(
        self,
        operation_type: str = "withdraw",
        limit: int = 1000,
        currency: str = None,
        startTime: int = None,
        endTime: int = None,
    ):
        """
        :param limit: int
        :param currency: str
        :param operation_type: str (deposit, withdraw)
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "N": limit,
            "operation_type": operation_type,
        }
        if currency is not None:
            payload["currency"] = currency
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime

        res = self._request(
            method="GET",
            path=FundingAccount.GET_DEPOSIT_WITHDRAW_HISTORY,
            query=payload,
        )
        return res

    def get_deposit_withdraw_history_detail(
        self,
        id: str,
    ):
        """
        :param id: str (withdraw_id or deposit_id)
        """
        payload = {
            "id": id,
        }

        res = self._request(
            method="GET",
            path=FundingAccount.GET_DEPOSIT_WITHDRAW_HISTORY_DETAIL,
            query=payload,
        )
        return res

    def get_contract_assets(self):
        res = self._request(
            method="GET",
            path=FuturesAccount.GET_CONTRACT_ASSETS,
            query=None,
        )
        return res
