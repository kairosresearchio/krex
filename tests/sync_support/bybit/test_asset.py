from krex.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)


def test_get_coin_info():
    res = client.get_coin_info()
    assert res is not None


# def test_get_sub_uid():
#     res = client.get_sub_uid()
#     assert res is not None


def test_get_spot_asset_info():
    res = client.get_spot_asset_info()
    assert res is not None


def test_get_coins_balance():
    res = client.get_coins_balance(accountType="FUND")
    assert res is not None


def test_get_coin_balance():
    res = client.get_coin_balance(accountType="FUND", coin="BTC")
    assert res is not None


def test_get_withdrawable_amount():
    res = client.get_withdrawable_amount(coin="USDT")
    assert res is not None


def test_get_internal_transfer_records():
    res = client.get_internal_transfer_records()
    assert res is not None


def test_get_universal_transfer_records():
    res = client.get_universal_transfer_records()
    assert res is not None


def test_get_deposit_records():
    res = client.get_deposit_records()
    assert res is not None


def test_get_internal_deposit_records():
    res = client.get_internal_deposit_records()
    assert res is not None


# def test_get_master_deposit_address():
#     res = client.get_master_deposit_address(coin="USDT")
#     assert res is not None


def test_get_withdrawal_records():
    res = client.get_withdrawal_records()
    assert res is not None
