from enum import Enum


class Balance(str, Enum):
    CASH_ACCOUNT_BALANCE = {
        "route": "{ACCOUNT_GROUP}/api/pro/v1/cash/balance",
        "hash": "balance",
    }

    def __str__(self) -> str:
        return self.value
