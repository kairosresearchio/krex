from dataclasses import dataclass
from ._trade_http import TradeHTTP
from ._account_http import AccountHTTP
from ._asset_http import AssetHTTP


@dataclass
class Client(
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
