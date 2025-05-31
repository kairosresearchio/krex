from ._http_manager import HTTPManager
from .endpoints.path import Path
from .endpoints.asset import Asset


class AssetHTTP(HTTPManager):
    def user_vault_equities(
        self,
        user: str,
    ):
        """
        :param user: str (waller address)
        """
        payload = {
            "type": Asset.USERVAULTEQUITIES,
            "user": user,
        }

        res = self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
