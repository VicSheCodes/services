"""
add asyncio loop example
"""

import asyncio

async def async_task(name, duration):
    print(f"Task {name} starting...")
    await asyncio.sleep(duration)
    print(f"Task {name} completed after {duration} seconds.")
    return name

async def main():
    tasks = [
        async_task("A", 2),
        async_task("B", 3),
        async_task("C", 1)
    ]
    results = await asyncio.gather(*tasks)
    print(f"All tasks completed. Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())