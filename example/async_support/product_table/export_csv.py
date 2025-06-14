import asyncio
import polars as pl
from krex.async_support.product_table.manager import ProductTableManager


async def test_fetch_product_tables():
    manager = await ProductTableManager.get_instance()

    if isinstance(manager.product_table, pl.DataFrame) and manager.product_table.height > 0:
        print(manager.product_table.head())

        csv_filename = "product_table.csv"
        manager.product_table.write_csv(csv_filename)
        print(f"📁 Data successfully exported to {csv_filename}")
    else:
        print("❌ _fetch_product_tables test failed. The returned DataFrame is either empty or of an incorrect type.")


if __name__ == "__main__":
    asyncio.run(test_fetch_product_tables())
