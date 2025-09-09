from enum import Enum


class Public(str, Enum):
    GET_INSTRUMENT_INFO = "/api/v5/public/instruments"
    GET_FUNDING_RATE = "/api/v5/public/funding-rate"
    GET_FUNDING_RATE_HISTORY = "/api/v5/public/funding-rate-history"
    GET_POSITION_TIERS = "/api/v5/public/position-tiers"

    def __str__(self) -> str:
        return self.value
