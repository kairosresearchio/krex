from enum import Enum


class SpotMarket(str, Enum):
    GET_CURRENCIES_LIST = "/spot/v1/currencies"
    GET_TRADING_PAIRS_LIST = "/spot/v1/symbols"
    GET_TRADING_PAIRS_DETAILS = "/spot/v1/symbols/details"
    GET_TICKER_OF_ALL_PAIRS = "/spot/quotation/v3/tickers"
    GET_TICKER_OF_A_PAIR = "/spot/quotation/v3/ticker"
    GET_LATEST_KLINE_DATA = "/spot/quotation/v3/lite-klines"
    
    def __str__(self) -> str:
        return self.value
    

class FuturesMarket(str, Enum):
    GET_CONTRACTS_DETAILS = "/contract/public/details"
    GET_DEPTH = "/contract/public/depth"
    GET_CURRENT_FUNDING_RATE = "/contract/public/funding-rate"
    GET_KLINE = "/contract/public/kline"
    GET_FUNDING_RATE_HISTORY = "/contract/public/funding-rate-history"
    
    def __str__(self) -> str:
        return self.value
    

