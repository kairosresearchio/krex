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

positions = client.get_positions()
print(positions)

res = client.switch_mode(product_symbol="XBT-USDT-SWAP", enabled=True)
print(res)

res = client.set_leverage(product_symbol="XBT-USDT-SWAP", leverage=10, cross_margin=True)
print(res)

margining_mode = client.set_margining_mode()
print(margining_mode)

margining_mode = client.get_margining_mode()
print(margining_mode)

margin = client.get_margin()
print(margin)
