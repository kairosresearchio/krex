from enum import Enum


class Account(str, Enum):
    GET_WALLET_BALANCE= "/cloud/trade/v3/account/wallet-balance"

    def __str__(self) -> str:
        return self.value
