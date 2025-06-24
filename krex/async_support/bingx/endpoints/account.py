from enum import Enum


class SwapAccount(str, Enum):
    ACCOUNT_BALANCE = "/openApi/swap/v3/user/balance"
    OPEN_POSITIONS = "/openApi/swap/v2/user/positions"
    FUND_FLOW = "/openApi/swap/v2/user/income"
    LISTEN_KEY = "/openApi/user/auth/userDataStream" # 你一定會有點 confused haha pls see: https://bingx-api.github.io/docs/#/en-us/swapV2/socket/listenKey.html%23generate%20Listen%20Key

    def __str__(self) -> str:
        return self.value
