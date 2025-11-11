"""
Example 2: Producer-Consumer with AsyncIO
Compare to your threading version
"""
import asyncio
import random
from typing import List


# ========== THREADING VERSION (Your Current Code) ==========
def threading_version_summary():
    """
    Your threading version:
    - Uses queue.Queue (thread-safe)
    - Producers/consumers are threads
    - OS manages thread switching
    - Can have race conditions without locks
    """
    print("""
    Threading Version:
    ┌─────────────┐
    │ Producer 1  │──┐
    │ (Thread)    │  │
    └─────────────┘  │
                     ├──► queue.Queue ──► ┌─────────────┐
    ┌─────────────┐  │                    │ Consumer 1  │
    │ Producer 2  │──┘                    │ (Thread)    │
    │ (Thread)    │                       └─────────────┘
    └─────────────┘
    
    - Blocking: queue.get(timeout=2)
    - Thread-safe: queue handles locks
    """)


# ========== ASYNCIO VERSION (Better!) ==========
async def producer_async(name: str, queue: asyncio.Queue, num_items: int):
    """Async producer - yields control while 'working'"""
    for i in range(num_items):
        item = f"Item-{name}-{i}"
        print(f"[Producer {name}] Creating {item}")

        # Simulate finding URLs (async I/O)
        await asyncio.sleep(random.uniform(0.1, 0.3))

        # Put item in queue (async operation)
        await queue.put(item)

    print(f"[Producer {name}] ✅ Finished")


async def consumer_async(name: str, queue: asyncio.Queue):
    """Async consumer - yields control while waiting"""
    while True:
        try:
            # Wait for item (with timeout)
            item = await asyncio.wait_for(queue.get(), timeout=2.0)

            print(f"[Consumer {name}] Processing {item}")

            # Simulate processing (async I/O)
            await asyncio.sleep(random.uniform(0.5, 1.0))

            # Mark task as done
            queue.task_done()

            print(f"[Consumer {name}] ✅ Done with {item}")

        except asyncio.TimeoutError:
            print(f"[Consumer {name}] No more items, exiting")
            break


async def main_async():
    """Run async producer-consumer"""
    print("\n" + "=" * 60)
    print("ASYNCIO VERSION: Producer-Consumer")
    print("=" * 60)

    # Create async queue
    queue = asyncio.Queue(maxsize=10)

    # Create producer tasks
    producers = [
        producer_async("A", queue, num_items=5),
        producer_async("B", queue, num_items=5),
    ]

    # Create consumer tasks
    consumers = [
        consumer_async("1", queue),
        consumer_async("2", queue),
        consumer_async("3", queue),
    ]

    # Run producers and consumers concurrently
    await asyncio.gather(
        *producers,  # Run all producers
        *consumers,  # Run all consumers
    )

    print("\n[Main] All tasks completed!")


if __name__ == "__main__":
    # Show threading version summary
    threading_version_summary()

    # Run async version
    asyncio.run(main_async())