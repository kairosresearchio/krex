from ._http_manager import HTTPManager
from .endpoints.path import Path
from .endpoints.account import Account


class AccountHTTP(HTTPManager):
    def clearinghouse_state(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def open_orders(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def user_fills(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def user_rate_limit(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def order_status(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def historical_orders(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def subaccounts(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def user_role(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res

    def portfolio(
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

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
