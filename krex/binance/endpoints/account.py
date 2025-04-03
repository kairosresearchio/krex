from enum import Enum

class Account(str, Enum):

    ACCOUNT_INFO = "/api/v3/account" # get account info
    ACCOUNT_TRADE_LIST = "/api/v3/myTrades" # get trades and symbol
    QUERY_UNFILLED_ORDERS = "/api/v3/openOrders" # get, displays unfilled order count for all intervals
    QUERY_PREVENTED_MATCHES = "/api/v3/myPreventedMatches" # get, displays list of orders expired due to STP
    QUERY_ALLOCATIONS = "/api/v3/myAllocations" # get, retrieves allocations resulting from SOR order placement
    QUERY_COMMISSION_RATES = "/api/v3/commissionRate" # get, get commission rates

    def __str__(self) -> str:
        return self.value