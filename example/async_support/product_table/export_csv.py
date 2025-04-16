import asyncio
import pandas as pd
from krex.async_support.product_table.manager import ProductTableManager


async def test_fetch_product_tables():
    manager = await ProductTableManager.get_instance()

    if isinstance(manager.product_table, pd.DataFrame) and not manager.product_table.empty:
        print(manager.product_table.head())

        csv_filename = "product_table.csv"
        manager.product_table.to_csv(csv_filename, index=False, encoding="utf-8-sig")
        print(f"📁 Data successfully exported to {csv_filename}")
    else:
        print("❌ _fetch_product_tables test failed. The returned DataFrame is either empty or of an incorrect type.")


if __name__ == "__main__":
    asyncio.run(test_fetch_product_tables())
