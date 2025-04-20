import polars as pl
from ._http_manager import HTTPManager
from .endpoints.account import FundingAccount, FuturesAccount
from ...utils.common_dataframe import to_dataframe


class AccountHTTP(HTTPManager):
    async def get_account_balance(
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

        res = await self._request(
            method="GET",
            path=FundingAccount.GET_ACCOUNT_BALANCE,
            query=payload,
        )
        return to_dataframe(res["data"].get("wallet", [])) if "data" in res else pl.DataFrame()

    async def get_account_currencies(
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

        res = await self._request(
            method="GET",
            path=FundingAccount.GET_ACCOUNT_CURRENCIES,
            query=payload,
        )
        return to_dataframe(res["data"].get("currencies", [])) if "data" in res else pl.DataFrame()

    async def get_spot_wallet(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=FundingAccount.GET_SPOT_WALLET_BALANCE,
            query=None,
        )
        return to_dataframe(res["data"].get("wallet", [])) if "data" in res else pl.DataFrame()

    async def get_deposit_address(
        self,
        currency: str,
    ) -> pl.DataFrame:
        """
        :param currency: str
        """
        payload = {
            "currency": currency,
        }

        res = await self._request(
            method="GET",
            path=FundingAccount.DEPOSIT_ADDRESS,
            query=payload,
        )
        return to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    # todo: test failed
    async def get_withdraw_charge(
        self,
        currency: str,
    ) -> pl.DataFrame:
        """
        :param currency: str
        """
        payload = {
            "currency": currency,
        }

        res = await self._request(
            method="GET",
            path=FundingAccount.WITHDRAW_QUOTA,
            query=payload,
        )
        return to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    # todo: not tested
    async def post_withdraw_apply(
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

        res = await self._request(
            method="POST",
            path=FundingAccount.WITHDRAW,
            query=payload,
        )
        return to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    async def get_deposit_withdraw_history(
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

        res = await self._request(
            method="GET",
            path=FundingAccount.GET_DEPOSIT_WITHDRAW_HISTORY,
            query=payload,
        )
        return to_dataframe(res["data"].get("records", [])) if "data" in res else pl.DataFrame()

    async def get_deposit_withdraw_history_detail(
        self,
        id: str,
    ) -> pl.DataFrame:
        """
        :param id: str (withdraw_id or deposit_id)
        """
        payload = {
            "id": id,
        }

        res = await self._request(
            method="GET",
            path=FundingAccount.GET_DEPOSIT_WITHDRAW_HISTORY_DETAIL,
            query=payload,
        )
        return to_dataframe(res["data"]["record"]) if "data" in res and "record" in res["data"] else pl.DataFrame()

    async def get_contract_assets(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=FuturesAccount.GET_CONTRACT_ASSETS,
            query=None,
        )
        return to_dataframe(res["data"]) if "data" in res else pl.DataFrame()
