from enum import Enum


class SwapAccount(str, Enum):
    ACCOUNT_BALANCE = "/openApi/swap/v3/user/balance"
    OPEN_POSITIONS = "/openApi/swap/v2/user/positions"
    FUND_FLOW = "/openApi/swap/v2/user/income"
    LISTEN_KEY = "/openApi/user/auth/userDataStream"

    def __str__(self) -> str:
        return self.value
