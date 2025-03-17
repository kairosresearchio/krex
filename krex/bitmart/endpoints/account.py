from enum import Enum


class FundingAccount(str, Enum):
    # https://api-cloud.bitmart.com
    GET_ACCOUNT_BALANCE = "/account/v1/wallet"
    GET_ACCOUNT_CURRENCIES = "/account/v1/currencies"
    GET_SPOT_WALLET_BALANCE = "/spot/v1/wallet"
    DEPOSIT_ADDRESS = "/account/v1/deposit/address"
    WITHDRAW_QUOTA = "/account/v1/withdraw/charge"
    WITHDRAW = "/account/v1/withdraw/apply"
    GET_DEPOSIT_WITHDRAW_HISTORY = "/account/v2/deposit-withdraw/history"
    GET_DEPOSIT_WITHDRAW_HISTORY_DETAIL = "/account/v1/deposit-withdraw/detail"

    def __str__(self) -> str:
        return self.value


class FuturesAccount(str, Enum):
    # https://api-cloud-v2.bitmart.com
    GET_CONTRACT_ASSETS = "/contract/private/assets-detail"

    def __str__(self) -> str:
        return self.value
