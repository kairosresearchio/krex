from enum import Enum


class Account(str, Enum):
    GET_WALLET_BALANCE = "/v5/account/wallet-balance"
    GET_TRANSFERABLE_AMOUNT = "/v5/account/withdrawal"
    UPGRADE_TO_UNIFIED_ACCOUNT = "/v5/account/upgrade-to-uta"
    GET_BORROW_HISTORY = "/v5/account/borrow-history"
    REPAY_LIABILITY = "/v5/account/quick-repayment"
    GET_COLLATERAL_INFO = "/v5/account/collateral-info"
    SET_COLLATERAL_COIN = "/v5/account/set-collateral-switch"
    GET_FEE_RATE = "/v5/account/fee-rate"
    GET_ACCOUNT_INFO = "/v5/account/info"
    GET_TRANSACTION_LOG = "/v5/account/transaction-log"
    SET_MARGIN_MODE = "/v5/account/set-margin-mode"

    def __str__(self) -> str:
        return self.value
