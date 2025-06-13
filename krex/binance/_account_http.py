from ._http_manager import HTTPManager
from .endpoints.account import FuturesAccount
from ..utils.common import Common


class AccountHTTP(HTTPManager):
    def get_account_balance(
        self,
    ):
        res = self._request(
            method="GET",
            path=FuturesAccount.ACCOUNT_BALANCE,
            query=None,
        )
        return res

    def get_income_history(
        self,
        product_symbol: str = None,
        incomeType: str = None,
        startTime: int = None,
        endTime: int = None,
        page: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param incomeType: str (TRANSFER, WELCOME_BONUS, REALIZED_PNL, FUNDING_FEE, COMMISSION, INSURANCE_CLEAR, REFERRAL_KICKBACK, COMMISSION_REBATE, API_REBATE, CONTEST_REWARD, CROSS_COLLATERAL_TRANSFER, OPTIONS_PREMIUM_FEE, OPTIONS_SETTLE_PROFIT, INTERNAL_TRANSFER, AUTO_EXCHANGE, DELIVERED_SETTELMENT, COIN_SWAP_DEPOSIT, COIN_SWAP_WITHDRAW, POSITION_LIMIT_INCREASE_FEE, STRATEGY_UMFUTURES_TRANSFER，FEE_RETURN，BFUSD_REWARD)
        :param startTime: int
        :param endTime: int
        :param page: int
        :param limit: int
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BINANCE, product_symbol)
        if incomeType is not None:
            payload["incomeType"] = incomeType
        if startTime is not None:
            payload["startTime"] = startTime
        if endTime is not None:
            payload["endTime"] = endTime
        if page is not None:
            payload["page"] = page
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=FuturesAccount.INCOME_HISTORY,
            query=payload,
        )
        return res
