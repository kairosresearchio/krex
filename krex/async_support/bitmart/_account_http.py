import pandas as pd
from ._http_manager import HTTPManager
from .endpoints.account import FundingAccount, FuturesAccount


class AccountHTTP(HTTPManager):
    def _to_dataframe(self, data):
        if isinstance(data, list):
            return pd.DataFrame(data)
        elif isinstance(data, dict):
            return pd.DataFrame([data])
        else:
            return pd.DataFrame()

    async def get_account_balance(
        self,
        currency: str = None,
        needUsdValuation: bool = False,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"].get("wallet", [])) if "data" in res else pd.DataFrame()

    async def get_account_currencies(
        self,
        currencies: str = None,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"].get("currencies", [])) if "data" in res else pd.DataFrame()

    async def get_spot_wallet(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=FundingAccount.GET_SPOT_WALLET_BALANCE,
            query=None,
        )
        return pd.DataFrame(res["data"]["wallet"]) if "data" in res else pd.DataFrame()

    async def get_deposit_address(
        self,
        currency: str,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pd.DataFrame()

    # todo: test failed
    async def get_withdraw_charge(
        self,
        currency: str,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pd.DataFrame()

    # todo: not tested
    async def post_withdraw_apply(
        self,
        currency: str,
        amount: str,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"]) if "data" in res else pd.DataFrame()

    async def get_deposit_withdraw_history(
        self,
        operation_type: str = "withdraw",
        limit: int = 1000,
        currency: str = None,
        startTime: int = None,
        endTime: int = None,
    ) -> pd.DataFrame:
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
        return self._to_dataframe(res["data"].get("records", [])) if "data" in res else pd.DataFrame()

    async def get_deposit_withdraw_history_detail(
        self,
        id: str,
    ) -> pd.DataFrame:
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
        return (
            self._to_dataframe(res["data"]["record"]) if "data" in res and "record" in res["data"] else pd.DataFrame()
        )

    async def get_contract_assets(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=FuturesAccount.GET_CONTRACT_ASSETS,
            query=None,
        )
        return self._to_dataframe(res["data"]) if "data" in res else pd.DataFrame()
