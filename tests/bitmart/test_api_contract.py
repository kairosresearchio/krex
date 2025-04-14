import time

from krex.http.bitmart.client import Client

BITMART_API_KEY = "api_key"
BITMART_API_SECRET = "api_secret"
MEMO = "memo"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


def test_get_contracts_details():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/details"""
    assert client.get_contracts_details(contract_symbol="ETHUSDT")[0]["code"] == 1000


def test_get_depth():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/depth"""
    assert client.get_depth(contract_symbol="ETHUSDT")[0]["code"] == 1000


def test_get_current_funding_rate():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate"""
    assert client.get_current_funding_rate(contract_symbol="ETHUSDT")[0]["code"] == 1000


def test_get_contract_kline():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/kline"""
    end_time = int(time.time())
    start_time = end_time - 3600
    assert (
        client.get_contract_kline(contract_symbol="ETHUSDT", step=5, start_time=start_time, end_time=end_time)[0][
            "code"
        ]
        == 1000
    )


def test_get_funding_rate_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate-history"""
    assert client.get_funding_rate_history(contract_symbol="ETHUSDT", limit=10)[0]["code"] == 1000


def test_get_contract_assets():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/assets-detail"""
    assert client.get_contract_assets()[0]["code"] == 1000


def test_get_contract_order_detail():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/order"""
    assert client.get_contract_order_detail(contract_symbol="BTCUSDT", order_id="220609666322019")[0]["code"] == 1000


def test_get_contract_order_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/order-history"""
    assert (
        client.get_contract_order_history(contract_symbol="BTCUSDT", start_time=1662368173, end_time=1662368179)[0][
            "code"
        ]
        == 1000
    )


def test_get_contract_open_order():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/get-open-orders"""
    assert (
        client.get_contract_open_order(contract_symbol="BTCUSDT", type="limit", order_state="all", limit=5)[0]["code"]
        == 1000
    )


def test_get_contract_position():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/position"""
    assert client.get_contract_position(contract_symbol="BTCUSDT")[0]["code"] == 1000


def test_get_contract_trade():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/trades"""
    trades = client.get_contract_trade(contract_symbol="BTCUSDT", start_time=1662368173, end_time=1662368179)
    assert trades[0]["code"] == 1000


def test_get_contract_transaction_history():
    """Test GET https://api-cloud-v2.bitmart.com/contract/private/transaction-history"""
    trades = client.get_contract_transaction_history(
        contract_symbol="BTCUSDT", start_time=1662368173, end_time=1662368179
    )
    assert trades[0]["code"] == 1000


def test_get_contract_transfer_list():
    """Test POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract-list"""
    trades = client.get_contract_transfer_list(page=1, limit=10)
    assert trades[0]["code"] == 1000


def test_place_contract_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/submit-order"""
    response = client.place_contract_order(
        contract_symbol="BTCUSDT",
        side=1,
        type="limit",
        leverage="20",
        open_type="isolated",
        size=1,
        price="78000",
        mode=1,
        stp_mode=2,
    )
    print(response)
    assert response[0]["code"] == 1000


def test_modify_limit_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/modify-limit-order"""
    response = client.modify_limit_order(contract_symbol="BTCUSDT", order_id=62970000003, price="77000")
    assert response[0]["code"] == 1000


def test_cancel_contract_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-order"""
    assert client.cancel_contract_order(contract_symbol="ETHUSDT", order_id="220906179559421")[0]["code"] == 1000

    assert client.cancel_contract_order(contract_symbol="ETHUSDT")[0]["code"] == 1000

    assert client.cancel_contract_order(contract_symbol="ETHUSDT", client_order_id="220906179559421")[0]["code"] == 1000


def test_cancel_all_contract_order():
    """Test POST https://api-cloud-v2.bitmart.com/contract/private/cancel-orders"""
    assert client.cancel_all_contract_order(contract_symbol="ETHUSDT")[0]["code"] == 1000


def test_transfer_contract():
    """Test POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract"""
    assert client.transfer_contract(currency="USDT", amount="10", type="spot_to_contract")[0]["code"] == 1000


def test_submit_leverage():
    """POST https://api-cloud-v2.bitmart.com/contract/private/submit-leverage"""
    assert client.submit_leverage(contract_symbol="BTCUSDT", open_type="cross", leverage="1")[0]["code"] == 1000
