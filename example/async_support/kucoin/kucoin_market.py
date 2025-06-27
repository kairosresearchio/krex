import asyncio
import krex.async_support as krex


async def main():
    client = await krex.kucoin()

    try:
        instrument_info = await client.get_spot_instrument_info()
        print(instrument_info)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
