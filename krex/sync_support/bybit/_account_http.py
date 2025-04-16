from ._http_manager import HTTPManager
from .endpoints.account import Account
from ...utils.common import Common


class AccountHTTP(HTTPManager):
    def get_wallet_balance(self):
        """
        default UNIFIED account and ensure the account is upgraded to unified account before trading
        """
        payload = {
            "accountType": "UNIFIED",
        }

        return self._request(
            method="GET",
            path=Account.GET_WALLET_BALANCE,
            query=payload,
        )

    def get_transferable_amount(
        self,
        coins: list = None,
    ):
        """
        :param coins: list
        """
        payload = {}
        if coins is not None:
            coinName = ",".join(coins)
            payload = {
                "coinName": coinName,
            }

        return self._request(
            method="GET",
            path=Account.GET_TRANSFERABLE_AMOUNT,
            query=payload,
        )

    def upgrade_to_unified_trading_account(self):
        """
        upgrade to unified trading account
        """
        return self._request(
            method="POST",
            path=Account.UPGRADE_TO_UNIFIED_ACCOUNT,
            query=None,
        )

    def get_borrow_history(self, coin: str = None, startTime: int = None, limit: int = 20):
        """
        :param coin: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["currency"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        return self._request(
            method="GET",
            path=Account.GET_BORROW_HISTORY,
            query=payload,
        )

    def repay_liability(
        self,
        coin: str = None,
    ):
        """
        :param coin: str
        """
        payload = {}
        if coin is not None:
            payload = {
                "coin": coin,
            }

        return self._request(
            method="POST",
            path=Account.REPAY_LIABILITY,
            query=payload,
        )

    def get_collateral_info(
        self,
        coin: str = None,
    ):
        """
        :param coin: str
        """
        payload = {}
        if coin is not None:
            payload = {
                "coin": coin,
            }

        return self._request(
            method="GET",
            path=Account.GET_COLLATERAL_INFO,
            query=payload,
        )

    def set_collateral_coin(
        self,
        coin: str,
        switch: str,
    ):
        """
        :param coin: str
        :param switch: str "ON" or "OFF"
        """
        payload = {
            "coin": coin,
            "collateralSwitch": switch,
        }

        return self._request(
            method="POST",
            path=Account.SET_COLLATERAL_COIN,
            query=payload,
        )

    def get_fee_rates(
        self,
        product_symbol: str = None,
        category: str = None,
    ):
        """
        Get the trading fee rate
        if product_symbol is not specified, pls specify the category

        :param product_symbol: str
        :param category: str Product type. spot, linear, inverse, option
        """
        payload = {}
        if product_symbol is not None:
            payload["category"] = self.ptm.get_product_type(product_symbol, Common.BYBIT)
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT)

        if category is not None:
            payload["category"] = category

        return self._request(
            method="GET",
            path=Account.GET_FEE_RATE,
            query=payload,
        )

    def get_account_info(self):
        return self._request(
            method="GET",
            path=Account.GET_ACCOUNT_INFO,
            query=None,
        )

    def get_transaction_log(
        self,
        category: str = None,
        coin: str = None,
        startTime: int = None,
        limit: int = 20,
    ):
        """
        :param category: str
        :param coin: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "limit": limit,
        }
        if category is not None:
            payload["category"] = category
        if coin is not None:
            payload["currency"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        return self._request(
            method="GET",
            path=Account.GET_TRANSACTION_LOG,
            query=payload,
        )

    def set_margin_mode(
        self,
        margin_mode: str,
    ):
        """
        :param margin_mode: str ISOLATED_MARGIN, REGULAR_MARGIN(i.e. Cross margin), PORTFOLIO_MARGIN
        """
        payload = {
            "setMarginMode": margin_mode,
        }

        return self._request(
            method="POST",
            path=Account.SET_MARGIN_MODE,
            query=payload,
        )
