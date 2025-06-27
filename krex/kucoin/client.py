from ._market_http import MarketHTTP
from ._account_http import AccountHTTP


class Client(
    MarketHTTP,
    AccountHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Close the client and clean up resources."""
        if hasattr(self, "session") and self.session is not None:
            self.session.close()
            self.session = None 