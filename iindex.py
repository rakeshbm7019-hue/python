import asyncio
import random
async def sensor_stream(n):
    for i in range(n):
        await asyncio.sleep(0.5)  # simulate delay
        yield {"id": i, "value": random.randint(1, 100)}

async def filter_stream(stream, threshold=50):
    async for data in stream:
        if data["value"] > threshold:
            yield data

async def transform_stream(stream):
    async for data in stream:
        yield {"id": data["id"], "processed": data["value"] ** 2}

async def consume(stream):
    async for item in stream:
        print("Processed:", item)

async def main():
    raw = sensor_stream(10)
    filtered = filter_stream(raw, threshold=70)
    transformed = transform_stream(filtered)
    await consume(transformed)

if __name__ == "__main__":
    asyncio.run(main())
