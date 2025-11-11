# 1. Basic async/await syntax
# Task: Write a coroutine that prints "Start", sleeps asynchronously for 2 seconds, then prints "Done".
# Goal: Show understanding of async / await and asyncio.sleep().

import asyncio
import aiohttp

async def print_stat_and_sleep():
    print(f"\nStart")
    await asyncio.sleep(2)
    print(f"\nDone")

def test_print_stat_and_sleep():
    asyncio.run(print_stat_and_sleep())

# 2. Running two coroutines concurrently
# Task: Run two async functions concurrently so that the total runtime ≈ the longest sleep, not the sum.


async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")

async def gather_the_task():
    await asyncio.gather(task("A", 2), task("B", 3))

def test_gather_the_task():
    asyncio.run(gather_the_task())


# Q21. How would you download 100 URLs concurrently with asyncio?

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

# results = await asyncio.gather(*[fetch(u) for u in urls])

async def download_100_urls():
    urls = ["https://example.com", "https://example.org"]  # add your URLs
    results = await asyncio.gather(*(fetch(u) for u in urls))
    print(len(results))

def test_download_100_urls():
    asyncio.run(download_100_urls())


# Q22. How can you throttle concurrency (e.g. 5 coroutines at a time)?

sem = asyncio.Semaphore(5)

async def bounded_fetch(url, sem=sem):
    async with sem:
        return await fetch(url)

# Example usage:
# results = await asyncio.gather(*(bounded_fetch(u) for u in urls))


# Q23. What’s the difference between asyncio and libraries like trio or curio?
# → asyncio is built-in and standardized; trio and curio offer cleaner structured concurrency and simpler cancellation semantics.

# Q24. What are some async frameworks in Python?
#
# aiohttp (HTTP client/server)
#
# FastAPI (web framework)
#
# Quart (async Flask clone)
#
# asyncpg (PostgreSQL driver)


# Q25. How do you debug asyncio code?

# Enable debug mode:

async def func_to_run_in_debug_mode():
    print("Running in debug mode")
    await asyncio.sleep(3)

def test_debug_mode():
    asyncio.run(func_to_run_in_debug_mode(), debug=True)

# Use loop.set_debug(True)
# Log slow callbacks with asyncio.get_running_loop().slow_callback_duration

# When do you use asyncio.run() vs loop.run_until_complete()?
# → Use asyncio.run() for top-level entry points; use loop.run_until_complete() when you need more control over the event loop.


