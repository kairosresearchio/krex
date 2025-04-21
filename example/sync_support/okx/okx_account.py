from krex.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"

client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)

result = client.get_account_instruments(
    instType="SPOT",
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_account_balance()
print(result)

result = client.get_positions(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_positions_history(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_position_risk()
print(result)

result = client.get_account_bills(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_account_bills_archive(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.post_account_bills_history_archive(
    year="2025",
    quarter="Q1",
)
print(result)

result = client.get_account_bills_history_archive(
    year="2025",
    quarter="Q1",
)
print(result)

result = client.get_account_config()
print(result)

result = client.set_position_mode(
    posMode="long_short_mode",
)
print(result)

result = client.get_max_order_size(
    product_symbol="BTC-USDT-SPOT",
    tdMode="isolated",
)
print(result)

result = client.get_max_avail_size(
    product_symbol="BTC-USDT-SPOT",
    tdMode="cash",
)
print(result)

result = client.get_leverage(
    product_symbol="BTC-USDT-SWAP",
    mgnMode="cross",
)
print(result)

result = client.get_adjust_leverage(
    product_symbol="BTC-USDT-SWAP",
    instType="SWAP",
    mgnMode="cross",
    lever="3",
)
print(result)

result = client.get_max_loan(
    product_symbol="BTC-USDT-SPOT",
    mgnMode="cross",
    mgnCcy="USDT",
)
print(result)

result = client.get_fee_rates(
    product_symbol="BTC-USDT-SPOT",
    instType="SPOT",
)
print(result)

result = client.get_interest_accrued(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_interest_rate()
print(result)

result = client.set_greeks(greeksType="PA")
print(result)

result = client.get_max_withdrawal()
print(result)

result = client.get_quick_borrow_repay_history(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_interest_limits()
print(result)

result = client.spot_borrow_repay_history()
print(result)

result = client.set_leverage(
    lever="10",
    mgnMode="cross",
    product_symbol="BTC-USDT-SWAP",
)
print(result)

result = client.set_isolated_mode(type="CONTRACTS")
print(result)

# # need test
# result = client.adjustment_margin(
#     product_symbol="BTC-USDT-SWAP",
#     posSide="short",
#     type="add",
#     amt="0.001",
# )
# print(result)

# # need test
# result = client.quick_borrow_repay(
#     product_symbol="BTC-USDT-SPOT",
#     ccy="USDT",
#     side="borrow",
#     amt="0.01",
# )
# print(result)

# # need test
# result = client.spot_manual_borrow_repay(
#     ccy="USDT",
#     side="borrow",
#     amt="0.01",
# )
# print(result)

# # need test
# result = client.set_auto_repay(autoRepay="true")
# print(result)

# # need test
# result = client.set_risk_offset_amt(
#     ccy="USDT",
#     clSpotInUseAmt="0.01",
# )
# print(result)

# # need test
# result = client.set_auto_loan(autoLoan="true")
# print(result)
