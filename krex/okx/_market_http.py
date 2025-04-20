from ._http_manager import HTTPManager
from .endpoints.market import Market


class MarketHTTP(HTTPManager):
    def get_candlesticks(
        self,
        instId: str,
        bar: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param instId: str
        :param bar: str
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {
            "instId": instId,
        }
        if bar is not None:
            payload["bar"] = bar
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Market.GET_KLINE,
            query=payload,
        )

    def get_orderbook(
        self,
        instId: str,
        sz: str = None,
    ):
        """
        :param instId: str
        :param sz: str
        """
        payload = {
            "instId": instId,
        }
        if sz is not None:
            payload["sz"] = sz

        return self._request(
            method="GET",
            path=Market.GET_ORDERBOOK,
            query=payload,
        )

    def get_tickers(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
    ):
        """
        :param instType: str (SPOT, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily

        return self._request(
            method="GET",
            path=Market.GET_TICKERS,
            query=payload,
        )
