import asyncio
import krex.async_support as krex


async def main():
    wallet_address = ""
    client = await krex.hyperliquid(
        wallet_address=wallet_address,
        private_key="",  # Replace with your private key
    )

    try:
        result = await client.place_order(
            product_symbol="BTC-USD-SWAP",
            isBuy=True,
            price="104320",
            size="0.00011",
            reduceOnly=False,
            isMarket=True,
            triggerPx="10000",
            tpsl="sl",
            grouping="na",
        )
        print(result)

        result = await client.place_future_market_order(
            product_symbol="BTC-USD-SWAP", isBuy=True, size="0.00011", triggerPx="10000", tpsl="sl"
        )
        print(result)

        result = await client.place_future_market_buy_order(
            product_symbol="BTC-USD-SWAP", size="0.00011", triggerPx="10000", tpsl="sl"
        )
        print(result)

        result = await client.place_future_market_sell_order(
            product_symbol="BTC-USD-SWAP", size="0.00011", triggerPx="10000", tpsl="sl"
        )
        print(result)

        result = await client.place_future_limit_order(
            product_symbol="BTC-USD-SWAP", isBuy=True, price="104320", size="0.00011", tif="Gtc"
        )
        print(result)

        result = await client.place_future_limit_buy_order(
            product_symbol="BTC-USD-SWAP", price="104320", size="0.00011", tif="Gtc"
        )
        print(result)

        result = await client.place_future_limit_sell_order(
            product_symbol="BTC-USD-SWAP", price="104320", size="0.00011", tif="Gtc"
        )
        print(result)

        result = await client.cancel_order(product_symbol="BTC-USD-SWAP", oid=98517251376)
        print(result)

        result = await client.schedule_cancel(time=1748628637000)
        print(result)

        result = await client.modify_order(
            oid=32755192478,
            product_symbol="MELANIA-USDC-SWAP",
            isBuy=True,
            price="0.3",
            size="200",
            reduceOnly=False,
            tif="Gtc",
        )
        print(result)

        result = await client.modify_order(
            oid=32755192478,
            product_symbol="MELANIA-USDC-SWAP",
            isBuy=True,
            price="0.3",
            size="200",
            reduceOnly=False,
            tif="Gtc",
        )
        print(result)

        result = await client.update_leverage(product_symbol="MELANIA-USDC-SWAP", isCross=False, leverage=3)
        print(result)

        result = await client.update_isolate_margin(product_symbol="BTC-USDC-SWAP", isBuy=True, ntli=2)
        print(result)

        result = await client.place_twap_order(
            product_symbol="MELANIA-USDC-SWAP", isBuy=True, size="10000", reduceOnly=False, minutes=5, randomize=False
        )
        print(result)

        result = await client.cancel_twap_order(product_symbol="MELANIA-USDC-SWAP", twap_id=6249)
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
