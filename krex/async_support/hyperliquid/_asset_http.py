from ._http_manager import HTTPManager
from .endpoint.path import Path
from .endpoint.asset import Asset


class AssetHTTP(HTTPManager):
    async def user_vault_equities(
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

        res = await self._request(
            method="POST",
            path=Path.INFO,
            query=payload,
            signed=False,
        )
        return res
