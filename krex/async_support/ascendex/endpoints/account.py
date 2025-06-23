from enum import Enum


class CashAccount(str, Enum):
    ACCOUNT_INFO = {
        "route": "/api/pro/v1/info",
        "hash": "info",
    }

    def __str__(self) -> str:
        return self.value
