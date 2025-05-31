from krex.hyperliquid.client import Client


client = Client(
    wallet_address= "",
    private_key= "" 
) 

result = client.place_order(
    product_symbol= "PURR-USDC-SPOT",
    isBuy= True,
    price= "0.1",
    size = "100",
    reduceOnly= False,
    tif= "Gtc"
)
print(result)

result = client.place_future_market_order(
    product_symbol= "BTC-USD-SWAP",
    isBuy= True,
    size = "0.00011",
    triggerPx= "10000",
    tpsl= "sl"
)
print(result)

result = client.place_future_market_buy_order(
    product_symbol= "BTC-USD-SWAP",
    size = "0.00011",
    triggerPx= "10000",
    tpsl= "sl"
)
print(result)

result = client.place_future_market_sell_order(
    product_symbol= "ETH-USD-SWAP",
    size = "0.0011",
    triggerPx= "10000",
    tpsl= "sl"
)
print(result)

result = client.place_future_limit_order(
    product_symbol= "BTC-USD-SWAP",
    isBuy= True,
    price= "104320",
    size = "0.00011",
    tif= "Gtc"
)
print(result)

result = client.place_future_limit_buy_order(
    product_symbol= "BTC-USD-SWAP",
    price= "104320",
    size = "0.00011",
    tif= "Gtc"
)
print(result)

result = client.place_future_limit_sell_order(
    product_symbol= "BTC-USD-SWAP",
    price= "104320",
    size = "0.00011",
    tif= "Gtc"
)
print(result)

result = client.cancel_order(
    product_symbol= "BTC-USD-SWAP",
    oid= 98746214479
)
print(result)

result = client.schedule_cancel(
    time= 1748628637000
)
print(result)

result = client.modify_order(
    oid= 32755192478,
    product_symbol= "MELANIA-USDC-SWAP",
    isBuy= True,
    price= "0.3",
    size = "200",
    reduceOnly= False,
    tif = "Gtc"
)
print(result)

result = client.modify_batch_orders(
        modifies= [{
        "oid": 98758682365,
        "order": {
            'a': 1, 
            'b': False, 
            'p': '2510', 
            's': '0.011', 
            'r': False, 
            't': {'trigger': {
                'isMarket': True, 
                'triggerPx': '10000', 
                'tpsl': 'sl'
                }
            }
        }}
        ,{
        "oid": 98758542882,
        "order":{
            'a': 0, 
            'b': False, 
            'p': '103410', 
            's': '0.00011', 
            'r': False, 
            't': {'trigger': {
                'isMarket': True, 
                'triggerPx': '10000', 
                'tpsl': 'sl'
                }
            }
        }}
        ]
    )
print(result)

result = client.update_leverage(
    product_symbol= "MELANIA-USD-SWAP",
    isCross= False,
    leverage= 3
)
print(result)

result = client.update_isolate_margin(
    product_symbol= "BTC-USD-SWAP",
    isBuy= True,
    ntli= 2
)
print(result)

result = client.place_twap_order(
    product_symbol= "MELANIA-USD-SWAP",
    isBuy= True,
    size = "10000",
    reduceOnly= False,
    minutes= 5,  
    randomize= False
)
print(result)

result = client.cancel_twap_order(
    product_symbol= "MELANIA-USD-SWAP",
    twap_id= 744123
)
print(result)