from enum import Enum


class Balance(str, Enum):
    CASH_ACCOUNT_BALANCE = "/{ACCOUNT_GROUP}/api/pro/v1/cash/balance"

    @property
    def hash(self):
        return self.value.split("/")[-1]

    def __str__(self) -> str:
        return self.value
