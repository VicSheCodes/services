import asyncio

#  generator version
def even_numbers(start, end):
    if start % 2 != 0:
        start += 1
    while start <= end:
        yield start  # Pause and return value
        start += 2

# Async version (pretend fetching data takes time)
async def fetch_even_numbers(start, end):
    if start % 2 != 0:
        start += 1

    results = []
    while start <= end:
        await asyncio.sleep(0.1)  # Simulate slow operation
        results.append(start)
        start += 2

    return results

# Running it
async def main():
    numbers = await fetch_even_numbers(1, 10)
    print(numbers)  # [2, 4, 6, 8, 10]

if __name__ == '__main__':
    asyncio.run(main())