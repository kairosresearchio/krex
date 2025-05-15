from dataclasses import dataclass


@dataclass
class BookTicker:
    symbol: str
    best_bid_price: float
    best_bid_quantity: float
    best_ask_price: float
    best_ask_quantity: float
    timestamp: int
    funding_rate: float = 0.0