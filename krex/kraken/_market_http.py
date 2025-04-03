from ..utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.market import Market


class MarketHTTP(HTTPManager):
    def get_server_time(self, nonce: int):
        """
        Gets the server's time from Kraken API.
        """
        payload = {
            "nonce": nonce
        }
        
        return self.http._request(
            method="POST",
            endpoint=str(Market.GET_SERVER_TIME),
            data=payload,
            auth=False  # No authentication needed for this endpoint
        )

    def get_system_status(self, nonce: int):
        """
        Retrieves the current system status from Kraken API.
        """
        payload = {
            "nonce": nonce
        }
        
        return self.http._request(
            method="POST",
            endpoint=str(Market.GET_SYSTEM_STATUS),
            data=payload,
            auth=False  # No authentication needed for this endpoint
        )
    
    def get_asset_info(self, nonce: int, asset: str = None, aclass: str = 'currency'):
        """
        Retrieves information about available assets for deposit, withdrawal, trading, and earn.
        Parameters:
            nonce: A unique integer to ensure the request is unique.
            asset: A comma delimited list of assets to retrieve information for. Default is None, meaning all assets will be retrieved.
            aclass: The asset class. Default is 'currency'. Options include 'currency' and 'commodity', etc.
        """
        payload = {
            "nonce": nonce,
            "asset": asset,  # Optional: Comma delimited list of assets
            "aclass": aclass  # Optional: Asset class (default: currency)
        }
        
        # Remove None values to keep the payload clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Market.GET_ASSET_INFO),
            data=payload,
            auth=False  # No authentication needed for this public endpoint
        )
    
    def get_tradable_asset_pairs(self, nonce: int, pair: str = None, info: str = 'info', country_code: str = None):
        """
        Retrieves tradable asset pairs from Kraken.
        Parameters:
            nonce: A unique integer to ensure the request is unique.
            pair: A comma-delimited list of asset pairs to retrieve info for. Default is None, meaning all tradable pairs are retrieved.
            info: The type of information to retrieve. Default is 'info' (general info). Options include 'info', 'leverage', 'fees', 'margin'.
            country_code: Optional filter to restrict pairs to certain countries/regions.
        """
        payload = {
            "nonce": nonce,
            "pair": pair,  # Optional: A comma-delimited list of asset pairs (e.g., "BTC/USD,ETH/BTC")
            "info": info,  # Optional: Type of info to retrieve (default: 'info')
            "country_code": country_code  # Optional: Filter by country/region (e.g., 'US:TX,GB,CA')
        }

        # Remove None values to keep the payload clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Market.GET_TRADABLE_ASSET_PAIRS),
            data=payload,
            auth=False  # No authentication needed for this public endpoint
        )
    
    def get_ticker_information(self, nonce: int, pair: str = None):
        """
        Retrieves ticker information for a specific asset pair or all tradable asset pairs.
        Parameters:
            nonce: A unique integer to ensure the request is unique.
            pair: A specific asset pair to get ticker information for (e.g., "XBTUSD"). If None, all tradable pairs are returned.
        """
        payload = {
            "nonce": nonce,
            "pair": pair  # Optional: Specific asset pair (e.g., "XBTUSD")
        }

        # Remove None values to keep the payload clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Market.GET_TICKER_INFORMATION),
            data=payload,
            auth=False  # No authentication needed for this public endpoint
        )