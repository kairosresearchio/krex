from enum import Enum


class Account(str, Enum):
    CLEARINGHOUSESTATE = "clearinghouseState"
    OPENORDERS = "openOrders"
    USERFILLS = "userFills"
    USERRATELIMIT = "userRateLimit"
    ORDERSTATUS = "orderStatus"
    HISTORICALORDERS = "historicalOrders"
    SUBACCOUNTS = "subaccounts"
    USERROLE = "userRole"
    PORTFOLIO = "portfolio"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return repr(self.value)
