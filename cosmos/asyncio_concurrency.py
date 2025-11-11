# asyncio_concurrency.py
import asyncio
from contextlib import suppress

async def io_bound_task(x):
    # Simulate async I/O
    await asyncio.sleep(0.1)
    return x * x

async def bounded_worker(x, sem):
    async with sem:
        return await io_bound_task(x)

async def main():
    sem = asyncio.Semaphore(100)  # limit in-flight operations
    tasks = [asyncio.create_task(bounded_worker(i, sem)) for i in range(1000)]

    try:
        results = await asyncio.wait_for(asyncio.gather(*tasks), timeout=5.0)
        print("Results sample:", results[:5])
    except asyncio.TimeoutError:
        print("Timed out, cancelling...")
        for t in tasks:
            t.cancel()
        with suppress(asyncio.CancelledError):
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())