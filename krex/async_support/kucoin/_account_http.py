from ._http_manager import HTTPManager
from .endpoints.account import SpotAccount


class AccountHTTP(HTTPManager):
    async def get_account_balance(
        self,
        currency: str = None,
        type: str = None,
    ):
        payload = {}
        if currency:
            payload["currency"] = currency
        if type:
            payload["type"] = type

        res = await self._request(
            method="GET",
            path=SpotAccount.ACCOUNT_BALANCE,
            query=payload,
        )
        return res
