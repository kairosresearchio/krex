from ._http_manager import HTTPManager
from .endpoints.account import CashAccount


class AccountHTTP(HTTPManager):
    async def get_account_info(self):
        payload = {}
        res = await self._request(
            method="GET",
            path=CashAccount.ACCOUNT_INFO,
            hash_path=CashAccount.ACCOUNT_INFO.hash,
            query=payload,
        )
        return res
