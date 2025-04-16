from ._trade_http import TradeHTTP
from ._market_http import MarketHTTP
from ._account_http import AccountHTTP


# @dataclass
class Client(
    TradeHTTP,
    MarketHTTP,
    AccountHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)

    async def __aenter__(self):
        await self.async_init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()
