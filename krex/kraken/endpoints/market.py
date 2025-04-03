from enum import Enum



class Market(str, Enum):
    GET_SERVER_TIME = "/0/public/Time" # get the server's time
    GET_SYSTEM_STATUS = "/0/public/SystemStatus" # get current system status or trading mode
    GET_ASSET_INFO = "/0/public/Assets" # get info about assets that are available for deposit, withdrawl, trading, and earn
    GET_TRADABLE_ASSET_PAIRS = "/0/public/AssetPairs" # get tradable asset pairs
    GET_TICKER_INFO = "/0/public/Ticker" # get ticker info for all or requested markets
    GET_OHLC_DATA = "" # retrieve ohlc market data
    GET_ORDER_BOOK = "" # returns level 2 order book
    GET_RECENT_TRADES = "" # returns last 1000 trades by default
    GET_RECENT_SPREADS = "" # returns last 200 top of book spreads for a given pair

    def __str__(self) -> str:
        return self.value
