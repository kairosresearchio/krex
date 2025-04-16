from dataclasses import dataclass


@dataclass
class BalanceInfo:
    symbol: str
    available_balance: float
    position_deposit: float
    frozen_balance: float
