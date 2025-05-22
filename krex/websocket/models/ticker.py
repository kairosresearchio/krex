from dataclasses import dataclass


@dataclass
class BookTicker:
    symbol: str
    product_type: str
    best_bid_price: float
    best_bid_quantity: float
    best_ask_price: float
    best_ask_quantity: float
    timestamp: int
