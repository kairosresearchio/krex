from dataclasses import dataclass
from ._trade_http import TradeHTTP
from ._market_http import MarketHTTP
from ._account_http import AccountHTTP


@dataclass
class Client(
    TradeHTTP,
    MarketHTTP,
    AccountHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
