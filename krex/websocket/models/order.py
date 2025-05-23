from dataclasses import dataclass
from enum import Enum


class OrderStatus(str, Enum):
    OPEN = "open"
    FILLED = "filled"
    CANCELLED = "cancelled"
    PARTIALLY_FILLED = "partially_filled"
    # REJECTED = "rejected"


class OrderType(str, Enum):
    LIMIT = "limit"
    MARKET = "market"


class OrderMode(str, Enum):
    POST_ONLY = "post_only"
    IOC = "ioc"
    FOK = "fok"
    GTC = "gtc"


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Exchange(str, Enum):
    OKX = "okx"
    BITMART = "bitmart"
    BYBIT = "bybit"


@dataclass
class TradeStatus:
    order_id: str
    client_oid: str
    order_type: str
    status: OrderStatus
    price: float
    quantity: float
    filled_quantity: float
    deal_avg_price: float


@dataclass
class TradeRequest:
    exchange: Exchange
    symbol: str
    side: OrderSide
    price: float
    quantity: float
    order_type: OrderType
    mode: OrderMode
    client_oid: str
    is_open_new_position: bool = False
    create_time: int = None
