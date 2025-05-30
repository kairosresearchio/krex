from dataclasses import dataclass
from ._account_http import AccountHTTP
from ._asset_http import AssetHTTP
from ._market_http import MarketHTTP


@dataclass
class Client(
    AccountHTTP,
    AssetHTTP,
    MarketHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
