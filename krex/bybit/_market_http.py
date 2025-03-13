from ._http_manager import HTTPManager
from .endpoints.market import Market


class MarketHTTP(HTTPManager):
    def get_instruments_info(
        self,
        category: str,
        symbol: str = None,
        status: str = None,
        baseCoin: str = None,
        limit: int = None,
    ):
        """
        :param category: str (spot, linear, inverse, option)
        :param symbol: str
        :param status: str
        :param baseCoin: str
        :param limit: int
        """
        payload = {
            "category": category,
        }
        if symbol is not None:
            payload["symbol"] = symbol
        if status is not None:
            payload["status"] = status
        if baseCoin is not None:
            payload["baseCoin"] = baseCoin
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Market.GET_INSTRUMENTS_INFO,
            query=payload,
        )

    def get_kline(
        self,
        symbol: str,
        interval: str,
        category: str = None,
        startTime: int = None,
        limit: int = None,
    ):
        """
        :param symbol: str
        :param interval: str
        :param category: str (spot, linear, inverse) default is linear
        :param startTime: int
        :param limit: int
        """
        payload = {
            "symbol": symbol,
            "interval": interval,
        }
        if category is not None:
            payload["category"] = category
        if startTime is not None:
            payload["start"] = startTime
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Market.GET_KLINE,
            query=payload,
        )

    def get_orderbook(
        self,
        category: str,
        symbol: str,
        limit: int = None,
    ):
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param limit: int
        """
        payload = {
            "category": category,
            "symbol": symbol,
        }
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Market.GET_ORDERBOOK,
            query=payload,
        )

    def get_tickers(
        self,
        category: str,
        symbol: str = None,
        baseCoin: str = None,
    ):
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param baseCoin: str
        """
        payload = {
            "category": category,
        }
        if symbol is not None:
            payload["symbol"] = symbol
        if baseCoin is not None:
            payload["baseCoin"] = baseCoin

        return self._request(
            method="GET",
            path=Market.GET_TICKERS,
            query=payload,
        )

    def get_funding_rate_history(
        self,
        category: str,
        symbol: str,
        startTime: int = None,
        limit: int = None,
    ):
        """
        :param category: str (linear, inverse)
        :param symbol: str
        :param startTime: int
        :param limit: int
        """
        payload = {
            "category": category,
            "symbol": symbol,
        }
        if startTime is not None:
            payload["startTime"] = startTime
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Market.GET_FUNDING_RATE_HISTORY,
            query=payload,
        )
