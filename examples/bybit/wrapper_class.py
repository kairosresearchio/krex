from krex.bybit.client import Client


BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = False  # True means your API keys were generated on testnet.bybit.com


class BybitWrapper:
    def __init__(
        self,
        api_key: str = None,
        api_secret: str = None,
        testnet: bool = None,
    ):
        self.instance = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=testnet,
        )

    def cancel_all_orders(
        self,
        category: str = "spot",
        symbol: str = "ETHUSDT",
    ) -> dict:
        """
        Cancel orders by category and symbol
        """
        return self.instance.cancel_all_orders(category=category, symbol=symbol)

    def get_realtime_orders(
        self,
        category: str,
        symbol: str = None,
    ) -> dict:
        """
        Get realtime orders
        """
        return self.instance.get_open_orders(
            category=category,
            symbol=symbol,
        )

    def get_order_history(self, **kwargs) -> dict:
        return self.instance.get_order_history(**kwargs)["result"]["list"]


wrapper = BybitWrapper(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

response = wrapper.get_realtime_orders(category="linear", symbol="ETHUSDT")
print(response)
