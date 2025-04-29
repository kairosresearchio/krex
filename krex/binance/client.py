from dataclasses import dataclass
from ._trade_http import TradeHTTP
from ._account_http import AccountHTTP
from ._market_http import MarketHTTP


@dataclass
class Client(
    TradeHTTP,
    AccountHTTP,
    MarketHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
