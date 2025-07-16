from enum import Enum


class Trading(str, Enum):
    GET_EXECUTION_HISTORY = "/api/v1/user/executionHistory"
    GET_EXECUTIONS = "/api/v1/execution"
    GET_TRADE_HISTORY = "/api/v1/execution/tradeHistory"
    GET_TRADING_VOLUME = "/api/v1/user/tradingVolume"

    def __str__(self) -> str:
        return self.value
