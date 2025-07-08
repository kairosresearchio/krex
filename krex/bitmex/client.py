from dataclasses import dataclass
from ._market_http import MarketHTTP
from ._account_http import AccountHTTP
from ._trade_http import TradeHTTP
from ._position_http import PositionHTTP
from ._trading_http import TradingHTTP


@dataclass
class Client(
    MarketHTTP,
    AccountHTTP,
    TradeHTTP,
    PositionHTTP,
    TradingHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
