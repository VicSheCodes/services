import asyncio

async def do_something(x, delay):
    print(f"Starting task {x}")
    await asyncio.sleep(delay)
    print(f"Finished task {x}")

async def main():
    tasks = [
        do_something(1, 2),
        do_something(2, 1),
        do_something(3, 3),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
