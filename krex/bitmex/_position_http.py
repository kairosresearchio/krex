from typing import Union
from krex.utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.positions import Positions


class PositionHTTP(HTTPManager):
    def get_positions(
        self,
        filter: str | None = None,
        columns: str | None = None,
        count: int | None = None,
        target_account_id: int | None = None,
        target_account_ids: Union[list, str] | None = None,
    ):
        """
        :param filter: str
        :param columns: str
        :param count: int
        :param target_account_id: int
        :param target_account_ids: list[str] or str
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if filter is not None:
            payload["filter"] = filter

        if columns is not None:
            payload["columns"] = columns

        if count is not None:
            payload["count"] = count

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        if target_account_ids is not None:
            payload["targetAccountIds"] = target_account_ids

        res = self._request(
            method="GET",
            path=Positions.GET_POSITIONS,
            query=payload,
        )
        return res

    def switch_mode(
        self,
        product_symbol: str,
        enabled: bool = True,
    ):
        """
        Isolated Margin or Cross Margin (True for isolated margin, false for cross margin.)

        :param product_symbol: str
        :param enabled: bool (Default: True)
        """
        assert self.ptm is not None
        payload: dict[str, str | int | list[str] | float | bool] = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol),
            "enabled": enabled,
        }

        res = self._request(
            method="POST",
            path=Positions.SWITCH_MODE,
            query=payload,
        )
        return res

    def set_leverage(
        self,
        product_symbol: str,
        leverage: float,
        cross_margin: bool = True,
        target_account_id: int | None = None,
    ):
        """
        :param product_symbol: str
        :param leverage: float
        :param cross_margin: bool (True for cross margin, false for isolated margin.)
        :param target_account_id: int
        """
        assert self.ptm is not None
        payload: dict[str, str | int | list[str] | float] = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMEX, product_symbol),
            "leverage": leverage,
            "crossMargin": cross_margin,
        }

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        res = self._request(
            method="POST",
            path=Positions.LEVERAGE,
            query=payload,
        )
        return res

    def set_margining_mode(
        self,
        multi_asset: bool = False,
        target_account_id: int | None = None,
    ):
        """
        :param multi_asset: bool (True for multi-asset margining, False for single-asset)
        :param target_account_id: int
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if multi_asset:
            payload["marginingMode"] = "MultiAsset"
        # For single-asset margining, leave the field empty (don't include it)

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        res = self._request(
            method="POST",
            path=Positions.MARGINING_MODE,
            query=payload,
        )
        return res

    def get_margining_mode(
        self,
        target_account_id: int | None = None,
        target_account_ids: Union[list, str] | None = None,
    ):
        """
        :param target_account_id: int
        :param target_account_ids: list[str] or str
        """
        payload: dict[str, str | int | list[str] | float | bool] = {}

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        if target_account_ids is not None:
            payload["targetAccountIds"] = target_account_ids

        res = self._request(
            method="GET",
            path=Positions.MARGINING_MODE,
            query=payload,
        )
        return res

    def get_margin(
        self,
        currency: str = "all",
        target_account_id: int | None = None,
        target_account_ids: Union[list, str] | None = None,
    ):
        """
        :param currency: str
        :param target_account_id: int
        :param target_account_ids: list[str] or str
        """
        payload: dict[str, str | int | list[str] | float | bool] = {
            "currency": currency,
        }

        if target_account_id is not None:
            payload["targetAccountId"] = target_account_id

        if target_account_ids is not None:
            payload["targetAccountIds"] = target_account_ids

        res = self._request(
            method="GET",
            path=Positions.GET_MARGIN,
            query=payload,
        )
        return res
