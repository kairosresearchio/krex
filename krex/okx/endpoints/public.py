from enum import Enum


class Public(str, Enum):
    FUNDING_RATE = "/api/v5/public/funding-rate"
    FUNDING_RATE_HISTORY = "/api/v5/public/funding-rate-history"

    def __str__(self) -> str:
        return self.value
