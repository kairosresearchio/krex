from enum import Enum


class Asset(str, Enum):
    GET_COIN_INFO = "/v5/asset/coin/query-info"
    GET_SUB_UID = "/v5/asset/transfer/query-sub-member-list"
    GET_SPOT_ASSET_INFO = "/v5/asset/transfer/query-asset-info"
    GET_ALL_COINS_BALANCE = "/v5/asset/transfer/query-account-coins-balance"
    GET_SINGLE_COIN_BALANCE = "/v5/asset/transfer/query-account-coin-balance"
    GET_WITHDRAWABLE_AMOUNT = "/v5/asset/withdraw/withdrawable-amount"
    GET_INTERNAL_TRANSFER_RECORDS = "/v5/asset/transfer/query-inter-transfer-list"
    GET_TRANSFERABLE_COIN = "/v5/asset/transfer/query-transfer-coin-list"
    CREATE_INTERNAL_TRANSFER = "/v5/asset/transfer/inter-transfer"
    CREATE_UNIVERSAL_TRANSFER = "/v5/asset/transfer/universal-transfer"
    GET_UNIVERSAL_TRANSFER_RECORDS = "/v5/asset/transfer/query-universal-transfer-list"
    SET_DEPOSIT_ACCOUNT = "/v5/asset/deposit/deposit-to-account"
    GET_DEPOSIT_RECORDS = "/v5/asset/deposit/query-record"
    GET_SUB_ACCOUNT_DEPOSIT_RECORDS = "/v5/asset/deposit/query-sub-member-record"
    GET_INTERNAL_DEPOSIT_RECORDS = "/v5/asset/deposit/query-internal-record"
    GET_MASTER_DEPOSIT_ADDRESS = "/v5/asset/deposit/query-address"
    GET_WITHDRAWAL_RECORDS = "/v5/asset/withdraw/query-record"
    WITHDRAW = "/v5/asset/withdraw/create"
    CANCEL_WITHDRAWAL = "/v5/asset/withdraw/cancel"

    def __str__(self) -> str:
        return self.value
