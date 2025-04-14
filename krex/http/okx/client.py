from dataclasses import dataclass
from ._trade_http import TradeHTTP
from ._account_http import AccountHTTP
from ._asset_http import AssetHTTP
from ._public_http import PublicHTTP
from ._market_http import MarketHTTP


@dataclass
class Client(
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    PublicHTTP,
    MarketHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
