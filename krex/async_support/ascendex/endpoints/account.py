from enum import Enum


class CashAccount(str, Enum):
    ACCOUNT_INFO = "/api/pro/v1/info"

    @property
    def hash(self):
        return self.value.split("/")[-1]

    def __str__(self) -> str:
        return self.value
