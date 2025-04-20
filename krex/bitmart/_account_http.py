import polars as pl
from ._http_manager import HTTPManager
from .endpoints.account import FundingAccount, FuturesAccount


class AccountHTTP(HTTPManager):
    def _to_dataframe(self, data, schema: list[str] = None) -> pl.DataFrame:
        if not data:
            return pl.DataFrame()

        if isinstance(data, list):
            if schema:
                return pl.DataFrame(data, schema=schema, orient="row")
            elif all(isinstance(item, dict) for item in data):
                return pl.DataFrame(data)
            else:
                return pl.DataFrame(data, orient="row")

        if isinstance(data, dict):
            return pl.DataFrame([data])

        return pl.DataFrame()

    def get_account_balance(
        self,
        currency: str = None,
        needUsdValuation: bool = False,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"].get("wallet", [])) if "data" in res else pl.DataFrame()

    def get_account_currencies(
        self,
        currencies: str = None,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"].get("currencies", [])) if "data" in res else pl.DataFrame()

    def get_spot_wallet(self) -> pl.DataFrame:
        res = self._request(
            method="GET",
            path=FundingAccount.GET_SPOT_WALLET_BALANCE,
            query=None,
        )
        return pl.DataFrame(res["data"]["wallet"]) if "data" in res else pl.DataFrame()

    def get_deposit_address(
        self,
        currency: str,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    # todo: test failed
    def get_withdraw_charge(
        self,
        currency: str,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    # todo: not tested
    def post_withdraw_apply(
        self,
        currency: str,
        amount: str,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    def get_deposit_withdraw_history(
        self,
        operation_type: str = "withdraw",
        limit: int = 1000,
        currency: str = None,
        startTime: int = None,
        endTime: int = None,
    ) -> pl.DataFrame:
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
        return self._to_dataframe(res["data"].get("records", [])) if "data" in res else pl.DataFrame()

    def get_deposit_withdraw_history_detail(
        self,
        id: str,
    ) -> pl.DataFrame:
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
        return (
            self._to_dataframe(res["data"]["record"]) if "data" in res and "record" in res["data"] else pl.DataFrame()
        )

    def get_contract_assets(self) -> pl.DataFrame:
        res = self._request(
            method="GET",
            path=FuturesAccount.GET_CONTRACT_ASSETS,
            query=None,
        )
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()
