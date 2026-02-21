import asyncio

async def main():
    print("Hello asyncio")
    await asyncio.sleep(1)
    print("Done")

asyncio.run(main())