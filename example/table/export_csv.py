import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT)

import asyncio
import pandas as pd
from krex.product_table.manager import ProductTableManager


async def test_fetch_product_tables():
    manager = await ProductTableManager()
    product_table = await manager._fetch_product_tables()

    if isinstance(product_table, pd.DataFrame) and not product_table.empty:
        print(product_table.head())

        csv_filename = "product_table.csv"
        product_table.to_csv(csv_filename, index=False, encoding="utf-8-sig")
        print(f"📁 Data successfully exported to {csv_filename}")
    else:
        print("❌ _fetch_product_tables test failed. The returned DataFrame is either empty or of an incorrect type.")


if __name__ == "__main__":
    asyncio.run(test_fetch_product_tables())
