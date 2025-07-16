import krex
import os
from dotenv import load_dotenv

load_dotenv()

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")


client = krex.bitmex(
    api_key=BITMEX_API_KEY,
    api_secret=BITMEX_API_SECRET,
)

# executions = client.get_executions(product_symbol="XBT-USDT-SWAP", count=5)
# print(executions)

# trade_history = client.get_trade_history(product_symbol="XBT-USDT-SWAP", count=5)
# print(trade_history)

trading_volume = client.get_trading_volume()
print(trading_volume)
print(client.get_rate_limit_info())
