import logging
from dataclasses import dataclass
from ._trade_http import TradeHTTP
from ._account_http import AccountHTTP
from ._asset_http import AssetHTTP
from ._position_http import PositionHTTP
from ._spot_margin_trade_http import SpotMarginTradeHTTP


logger = logging.getLogger(__name__)


@dataclass
class Client(
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    PositionHTTP,
    SpotMarginTradeHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
