from ._http_manager import HTTPManager
from .endpoints.public import Public


class PublicHTTP(HTTPManager):
    def get_instruments(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        instId: str = None,
    ):
        """
        :param instType: str
        :param uly: str
        :param instFamily: str
        :param instId: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if instId is not None:
            payload["instId"] = instId

        return self._request(
            method="GET",
            path=Public.GET_INSTRUMENT_INFO,
            query=payload,
        )

    def get_funding_rate(
        self,
        instId: str,
    ):
        """
        :param instId: str
        """
        payload = {
            "instId": instId,
        }

        return self._request(
            method="GET",
            path=Public.GET_FUNDING_RATE,
            query=payload,
        )

    def get_funding_rate_history(
        self,
        instId: str,
        before: str = None,
        after: str = None,
        limit: str = None,
    ):
        """
        :param instId: str
        """
        payload = {
            "instId": instId,
        }
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        return self._request(
            method="GET",
            path=Public.GET_FUNDING_RATE_HISTORY,
            query=payload,
        )
