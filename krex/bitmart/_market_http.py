from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket, FuturesMarket
from ..utils.common import Common
from ..utils.timeframe_utils import bitmart_convert_timeframe


class MarketHTTP(HTTPManager):
    def get_spot_currencies(self):
        res = self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_CURRENCIES,
            query=None,
            signed=False,
        )
        return res

    def get_trading_pairs(self):
        res = self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS,
            query=None,
            signed=False,
        )
        return res

    def get_trading_pairs_details(self):
        res = self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS_DETAILS,
            query=None,
            signed=False,
        )
        return res

    def get_ticker_of_all_pairs(self):
        res = self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_ALL_PAIRS,
            query=None,
            signed=False,
        )
        return res

    def get_ticker_of_a_pair(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }

        res = self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_A_PAIR,
            query=payload,
            signed=False,
        )
        return res

    def get_spot_kline(
        self,
        product_symbol: str,
        interval: str,
        before: int = None,
        after: int = None,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param before: int
        :param after: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMART, product_symbol),
        }
        if interval is not None:
            payload["step"] = bitmart_convert_timeframe(interval)
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_KLINE,
            query=payload,
            signed=False,
        )
        return res

    def get_contracts_details(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(Common.BITMART, product_symbol)

        res = self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_DETAILS,
            query=payload,
            signed=False,
        )
        return res

    def get_depth(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMART, product_symbol),
        }

        res = self._request(
            method="GET",
            path=FuturesMarket.GET_DEPTH,
            query=payload,
            signed=False,
        )
        return res

    def get_contract_kline(
        self,
        product_symbol: str,
        interval: str,
        start_time: int,
        end_time: int,
    ):
        """
        :param product_symbol: str
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMART, product_symbol),
            "step": bitmart_convert_timeframe(interval),
            "start_time": start_time,
            "end_time": end_time,
        }

        res = self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_KLINE,
            query=payload,
            signed=False,
        )
        return res

    def get_current_funding_rate(
        self,
        product_symbol: str,
    ):
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMART, product_symbol),
        }

        res = self._request(
            method="GET",
            path=FuturesMarket.GET_CURRENT_FUNDING_RATE,
            query=payload,
            signed=False,
        )
        return res

    def get_funding_rate_history(
        self,
        product_symbol: str,
        limit: int = None,
    ):
        """
        :param product_symbol: str
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(Common.BITMART, product_symbol),
        }
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=FuturesMarket.GET_FUNDING_RATE_HISTORY,
            query=payload,
            signed=False,
        )
        return res
