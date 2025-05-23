import asyncio
import math
import os
import time
from dotenv import load_dotenv

from krex.async_support.bybit.client import Client
from krex.websocket.bybit import BybitPublicSpotWsClient, BybitPrivateWsClient
from krex.websocket.data.market_data import MarketData
from krex.async_support.product_table.manager import ProductTableManager
from krex.utils.common import Common

load_dotenv()


def round_down(value: float, decimals: int) -> float:
    factor = 10**decimals
    return math.floor(value * factor) / factor


def round_qty(value: float, precision: float) -> str:
    decimals = abs(int(round(math.log10(precision))))
    return f"{round_down(value, decimals):.{decimals}f}"


class SpotHedgeStrategyBybit:
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        product_symbol: str,
        qty: float,
        timeout_sec: int = 5,
        delivery_code: str = None,
    ):
        self.spot_symbol = product_symbol + "-SPOT"
        if delivery_code:
            delivery_base = product_symbol.replace("USDT", "USD")
            self.future_symbol = f"{delivery_base}-{delivery_code}-SWAP"
        else:
            self.future_symbol = product_symbol + "-SWAP"

        self.ws_symbol = product_symbol.replace("-", "")

        self.qty = qty
        self.timeout_sec = timeout_sec
        self.market_data = MarketData()
        self.order_id = None
        self.spot_filled = 0.0
        self.future_filled = 0.0
        self.filled_orders = {}
        self.min_hedge_qty = 0.001
        self.spot_precision = 0.001

        self.api_key = api_key
        self.api_secret = api_secret

        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True,
        )

    async def execute(self):
        await self._initialize_ws_clients()
        await asyncio.sleep(1)  # Wait for WebSocket connection to fully initialize

        await self.client.async_init()
        ptm = await ProductTableManager.get_instance()
        self.min_hedge_qty = float(ptm.get_trading_details(self.future_symbol, Common.BYBIT)["min_size"])
        self.spot_precision = float(ptm.get_trading_details(self.spot_symbol, Common.BYBIT)["size_precision"])
        print(f"📀 Futures minimum trade size: {self.min_hedge_qty}")

        while self.spot_filled < self.qty:
            best_bid = await self._get_ws_best_bid_price()
            if best_bid is None:
                print("⚠️ Unable to get latest best bid price, retrying later")
                await asyncio.sleep(1)
                continue

            remain_qty = self.qty - self.spot_filled
            rounded_qty = round_qty(remain_qty, self.spot_precision)
            print(f"📅 Trying to place order @ {best_bid}, remaining {rounded_qty}")

            try:
                res = await self.client.place_post_only_limit_buy_order(
                    product_symbol=self.spot_symbol,
                    qty=rounded_qty,
                    price=str(best_bid),
                )
            except Exception as e:
                print(f"❌ Order placement failed: {e}")
                await asyncio.sleep(1)
                continue

            self.order_id = res.get("result", {}).get("orderId")
            print(f"📦 Attempting to place order, Order ID: {self.order_id}")

            if not self.order_id:
                print("❌ Order response does not contain valid Order ID")
                await asyncio.sleep(1)
                continue

            # Confirm the order wasn't immediately canceled (WS should update status)
            await asyncio.sleep(0.5)  # Wait for WS order status update
            trade_data = await self.market_data.get_all_trade_statuses()
            trade = trade_data.get(Common.BYBIT, {}).get(self.ws_symbol)
            if not trade or trade.status.name == "CANCELLED":
                print("❌ Order was cancelled")
                await asyncio.sleep(0.5)
                continue

            print(f"📦 Order successfully placed, status is {trade.status.name}, waiting for execution...")

            await self._wait_for_fill_or_timeout()

            if self.spot_filled >= self.qty:
                print("✅ Spot order fully executed")
                break

            print("⌛ Timeout before full execution, cancelling and replacing order")
            try:
                await self.client.cancel_order(
                    product_symbol=self.spot_symbol,
                    orderId=self.order_id,
                )
            except Exception as e:
                print(f"⚠️ Cancel order failed: {e}")
            await asyncio.sleep(0.5)

    async def _get_ws_best_bid_price(self):
        try:
            orderbooks = await self.market_data.get_all_depth_data()
            # print(f"📊 Current orderbook: {orderbooks}")
            clean_symbol = self.ws_symbol
            ob = orderbooks.get(Common.BYBIT, {}).get(clean_symbol)
            return float(ob.best_bid_price) if ob else None
        except Exception as e:
            print(f"⚠️ Unable to get best bid price from WebSocket: {e}")
            return None

    async def try_hedge(self):
        diff_qty = self.spot_filled - self.future_filled

        # Determine precision based on min_hedge_qty, e.g., 0.001 → 3
        precision = abs(int(round(math.log10(self.min_hedge_qty))))
        hedge_qty = round_down(diff_qty, precision)

        if hedge_qty >= self.min_hedge_qty:
            print(f"🔁 Futures hedge market order: Sell {hedge_qty:.{precision}f} BTC")
            try:
                await self.client.place_market_sell_order(
                    product_symbol=self.future_symbol,
                    qty=str(hedge_qty),
                    reduceOnly=False,
                    isLeverage=1,
                )
                self.future_filled += hedge_qty
            except Exception as e:
                print(f"❌ Futures hedge failed: {e}")
        else:
            print(
                f"⚠️ Hedge quantity has not reached minimum size {self.min_hedge_qty}, current difference {hedge_qty:.{precision}f}"
            )

    async def _wait_for_fill_or_timeout(self):
        start_time = time.time()

        while time.time() - start_time < self.timeout_sec:
            trade_data = await self.market_data.get_all_trade_statuses()
            trade = trade_data.get(Common.BYBIT, {}).get(self.ws_symbol)
            # print(f"📍 Trying to get status for trading pair {symbol_key}: {trade}")

            if not trade or trade.filled_quantity == 0:
                await asyncio.sleep(0.5)
                continue

            filled = trade.filled_quantity
            delta = filled - self.filled_orders.get(self.order_id, 0.0)

            if delta > 0:
                print(f"📈 New execution: +{delta:.8f} @ {trade.deal_avg_price}")
                self.spot_filled += delta
                self.filled_orders[self.order_id] = filled

                await self.try_hedge()

            if filled >= trade.quantity:
                print("✅ Order fully executed")
                return

            await asyncio.sleep(0.5)

    async def _initialize_ws_clients(self):
        public_ws = await BybitPublicSpotWsClient.create(
            subscription={"op": "subscribe", "args": [f"orderbook.1.{self.ws_symbol}"]},
            is_sandbox=True,
        )
        public_ws.market_data = self.market_data

        private_ws = await BybitPrivateWsClient.create(
            api_key=self.api_key,
            api_secret=self.api_secret,
            subscription={"op": "subscribe", "args": ["order"]},
            is_sandbox=True,
        )
        private_ws.market_data = self.market_data

        asyncio.create_task(public_ws.start())
        asyncio.create_task(private_ws.start())


async def main():
    product_symbol = "BTC-USDT"
    delivery_code = "M25"

    strat = SpotHedgeStrategyBybit(
        api_key=os.getenv("BYBIT_APIKEY"),
        api_secret=os.getenv("BYBIT_APISECRET"),
        product_symbol=product_symbol,
        delivery_code=delivery_code,
        qty=0.01,
    )
    await strat.execute()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
