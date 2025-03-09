from dataclasses import dataclass
from ._trade_http import TradeHTTP


@dataclass
class Client(
    TradeHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)
