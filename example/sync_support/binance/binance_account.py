import krex
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


client = krex.binance(
    api_key=BINANCE_API_KEY,
    api_secret=BINANCE_API_SECRET,
)

result = client.get_account_balance()
print(result)

result = client.get_income_history()
print(result)
