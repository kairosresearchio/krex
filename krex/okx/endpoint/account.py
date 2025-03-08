from enum import Enum


class Account(str, Enum):
    GET_INSTRUMENTS = "/api/v5/account/instruments"
    ACCOUNT_INFO = "/api/v5/account/balance"
    POSITION_INFO = "/api/v5/account/positions"
    POSITIONS_HISTORY = "/api/v5/account/positions-history"
    POSITION_RISK = "/api/v5/account/account-position-risk"
    BILLS_DETAIL = "/api/v5/account/bills"
    BILLS_ARCHIVE = "/api/v5/account/bills-archive"
    BILLS_HISTORY_ARCHIVE = "/api/v5/account/bills-history-archive"  # Need to add
    ACCOUNT_CONFIG = "/api/v5/account/config"
    POSITION_MODE = "/api/v5/account/set-position-mode"
    SET_LEVERAGE = "/api/v5/account/set-leverage"
    MAX_TRADE_SIZE = "/api/v5/account/max-size"
    MAX_AVAIL_SIZE = "/api/v5/account/max-avail-size"
    ADJUSTMENT_MARGIN = "/api/v5/account/position/margin-balance"
    GET_LEVERAGE = "/api/v5/account/leverage-info"
    GET_ADJUST_LEVERAGE = "/api/v5/account/adjust-leverage-info"  # Need to add
    MAX_LOAN = "/api/v5/account/max-loan"
    FEE_RATES = "/api/v5/account/trade-fee"
    INTEREST_ACCRUED = "/api/v5/account/interest-accrued"
    INTEREST_RATE = "/api/v5/account/interest-rate"
    SET_GREEKS = "/api/v5/account/set-greeks"
    ISOLATED_MODE = "/api/v5/account/set-isolated-mode"
    MAX_WITHDRAWAL = "/api/v5/account/max-withdrawal"
    ACCOUNT_RISK = "/api/v5/account/risk-state"
    QUICK_BORROW_REPAY = "/api/v5/account/quick-margin-borrow-repay"  # Need to add
    QUICK_BORROW_REPAY_HISTORY = (
        "/api/v5/account/quick-margin-borrow-repay-history"  # Need to add
    )
    INTEREST_LIMITS = "/api/v5/account/interest-limits"
    MANUAL_REBORROW_REPAY = "/api/v5/account/spot-manual-borrow-repay"
    SET_AUTO_REPAY = "/api/v5/account/set-auto-repay"
    GET_BORROW_REPAY_HISTORY = "/api/v5/account/spot-borrow-repay-history"
    POSITION_BUILDER = "/api/v5/account/position-builder"
    SET_RISK_OFFSET_AMT = "/api/v5/account/set-riskOffset-amt"  # Need to add
    GREEKS = "/api/v5/account/greeks"
    GET_PM_LIMIT = "/api/v5/account/position-tiers"
    ACTIVSTE_OPTION = "/api/v5/account/activate-option"
    SET_AUTO_LOAN = "/api/v5/account/set-auto-loan"
    PRESET_ACCOUNT_LEVEL_SWITCH = (
        "/api/v5/account/account-level-switch-preset"  # Need to add
    )
    PRECHECK_ACCOUNT_LEVEL_SWITCH = (
        "/api/v5/account/set-account-switch-precheck"  # Need to add
    )
    SET_ACCOUNT_LEVEL = "/api/v5/account/set-account-level"
    ACCOUNT_MMP_RESET = "/api/v5/account/mmp-reset"  # Need to add
    ACCOUNT_MMP_CONFIG = "/api/v5/account/mmp-config"  # Need to add

    # Interface under maintenance
    SIMULATED_MARGIN = "/api/v5/account/simulated_margin"
    BORROW_REPAY = "/api/v5/account/borrow-repay"
    BORROW_REPAY_HISTORY = "/api/v5/account/borrow-repay-history"
    GET_VIP_INTEREST_ACCRUED_DATA = "/api/v5/account/vip-interest-accrued"
    GET_VIP_INTEREST_DEDUCTED_DATA = "/api/v5/account/vip-interest-deducted"
    GET_VIP_LOAN_ORDER_LIST = "/api/v5/account/vip-loan-order-list"
    GET_VIP_LOAN_ORDER_DETAIL = "/api/v5/account/vip-loan-order-detail"
