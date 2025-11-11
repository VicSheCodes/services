"""
Example 1: AsyncIO Basics
Compare sync vs async
"""
import asyncio
import time


# ========== SYNCHRONOUS (BLOCKING) ==========
def sync_task(name, delay):
    """Regular function - blocks"""
    print(f"[Sync {name}] Starting (delay={delay}s)")
    time.sleep(delay)  # ← Blocks entire program
    print(f"[Sync {name}] Finished")
    return f"Result from {name}"


def run_sync_tasks():
    """Run tasks sequentially"""
    print("\n" + "=" * 50)
    print("SYNCHRONOUS (Sequential)")
    print("=" * 50)
    start = time.time()

    # Each task blocks until complete
    sync_task("A", 1)
    sync_task("B", 1)
    sync_task("C", 1)

    elapsed = time.time() - start
    print(f"\nTotal time: {elapsed:.2f}s")  # ← ~3 seconds


# ========== ASYNCHRONOUS (NON-BLOCKING) ==========
async def async_task(name, delay):
    """Async function - yields control"""
    print(f"[Async {name}] Starting (delay={delay}s)")
    await asyncio.sleep(delay)  # ← Yields to other tasks
    print(f"[Async {name}] Finished")
    return f"Result from {name}"


async def run_async_tasks():
    """Run tasks concurrently"""
    print("\n" + "=" * 50)
    print("ASYNCHRONOUS (Concurrent)")
    print("=" * 50)
    start = time.time()

    # All tasks run concurrently
    results = await asyncio.gather(
        async_task("A", 1),
        async_task("B", 1),
        async_task("C", 1),
    )

    elapsed = time.time() - start
    print(f"\nResults: {results}")
    print(f"Total time: {elapsed:.2f}s")  # ← ~1 second


if __name__ == "__main__":
    # Run sync version
    run_sync_tasks()

    # Run async version
    asyncio.run(run_async_tasks())