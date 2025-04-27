from enum import Enum


class Asset(str, Enum):
    CURRENCY_INFO = "/api/v5/asset/currencies"
    GET_BALANCES = "/api/v5/asset/balances"
    ASSET_VALUATION = "/api/v5/asset/asset-valuation"
    FUNDS_TRANSFER = "/api/v5/asset/transfer"
    TRANSFER_STATE = "/api/v5/asset/transfer-state"
    BILLS_INFO = "/api/v5/asset/bills"
    DEPOSIT_ADDRESS = "/api/v5/asset/deposit-address"
    DEPOSIT_HISTORY = "/api/v5/asset/deposit-history"
    WITHDRAWAL_COIN = "/api/v5/asset/withdrawal"
    CANCEL_WITHDRAWAL = "/api/v5/asset/cancel-withdrawal"
    WITHDRAWAL_HISTORY = "/api/v5/asset/withdrawal-history"
    GET_DEPOSIT_WITHDRAW_STATUS = "/api/v5/asset/deposit-withdraw-status"
    EXCHANGE_LIST = "/api/v5/asset/exchange-list"
    MONTHLY_STATEMENT = "/api/v5/asset/monthly-statement"
    GET_CURRENCIES = "/api/v5/asset/convert/currencies"
    CONVERT_HISTORY = "/api/v5/asset/convert/history"
