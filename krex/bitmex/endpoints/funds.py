from enum import Enum


class Account(str, Enum):
    ACCOUNT_INFO = "/api/v1/user/wallet"

    def __str__(self) -> str:
        return self.value
