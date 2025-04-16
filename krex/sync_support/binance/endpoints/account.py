from enum import Enum


class FuturesAccount(str, Enum):
    # https://fapi.binance.com
    ACCOUNT_BALANCE = "/fapi/v3/balance"
    INCOME_HISTORY = "/fapi/v1/income"

    def __str__(self) -> str:
        return self.value
