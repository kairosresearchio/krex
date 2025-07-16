from typing import Union
from ._http_manager import HTTPManager
from .endpoints.funds import Account


class AccountHTTP(HTTPManager):
    def get_wallet_summary(
        self,
        currency: str = "all",
        start_time: str | None = None,
        end_time: str | None = None,
        target_account_id: int | None = None,
        target_account_ids: Union[list, str] | None = None,
    ):
        """
        :param currency: str
        :param start_time: str
        :param end_time: str
        :param target_account_id: int
        :param target_account_ids: list[str] or str (can be "*")
        """
        payload: dict[str, str | int | list[str] | float | bool] = {
            "currency": currency,
        }

        if start_time is not None:
            payload["startTime"] = start_time

        if end_time is not None:
            payload["endTime"] = end_time

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        if target_account_ids is not None:
            if isinstance(target_account_ids, list):
                payload["targetAccountIds[]"] = target_account_ids
            elif isinstance(target_account_ids, str):
                payload["targetAccountIds"] = target_account_ids

        res = self._request(
            method="GET",
            path=Account.ACCOUNT_INFO,
            query=payload,
        )
        return res
