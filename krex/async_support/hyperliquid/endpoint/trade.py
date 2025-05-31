from enum import Enum


class Trade(str, Enum):
    ORDER = "order"
    CANCEL = "cancel"
    CANCELBYCLOID = "cancelByCloid"
    SCHEDULECANCEL = "scheduleCancel"
    MODIFY = "modify"
    BATCHMODIFY = "batchModify"
    UPDATELEVERAGE = "updateLeverage"
    UPDATEISOLATEMARGIN = "updateIsolatedMargin"
    TWAPORDER = "twapOrder"
    TWAPCANCEL = "twapCancel"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return repr(self.value)
