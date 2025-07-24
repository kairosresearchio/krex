import asyncio
import krex.async_support as krex
from dotenv import load_dotenv

load_dotenv()

# ZOOMEX_API_KEY = os.getenv("ZOOMEX_API_KEY")
# ZOOMEX_API_SECRET = os.getenv("ZOOMEX_API_SECRET")


async def main():
    client = await krex.zoomex()

    res = await client.get_instruments_info()
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
