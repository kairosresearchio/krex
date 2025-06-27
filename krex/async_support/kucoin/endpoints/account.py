from enum import Enum


class SpotAccount(str, Enum):
    ACCOUNT_BALANCE = "/api/v1/accounts"

    def __str__(self) -> str:
        return self.value
