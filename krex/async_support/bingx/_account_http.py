from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.account import SwapAccount


class AccountHTTP(HTTPManager):
    async def get_account_balance(self):
        payload = {}
        res = await self._request(
            method="GET",
            path=SwapAccount.ACCOUNT_BALANCE,
            query=payload,
        )
        return res

    async def get_open_positions(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINGX, product_symbol)

        res = await self._request(
            method="GET",
            path=SwapAccount.OPEN_POSITIONS,
            query=payload,
        )
        return res

    async def get_fund_flow(
        self,
        product_symbol: str = None,
        income_type: str = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param income_type: str
        :param start_time: int
        :param end_time: int
        :param limit: int
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = product_symbol
        if income_type is not None:
            payload["incomeType"] = income_type
        if start_time is not None:
            payload["startTime"] = start_time
        if end_time is not None:
            payload["endTime"] = end_time
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SwapAccount.FUND_FLOW,
            query=payload,
        )
        return res

    async def get_listen_key(self):
        if not self.session:
            await self.async_init()
        url = self.base_url + SwapAccount.LISTEN_KEY
        headers = {"X-BX-APIKEY": self.api_key}

        res = await self.session.post(url, headers=headers)
        data = res.json()
        return data.get("listenKey")

    async def keep_alive_listen_key(self, listen_key: str):
        """
        :param listen_key: str
        """
        payload = {
            "listenKey": listen_key,
        }

        res = await self._request(
            method="PUT",
            path=SwapAccount.LISTEN_KEY,
            query=payload,
        )
        return res
