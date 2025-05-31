from ._http_manager import HTTPManager
from .endpoint.path import Path
from .endpoint.account import Account


class AccountHTTP(HTTPManager):
    async def clearinghouse_state(
        self,
        user: str,
        dex: str = None,
    ):
        """
        :param user: str (waller address)
        :param dex: str
        """
        payload = {
            "type": Account.CLEARINGHOUSESTATE,
            "user": user,
        }

        if dex is not None:
            payload["dex"] = dex

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def open_orders(
        self,
        user: str,
        dex: str = None,
    ):
        """
        :param user: str (waller address)
        :param dex: str
        """
        payload = {
            "type": Account.OPENORDERS,
            "user": user,
        }

        if dex is not None:
            payload["dex"] = dex

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def user_fills(
        self,
        user: str,
        aggregateByTime: bool = False,
    ):
        """
        :param user: str (waller address)
        :param aggregateByTime: bool
        """
        payload = {
            "type": Account.USERFILLS,
            "user": user,
        }

        if aggregateByTime:
            payload["aggregateByTime"] = True

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def user_rate_limit(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Account.USERRATELIMIT,
            "user": user,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def order_status(
        self,
        user: str,
        oid: str,
    ):
        """
        :param user: str (waller address)
        :param oid: str
        """
        payload = {
            "type": Account.ORDERSTATUS,
            "user": user,
            "oid": oid,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def historical_orders(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Account.HISTORICALORDERS,
            "user": user,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def subaccounts(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Account.SUBACCOUNTS,
            "user": user,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def user_role(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Account.USERROLE,
            "user": user,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    async def portfolio(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Account.PORTFOLIO,
            "user": user,
        }

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
