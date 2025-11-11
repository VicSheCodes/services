"""

Pattern 1: asyncio.gather() - Run Multiple Tasks
"""
import asyncio
import time


async def task1():
    # Simulate an I/O-bound operation
    await asyncio.sleep(1)
    return 'result1'

async def task2():
    # Simulate another I/O-bound operation
    await asyncio.sleep(2)
    return 'result2'

async def task3():
    # Simulate yet another I/O-bound operation
    await asyncio.sleep(1.5)
    return 'result3'

async def main1():
    # Run tasks concurrently
    start = time.time()
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
    )
    print(results)  # [result1, result2, result3]
    elapsed = time.time() - start
    print(f"All tasks completed in {elapsed:.2f} seconds")

def test_gather():
    asyncio.run(main1())

"""
Pattern 2: asyncio.create_task() - Fire and Forget
"""

async def background_job():
    print(f"Background job started. {time.ctime()}")
    await asyncio.sleep(3)
    print(f"Background job finished. {time.ctime()}")

async def do_something_else():
    print(f"\nDoing something else... {time.ctime()}")
    await asyncio.sleep(2)
    print(f"Done with something else. {time.ctime()}")

async def main2():
    start = time.time()
    # Start task in background
    print("\nStart task in background")
    task = asyncio.create_task(background_job())    # Create a task from coroutine

    # Do other work
    await do_something_else()

    # Wait for background task
    await task

    elapsed = time.time() - start
    print(f"All tasks completed in {elapsed:.2f} seconds")

def test_create_task():
    asyncio.run(main2())

"""
Pattern 3: asyncio.wait_for() - Timeout
"""
async def slow_operation():
    await asyncio.sleep(6)  # Simulate a slow operation
    return "Finished"

async def main3():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=5.0)
    except asyncio.TimeoutError:
        print(f"\nTook too long!")

def test_wait_for():
    asyncio.run(main3())


"""
Pattern 4: asyncio.Queue - Producer-Consumer
"""

item = "data_item"

async def producer(queue):
    print("Producing item...")
    await queue.put(item)

async def consumer(queue):
    print("Consuming item...")
    item = await queue.get()
    queue.task_done()

def main4():
    print("\nUsing asyncio.Queue for producer-consumer pattern")
    queue = asyncio.Queue()

    async def run():
        print("Starting producer and consumer tasks")
        await asyncio.gather(
            producer(queue),
            consumer(queue),
        )

    print("Running event loop")
    asyncio.run(run())

def test_queue():
    main4()