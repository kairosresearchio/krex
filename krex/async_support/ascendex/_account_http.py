from ._http_manager import HTTPManager
from .endpoints.account import CashAccount


class AccountHTTP(HTTPManager):
    async def get_account_info(self):
        """
        Get account information (uses static endpoint)
        """
        res = await self._request(
            method="GET",
            path=CashAccount.ACCOUNT_INFO,
            query=None,
        )
        return res
