from ._http_manager import HTTPManager
from .endpoints.account import SwapAccount


class AccountHTTP(HTTPManager):
    async def get_listen_key(self):
        """
        Get listen key for WebSocket user data stream
        :return: str - listenKey for WebSocket connection
        """
        if not self.session:
            await self.async_init()
        url = self.base_url + SwapAccount.LISTEN_KEY
        headers = {"X-BX-APIKEY": self.api_key}
        response = await self.session.post(url, headers=headers)
        data = response.json()
        return data.get("listenKey")

    async def keep_alive_listen_key(self, listen_key: str):
        """
        Keep alive listen key to prevent expiration

        :param listen_key: str - The listen key to keep alive
        :return: dict - Response indicating success
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

    # async def delete_listen_key(self, listen_key: str):
    #     """
    #     Delete listen key to close WebSocket connection

    #     :param listen_key: str - The listen key to delete
    #     :return: dict - Response indicating success
    #     """
    #     payload = {
    #         "listenKey": listen_key,
    #     }

    #     res = await self._request(
    #         method="DELETE",
    #         path=SwapAccount.LISTEN_KEY,
    #         query=payload,
    #     )
    #     return res

    async def get_account_balance(self):
        """
        Get account balance

        :return: dict - Account balance information
        """
        res = await self._request(
            method="GET",
            path=SwapAccount.ACCOUNT_BALANCE,
            query={},
        )
        return res

    # async def get_open_positions(
    #     self,
    #     product_symbol: str = None,
    # ):
    #     """
    #     Get open positions

    #     :param product_symbol: str - Trading pair symbol (optional)
    #     :return: dict - Open positions information
    #     """
    #     payload = {}
    #     if product_symbol is not None:
    #         payload["symbol"] = product_symbol

    #     res = await self._request(
    #         method="GET",
    #         path=SwapAccount.OPEN_POSITIONS,
    #         query=payload,
    #     )
    #     return res

    async def get_fund_flow(
        self,
        product_symbol: str = None,
        income_type: str = None,
        start_time: int = None,
        end_time: int = None,
        limit: int = None,
    ):
        """
        Get fund flow/income history

        :param product_symbol: str - Trading pair symbol (optional)
        :param income_type: str - Income type filter (optional)
        :param start_time: int - Start time in milliseconds (optional)
        :param end_time: int - End time in milliseconds (optional)
        :param limit: int - Number of records to return (optional)
        :return: dict - Fund flow information
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
