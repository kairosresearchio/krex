from dataclasses import dataclass
from ._account_http import AccountHTTP
from ._earn_http import EarnHTTP
from ._funding_http import FundingHTTP
from ._market_http import MarketHTTP
from ._otc_http import OTCHTTP
from ._subaccount_http import SubAccountHTTP
from ._trade_http import TradeHTTP

@dataclass
class Client(
    AccountHTTP,
    EarnHTTP,
    FundingHTTP,
    MarketHTTP,
    OTCHTTP,
    SubAccountHTTP,
    TradeHTTP
):
    def __init__(self, **args):
        super().__init__(**args)
