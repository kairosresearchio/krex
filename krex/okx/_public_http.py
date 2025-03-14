from ._http_manager import HTTPManager
from .endpoints.public import Public


class PublicHTTP(HTTPManager):
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
            path=Public.FUNDING_RATE,
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
            path=Public.FUNDING_RATE_HISTORY,
            query=payload,
        )
