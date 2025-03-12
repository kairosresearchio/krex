from ._http_manager import HTTPManager
from .endpoints.account import Account


class MarketHTTP(HTTPManager):
    def get_instruments_info(self):
        pass
    
    def get_kline(self):
        pass
    
    def get_orderbook(self):
        pass

    def get_tickers(self):
        pass
    
    def get_funding_rate_history(self):
        pass