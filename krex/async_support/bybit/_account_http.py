from typing import List, Optional
from ._http_manager import HTTPManager
from .endpoints.account import Account
from ...utils.common import Common


class AccountHTTP(HTTPManager):
    
    # ------- Common functions -------
    
    async def get_balance(
        self,
        account_type: str = "UNIFIED",
    ):
        """
        Obtain wallet balance, query asset information of each currency. By default, currency information with assets or liabilities of 0 is not returned.
        Normally, you should use the UNIFIED account.

        Parameters
        ----------
        account_type : str[UNIFIED, CONTRACT, SPOT]
            The type of the account. If not specified, the default is UNIFIED.

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/wallet-balance
        """
        payload = {
            "accountType": account_type,
        }

        res = await self._request(
            method="GET",
            path=Account.GET_WALLET_BALANCE,
            query=payload,
        )
        return res
    
    async def get_fee_rates(
        self,
        product_symbol: Optional[str] = None,
        category: Optional[str] = "linear",
    ):
        """
        Get the trading fee rate.

        Parameters
        ----------
        product_symbol : str
            The product symbol of the trading fee rate. If not specified, the default is all linear products.
        category : str[spot, linear, inverse, option]
            The category of the trading fee rate. If you specify the product_symbol, the category can be ignored.

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/fee-rate
        """
        payload = {}
        if product_symbol is not None:
            payload["category"] = self.ptm.get_product_type(product_symbol, Common.BYBIT)
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BYBIT)

        elif category is not None:
            payload["category"] = category

        res = await self._request(
            method="GET",
            path=Account.GET_FEE_RATE,
            query=payload,
        )
        return res

    async def get_capital_flow(
        self,
        category: Optional[str] = None,
        coin: Optional[str] = None,
        startTime: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        """
        Fetches the capital flow of the account. Such as deposit, withdraw, transfer, trade, etc.

        Parameters
        ----------
        category : str[spot, linear, inverse, option]
            The category of the instrument that the capital flow belongs to.
        coin : str
            The coin of the capital flow belongs to.
        startTime : int
            The start time of the capital flow. If not specified, the default is 24 hours ago.
        limit : int
            The maximum number of capital flow to retrieve on each page. If not specified, the default is 20.

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/transaction-log
        """
        payload = {}
        if category is not None:
            payload["category"] = category
        if coin is not None:
            payload["currency"] = coin
        if startTime is not None:
            payload["startTime"] = startTime
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Account.GET_TRANSACTION_LOG,
            query=payload,
        )
        return res

    async def get_transferable_amount(
        self,
        coins: List[str],
    ):
        """
        Query the available amount to transfer of a specific coin in the Unified wallet.

        Parameters
        ----------
        coins : list
            Coin name, uppercase only. Supports up to 20 coins per request

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/unified-trans-amnt
        """
        payload = {}
        if coins is not None:
            coinName = ",".join(coins)
            payload = {
                "coinName": coinName,
            }

        res = await self._request(
            method="GET",
            path=Account.GET_TRANSFERABLE_AMOUNT,
            query=payload,
        )
        return res
    
    # ------- Exchange Specific functions -------

    async def upgrade_to_unified_account(self):
        """
        Upgrade to Unified account.

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/upgrade-unified-account
        """
        res = await self._request(
            method="POST",
            path=Account.UPGRADE_TO_UNIFIED_ACCOUNT,
            query=None,
        )
        return res

    async def get_borrow_history(
        self,
        coin: Optional[str] = None,
        startTime: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        """
        Get interest records, sorted in reverse order of creation time.

        Parameters
        ----------
        coin : str
            USDC, USDT, BTC, ETH etc, uppercase only
        startTime : int
            The start time of the borrowing history. If not specified, the default is 24 hours ago.
        limit : int
            The maximum number of interest records to retrieve on each page. If not specified, the default is 20.

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/borrow-history
        """
        payload = {
            "limit": limit,
        }
        if coin is not None:
            payload["currency"] = coin
        if startTime is not None:
            payload["startTime"] = startTime

        res = await self._request(
            method="GET",
            path=Account.GET_BORROW_HISTORY,
            query=payload,
        )
        return res

    async def repay_liability(
        self,
        coin: Optional[str] = None,
    ):
        """
        You can manually repay the liabilities of Unified account.

        Parameters
        ----------
        coin : str
            The coin with liability, uppercase only
            Input the specific coin: repay the liability of this coin in particular
            No coin specified: repay the liability of all coins

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/repay-liability
        """
        payload = {}
        if coin is not None:
            payload = {
                "coin": coin,
            }

        res = await self._request(
            method="POST",
            path=Account.REPAY_LIABILITY,
            query=payload,
        )
        return res

    async def get_collateral_info(
        self,
        coin: Optional[str] = None,
    ):
        """
        Get the collateral information of the current unified margin account, including loan interest rate, loanable amount, collateral conversion rate, whether it can be mortgaged as margin, etc.

        Parameters
        ----------
        coin : str
            Asset currency of all current collateral, uppercase only

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/collateral-info
        """
        payload = {}
        if coin is not None:
            payload = {
                "coin": coin,
            }

        res = await self._request(
            method="GET",
            path=Account.GET_COLLATERAL_INFO,
            query=payload,
        )
        return res

    async def set_collateral(
        self,
        coin: str,
        switch: str,
    ):
        """
        Set the collateral coin switch.

        Parameters
        ----------
        coin : str
            The coin of the collateral.
        switch : str "ON" or "OFF"

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/set-collateral
        """
        payload = {
            "coin": coin,
            "collateralSwitch": switch,
        }

        res = await self._request(
            method="POST",
            path=Account.SET_COLLATERAL_COIN,
            query=payload,
        )
        return res

    async def set_margin_mode(
        self,
        margin_mode: str,
    ):
        """
        Set the margin mode.

        Parameters
        ----------
        margin_mode : str[ISOLATED_MARGIN, REGULAR_MARGIN, PORTFOLIO_MARGIN]

        Returns
        -------
        Please refer to the official documentation for more details: https://bybit-exchange.github.io/docs/v5/account/set-margin-mode
        """
        payload = {
            "setMarginMode": margin_mode,
        }

        res = await self._request(
            method="POST",
            path=Account.SET_MARGIN_MODE,
            query=payload,
        )
        return res
