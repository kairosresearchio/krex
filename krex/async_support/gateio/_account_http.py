from ._http_manager import HTTPManager
from .endpoints.account import DeliveryAccount, FutureAccount, SpotAccount


class AccountHTTP(HTTPManager):
    async def get_futures_account(
        self,
        ccy: str = "usdt",  # or "btc"
    ):
        """
        :param ccy: str
        """
        path_params = {
            "settle": ccy,
        }

        res = await self._request(
            method="GET",
            path=FutureAccount.QUERY_FUTURES_ACCOUNT,
            path_params=path_params,
        )
        return res

    async def get_futures_account_book(
        self,
        ccy: str = "usdt",  # or "btc"
        contract: str = None,
        limit: int = None,
        offset: int = None,
        from_time: int = None,
        to_time: int = None,
        change_type: str = None,
    ):
        """
        :param ccy: str
        :param contract: str
        :param limit: int
        :param offset: int
        :param from_time: int
        :param to_time: int
        :param change_type: str
        """
        path_params = {
            "settle": ccy,
        }

        payload = {}
        if contract:
            payload["contract"] = contract
        if limit:
            payload["limit"] = limit
        if offset:
            payload["offset"] = offset
        if from_time:
            payload["from"] = from_time
        if to_time:
            payload["to"] = to_time
        if change_type:
            payload["type"] = change_type

        res = await self._request(
            method="GET",
            path=FutureAccount.QUERY_ACCOUNT_BOOK,
            path_params=path_params,
            query=payload,
        )
        return res

    async def get_delivery_account(
        self,
        ccy: str = "usdt",
    ):
        """
        :param ccy: str
        """
        path_params = {
            "settle": ccy,
        }

        res = await self._request(
            method="GET",
            path=DeliveryAccount.QUERY_DELIVERY_ACCOUNT,
            path_params=path_params,
        )
        return res

    async def get_delivery_account_book(
        self,
        ccy: str = "usdt",
        limit: int = None,
        offset: int = None,
        from_time: int = None,
        to_time: int = None,
        change_type: str = None,
    ):
        """
        :param ccy: str
        :param limit: int
        :param offset: int
        :param from_time: int
        :param to_time: int
        :param change_type: str
        """
        path_params = {
            "settle": ccy,
        }

        payload = {}
        if limit:
            payload["limit"] = limit
        if offset:
            payload["offset"] = offset
        if from_time:
            payload["from"] = from_time
        if to_time:
            payload["to"] = to_time
        if change_type:
            payload["type"] = change_type

        res = await self._request(
            method="GET",
            path=DeliveryAccount.QUERY_ACCOUNT_BOOK,
            path_params=path_params,
            query=payload,
        )
        return res

    async def get_spot_account(
        self,
        ccy: str = None,
    ):
        """
        :param ccy: str
        """
        payload = {}
        if ccy:
            payload["currency"] = ccy

        res = await self._request(
            method="GET",
            path=SpotAccount.QUERY_SPOT_ACCOUNT,
            query=payload,
        )
        return res

    async def get_spot_account_book(
        self,
        ccy: str = None,
        from_timestamp: int = None,
        to_timestamp: int = None,
        page: int = None,
        limit: int = None,
        type_: str = None,
        code: str = None,
    ):
        """
        :param ccy: str
        :param from_ts: int
        :param to_ts: int
        :param page: int
        :param limit: int
        :param type_: str
        :param code: str
        """
        payload = {}
        if ccy:
            payload["currency"] = ccy
        if from_timestamp:
            payload["from"] = from_timestamp
        if to_timestamp:
            payload["to"] = to_timestamp
        if page:
            payload["page"] = page
        if limit:
            payload["limit"] = limit
        if code:
            payload["code"] = code
        elif type_:
            payload["type"] = type_

        res = await self._request(
            method="GET",
            path=SpotAccount.QUERY_ACCOUNT_BOOK,
            query=payload,
        )
        return res
