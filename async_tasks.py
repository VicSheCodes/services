import asyncio

async def do_something(x, delay):
    print(f"Starting task {x}")
    await asyncio.sleep(delay)
    print(f"Finished task {x}")


async def main():

    # 1. Using asyncio.gather to run multiple coroutines concurrently
    tasks = [
        do_something(1, 2),
        do_something(2, 1),
        do_something(3, 3),
    ]
    await asyncio.gather(*tasks)

    # 2. Creating and managing a single task explicitly
    task = asyncio.create_task(do_something(4, 2))
    await task

    # 3. Looping to create multiple tasks dynamically
    more_tasks = []
    for i in range(5, 8):
        more_tasks.append(asyncio.create_task(do_something(i, i - 4)))
    await asyncio.gather(*more_tasks)

if __name__ == "__main__":
    asyncio.run(main())

