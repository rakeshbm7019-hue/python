import asyncio
import random

async def fetch_data(n):
    print(f"Task {n} started...")
    await asyncio.sleep(random.uniform(0.5, 2.0))  # simulate I/O
    print(f"Task {n} finished!")
    return f"Result {n}"

async def main():
    tasks = [fetch_data(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    print("All results:", results)

if __name__ == "__main__":
    asyncio.run(main())
