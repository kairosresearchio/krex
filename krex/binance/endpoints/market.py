from enum import Enum

class Market(str, Enum):
    ORDER_BOOK = "/api/v3/depth"
    RECENT_TRADES_LIST = "/api/v3/trades"
    OLD_TRADES_LOOKUP = "/api/v3/historicalTrades"
    AGG_TRADES_LIST = "/api/v3/aggTrades"
    KLINE_CANDLESTICK_DATA = "/api/v3/klines"
    UIKLINES = "/api/v3/klines"
    CURRENT_AVERAGE_PRICE = "/api/v3/avgPrice"
    HR_24_TICKER_PRICE_CHANGE = "/api/v3/ticker/24hr"
    TRADING_DAY_TICKER = "/api/v3/ticker/tradingDay"
    SYMBOL_PRICE_TICKER = "/api/v3/ticker/price"
    SYMBOL_ORDER_BOOK_TICKER = "/api/v3/ticker/bookTicker"
    ROLLING_WINDOW_PRICE_CHANGE = "/api/v3/ticker"


    def __str__(self) -> str:
        return self.value