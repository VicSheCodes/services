"""
AsyncIO is Python's way to write concurrent code using async/await syntax instead of threads. 
It's perfect for I/O-bound tasks (like  web scraper) but uses a single thread
with cooperative multitasking.

Threading vs AsyncIO: The Key Difference
Threading

OS manages threads:
Thread 1 ────┐
Thread 2 ────┼──► OS Scheduler decides who runs
Thread 3 ────┘     (preemptive multitasking)

Each thread can be interrupted at any time!

AsyncIO
Single thread, tasks cooperate:
Task 1 ──► yield control ──► Task 2 ──► yield control ──► Task 3
    ↑                            ↑                           ↑
    Explicitly gives up CPU     Explicitly gives up CPU    ...
    (cooperative multitasking)
    
Key difference:
Threads: OS decides when to switch (can happen anytime = race conditions!)
AsyncIO: You decide when to switch (using await = no race conditions!)

Async I/O is a single-threaded, single-process technique that uses cooperative multitasking.
Async I/O gives a feeling of concurrency despite using a single thread in a single process.
Coroutines—or coro for short—are a central feature of async I/O and can be scheduled concurrently,
but they’re not inherently concurrent.


What does it mean for something to be asynchronous? you can think of two key properties:

Asynchronous routines can pause their execution while waiting for a result and allow other routines
to run in the meantime.
Asynchronous code facilitates the concurrent execution of tasks by coordinating asynchronous routines.

"""
import asyncio
import time

import aiohttp


# Each thread blocks while waiting for network
def download_page_1(url, requests=None):
    response = requests.get(url)  # ← Blocks thread for 1 second
    return response.text

# With 3 threads downloading 3 pages:
# Thread 1: Wait... (1s)
# Thread 2: Wait... (1s)
# Thread 3: Wait... (1s)
# Total: ~1 second (good!)
# Resources: 3 threads, 3 OS context switches

# AsyncIO Version (Better!)
# Single thread handles all I/O
async def download_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:  # ← Yields control
            return await response.text()

# With 3 tasks downloading 3 pages:
# Task 1: Start download → yield
# Task 2: Start download → yield
# Task 3: Start download → yield
# (all downloads happen in parallel in 1 thread!)
# Total: ~1 second (same speed!)
# Resources: 1 thread, no context switches (faster!)


# Regular function (blocking)
def regular_function():
    time.sleep(1)  # ← Blocks entire thread
    return "Done"

# Async function (non-blocking)
async def async_function():
    await asyncio.sleep(1)  # ← Yields control to other tasks
    return "Done"

# Await (Cooperative Yielding)
async def task_a():
    print("A: Starting")
    await asyncio.sleep(1)  # ← "Hey event loop, I'm waiting. Run other tasks!"
    print("A: Done")

async def task_b():
    print("B: Starting")
    await asyncio.sleep(1)  # ← "Hey event loop, I'm waiting. Run other tasks!"
    print("B: Done")

# Run both
# asyncio.run(asyncio.gather(task_a(), task_b()))

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

"""
Event Loop:
1. Check which tasks are waiting for I/O
2. Switch to tasks that are ready
3. Repeat until all tasks complete
"""
if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())       #  The event loop manages all tasks
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")