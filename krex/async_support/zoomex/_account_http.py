from ._http_manager import HTTPManager
from .endpoints.account import Account
from ...utils.common import Common

class AccountHTTP(HTTPManager):
    async def get_wallet_balance(
        self,
        product_symbol: str = None
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "accountType": "CONTRACT",
        }
        if product_symbol is not None:
            payload["coin"] = self.ptm.get_exchange_symbol(Common.ZOOMEX, product_symbol)
        
        res = await self._request(
            method="GET",
            path=Account.GET_WALLET_BALANCE,
            query=payload,
            signed=True,
        )
        return res