import uuid
import time
from ._http_manager import HTTPManager
from .endpoints.asset import Asset


class AssetHTTP(HTTPManager):
    async def get_coin_info(
        self,
        coin: str = None,
    ):
        """
        :param coin: str
        """
        payload = {}
        if coin is not None:
            payload["coin"] = coin

        res = await self._request(
            method="GET",
            path=Asset.GET_COIN_INFO,
            query=payload,
        )
        return res

    async def get_sub_uid(self):
        res = await self._request(
            method="GET",
            path=Asset.GET_SUB_UID,
            query=None,
        )
        return res

    async def get_spot_asset_info(
        self,
        # accountType: str,
        coin: str = None,
    ):
        """
        async default accountType: SPOT
        :param coin: str
        """
        payload = {
            "accountType": "SPOT",
        }
        if coin is not None:
            payload["coin"] = coin

        res = await self._request(
            method="GET",
            path=Asset.GET_SPOT_ASSET_INFO,
            query=payload,
        )
        return res

    async def get_coins_balance(
        self,
        accountType: str,
        coin: str = None,
        memberId: str = None,
    ):
        """
        :param accountType: str
        :param coin: str
        :param memberId: str
        """
        payload = {
            "accountType": accountType,
        }
        if coin is not None:
            payload["coin"] = coin
        if memberId is not None:
            payload["memberId"] = memberId

        res = await self._request(
            method="GET",
            path=Asset.GET_ALL_COINS_BALANCE,
            query=payload,
        )
        return res

    async def get_coin_balance(
        self,
        accountType: str,
        coin: str,
        memberId: str = None,
        toAccountType: str = None,
    ):
        """
        :param accountType: str
        :param coin: str
        :param memberId: str
        :param toAccountType: str
        """
        payload = {
            "accountType": accountType,
            "coin": coin,
        }
        if memberId is not None:
            payload["memberId"] = memberId
        if toAccountType is not None:
            payload["toAccountType"] = toAccountType

        res = await self._request(
            method="GET",
            path=Asset.GET_SINGLE_COIN_BALANCE,
            query=payload,
        )
        return res

    async def get_withdrawable_amount(
        self,
        coin: str,
    ):
        """
        :param coin: str
        """
        payload = {
            "coin": coin,
        }

        res = await self._request(
            method="GET",
            path=Asset.GET_WITHDRAWABLE_AMOUNT,
            query=payload,
        )
        return res

    async def get_internal_transfer_records(
        self,
        coin: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param coin: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_INTERNAL_TRANSFER_RECORDS,
            query=payload,
        )
        return res

    async def get_transferable_coin(
        self,
        fromAccountType: str,
        toAccountType: str,
    ):
        """ "
        :param fromAccountType: str
        :param toAccountType: str
        """
        payload = {
            "fromAccountType": fromAccountType,
            "toAccountType": toAccountType,
        }

        res = await self._request(
            method="GET",
            path=Asset.GET_TRANSFERABLE_COIN,
            query=payload,
        )
        return res

    async def create_internal_transfer(
        self,
        coin: str,
        amount: str,
        fromAccountType: str,
        toAccountType: str,
    ):
        """
        :param coin: str
        :param amount: str
        :param fromAccountType: str
        :param toAccountType: str
        """
        transfer_id = str(uuid.uuid4())
        payload = {
            "transferId": transfer_id,
            "coin": coin,
            "amount": amount,
            "fromAccountType": fromAccountType,
            "toAccountType": toAccountType,
        }

        res = await self._request(
            method="POST",
            path=Asset.CREATE_INTERNAL_TRANSFER,
            query=payload,
        )
        return res

    async def create_universal_transfer(
        self,
        coin: str,
        amount: str,
        fromMemberId: int,
        toMemberId: int,
        fromAccountType: str,
        toAccountType: str,
    ):
        """
        :coin: str
        :amount: str
        :fromMemberId: int
        :toMemberId: int
        :fromAccountType: str
        :toAccountType: str
        """
        transfer_id = str(uuid.uuid4())
        payload = {
            "transferId": transfer_id,
            "coin": coin,
            "amount": amount,
            "fromMemberId": fromMemberId,
            "toMemberId": toMemberId,
            "fromAccountType": fromAccountType,
            "toAccountType": toAccountType,
        }

        res = await self._request(
            method="POST",
            path=Asset.CREATE_UNIVERSAL_TRANSFER,
            query=payload,
        )
        return res

    async def get_universal_transfer_records(
        self,
        coin: str = None,
        status: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param coin: str
        :param status: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if status is not None:
            payload["status"] = status
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_UNIVERSAL_TRANSFER_RECORDS,
            query=payload,
        )
        return res

    async def set_deposit_account(
        self,
        accountType: str,
    ):
        """
        :param accountType: str
        :param coin: str
        """
        payload = {
            "accountType": accountType,
        }

        res = await self._request(
            method="POST",
            path=Asset.SET_DEPOSIT_ACCOUNT,
            query=payload,
        )
        return res

    async def get_deposit_records(
        self,
        coin: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param coin: str
        :param startTime: str
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_DEPOSIT_RECORDS,
            query=payload,
        )
        return res

    async def get_sub_deposit_records(
        self,
        subMemberId: str,
        coin: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param subMemberId: str
        :param coin: str
        :param startTime: str
        :param limit: int
        """
        payload = {
            "subMemberId": subMemberId,
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_SUB_ACCOUNT_DEPOSIT_RECORDS,
            query=payload,
        )
        return res

    async def get_internal_deposit_records(
        self,
        coin: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param coin: str
        :param startTime: str
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_INTERNAL_DEPOSIT_RECORDS,
            query=payload,
        )
        return res

    async def get_master_deposit_address(
        self,
        coin: str,
    ):
        """
        :param coin: str
        """
        payload = {
            "coin": coin,
        }

        res = await self._request(
            method="GET",
            path=Asset.GET_MASTER_DEPOSIT_ADDRESS,
            query=payload,
        )
        return res

    async def get_withdrawal_records(
        self,
        coin: str = None,
        withdrawType: int = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param coin: str
        :param withdrawType: int
        :param startTime: int
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["coin"] = coin
        if withdrawType is not None:
            payload["withdrawType"] = withdrawType
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Asset.GET_WITHDRAWAL_RECORDS,
            query=payload,
        )
        return res

    async def withdraw(
        self,
        coin: str,
        chain: str,
        address: str,
        amount: str,
        tag: str = None,
    ):
        """
        :param coin: str
        :param chain: str
        :param address: str
        :param amount: str
        :param tag: str
        """
        payload = {
            "coin": coin,
            "chain": chain,
            "address": address,
            "amount": amount,
            "timestamp": int(time.time() * 1000),
            "accountType": "FUND",
            "feeType": 1,
        }
        if chain is not None:
            payload["chain"] = chain
        if tag is not None:
            payload["tag"] = tag

        res = await self._request(
            method="POST",
            path=Asset.WITHDRAW,
            query=payload,
        )
        return res

    async def cancel_withdrawal(
        self,
        id: str,
    ):
        """
        :param id: str
        """
        payload = {
            "id": id,
        }

        res = await self._request(
            method="POST",
            path=Asset.CANCEL_WITHDRAWAL,
            query=payload,
        )
        return res
