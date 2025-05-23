from dataclasses import dataclass
from enum import Enum


class PositionSide(str, Enum):
    LONG = "long"
    SHORT = "short"
    NONE = "none"  # okx 轉入保證金後會產生pos為0的情況


@dataclass
class PositionInfo:
    symbol: str
    side: PositionSide
    quantity: float
    open_avg_price: float
    # closed_volume: float
