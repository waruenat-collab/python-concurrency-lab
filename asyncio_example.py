import asyncio
import time

async def task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"End {name}")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

start = time.time()
asyncio.run(main())
print(f"Total time: {time.time() - start:.2f} seconds")