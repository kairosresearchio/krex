from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket, FuturesMarket


class MarketHTTP(HTTPManager):
    def get_spot_currencies(self):
        return self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_CURRENCIES,
            query=None,
        )

    def get_trading_pairs(self):
        return self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS,
            query=None,
        )

    def get_trading_pairs_details(self):
        return self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS_DETAILS,
            query=None,
        )

    def get_ticker_of_all_pairs(self):
        return self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_ALL_PAIRS,
            query=None,
        )

    def get_ticker_of_a_pair(
        self,
        symbol: str,
    ):
        """
        :param symbol: str
        """
        payload = {
            "symbol": symbol,
        }

        return self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_A_PAIR,
            query=payload,
        )

    def get_spot_kline(
        self,
        symbol: str,
        before: int = None,
        after: int = None,
        limit: int = None,
    ):
        """
        :param symbol: str
        :param before: int
        :param after: int
        :param limit: int
        """
        payload = {
            "symbol": symbol,
        }
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_KLINE,
            query=payload,
        )

    def get_contracts_details(
        self,
        symbol: str = None,
    ):
        """
        :param symbol: str
        """
        payload = {}
        if symbol is not None:
            payload["symbol"] = symbol

        return self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_DETAILS,
            query=payload,
        )

    def get_depth(
        self,
        symbol: str,
    ):
        """
        :param symbol: str
        """
        payload = {
            "symbol": symbol,
        }

        return self._request(
            method="GET",
            path=FuturesMarket.GET_DEPTH,
            query=payload,
        )

    def get_contract_kline(
        self,
        symbol: str,
        startTime: int,
        endTime: int,
    ):
        """
        :param symbol: str
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "symbol": symbol,
            "startTime": startTime,
            "endTime": endTime,
        }

        return self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_KLINE,
            query=payload,
        )

    def get_current_funding_rate(
        self,
        symbol: str,
    ):
        """
        :param symbol: str
        """
        payload = {
            "symbol": symbol,
        }

        return self._request(
            method="GET",
            path=FuturesMarket.GET_CURRENT_FUNDING_RATE,
            query=payload,
        )

    def get_funding_rate_history(
        self,
        symbol: str,
        limit: int = None,
    ):
        """
        :param symbol: str
        :param limit: int
        """
        payload = {
            "symbol": symbol,
        }
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=FuturesMarket.GET_FUNDING_RATE_HISTORY,
            query=payload,
        )
