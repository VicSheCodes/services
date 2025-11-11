"""
Example 4: Complete AsyncIO Producer-Consumer Web Scraper
"""
import asyncio
import aiohttp
from typing import List


class AsyncURLProducer:
    """Async producer that finds URLs"""

    def __init__(self, name: str, url_queue: asyncio.Queue, num_urls: int):
        self.name = name
        self.url_queue = url_queue
        self.num_urls = num_urls

    async def run(self):
        """Generate URLs and add to queue"""
        for i in range(self.num_urls):
            url = f"https://httpbin.org/delay/{i % 3}"  # Real URLs!
            print(f"[Producer {self.name}] Found URL: {url}")

            await self.url_queue.put(url)
            await asyncio.sleep(0.1)  # Simulate search time

        print(f"[Producer {self.name}] ✅ Finished")


class AsyncPageConsumer:
    """Async consumer that downloads pages"""

    def __init__(self, name: str, url_queue: asyncio.Queue):
        self.name = name
        self.url_queue = url_queue

    async def run(self):
        """Download pages from queue"""
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    # Get URL from queue (timeout 2s)
                    url = await asyncio.wait_for(
                        self.url_queue.get(),
                        timeout=2.0
                    )

                    print(f"[Consumer {self.name}] Downloading: {url}")

                    # Download page (async!)
                    async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                        content = await response.text()
                        print(f"[Consumer {self.name}] ✅ Downloaded {len(content)} bytes from {url}")

                    # Mark task as done
                    self.url_queue.task_done()

                except asyncio.TimeoutError:
                    print(f"[Consumer {self.name}] No more URLs, exiting")
                    break
                except Exception as e:
                    print(f"[Consumer {self.name}] ❌ Error: {e}")
                    self.url_queue.task_done()


async def main():
    """Run async producer-consumer"""
    print("=" * 60)
    print("AsyncIO Producer-Consumer Web Scraper")
    print("=" * 60)

    # Create async queue
    url_queue = asyncio.Queue(maxsize=10)

    # Create producers
    producers = [
        AsyncURLProducer("A", url_queue, num_urls=3),
        AsyncURLProducer("B", url_queue, num_urls=3),
    ]

    # Create consumers
    consumers = [
        AsyncPageConsumer("1", url_queue),
        AsyncPageConsumer("2", url_queue),
    ]

    # Run all tasks concurrently
    producer_tasks = [p.run() for p in producers]
    consumer_tasks = [c.run() for c in consumers]

    # Wait for all producers to finish
    await asyncio.gather(*producer_tasks)
    print("\n[Main] All producers finished")

    # Wait for queue to be empty
    await url_queue.join()
    print("[Main] All URLs processed")

    # Cancel consumers (they're waiting for more URLs)
    for task in asyncio.all_tasks():
        if task != asyncio.current_task():
            task.cancel()

    print("[Main] ✅ All tasks completed!")


if __name__ == "__main__":
    asyncio.run(main())