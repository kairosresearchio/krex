from ._trade_http import TradeHTTP
from ._account_http import AccountHTTP
from ._asset_http import AssetHTTP
from ._position_http import PositionHTTP
from ._market_http import MarketHTTP


class Client(
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    PositionHTTP,
    MarketHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)

    async def __aenter__(self):
        await self.async_init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()
