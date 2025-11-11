"""
Example 3: Real Web Scraper
Compare threading vs asyncio performance
"""
import asyncio
import time
import threading
import queue
import aiohttp  # pip install aiohttp
import requests  # pip install requests


# ========== THREADING VERSION ==========
def download_url_sync(url: str) -> str:
    """Download URL synchronously (blocks thread)"""
    response = requests.get(url, timeout=5)
    return response.text[:100]  # First 100 chars


def scraper_threading(urls: list[str]):
    """Threading-based scraper"""
    print("\n" + "=" * 60)
    print("THREADING VERSION")
    print("=" * 60)

    url_queue = queue.Queue()
    results = []
    results_lock = threading.Lock()

    # Producer: Add URLs to queue
    for url in urls:
        url_queue.put(url)

    # Consumer: Download URLs
    def worker():
        while True:
            try:
                url = url_queue.get(timeout=1)
                print(f"[Thread {threading.current_thread().name}] Downloading {url}")
                content = download_url_sync(url)
                with results_lock:
                    results.append((url, content))
                url_queue.task_done()
            except queue.Empty:
                break

    # Create 5 worker threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, name=f"Worker-{i}")
        t.start()
        threads.append(t)

    # Wait for completion
    for t in threads:
        t.join()

    return results


# ========== ASYNCIO VERSION ==========
async def download_url_async(session: aiohttp.ClientSession, url: str) -> str:
    """Download URL asynchronously (yields control)"""
    async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
        text = await response.text()
        return text[:100]


async def scraper_asyncio(urls: list[str]):
    """AsyncIO-based scraper"""
    print("\n" + "=" * 60)
    print("ASYNCIO VERSION")
    print("=" * 60)

    results = []

    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            print(f"[Task] Downloading {url}")
            # Create task for each URL
            task = download_url_async(session, url)
            tasks.append(task)

        # Run all downloads concurrently
        contents = await asyncio.gather(*tasks, return_exceptions=True)

        for url, content in zip(urls, contents):
            if isinstance(content, Exception):
                print(f"[Error] {url}: {content}")
            else:
                results.append((url, content))

    return results


# ========== BENCHMARK ==========
def benchmark():
    """Compare performance"""
    urls = [
        "https://httpbin.org/delay/1",  # Simulates 1s delay
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]

    # Test threading
    start = time.time()
    results_threading = scraper_threading(urls)
    time_threading = time.time() - start

    # Test asyncio
    start = time.time()
    results_asyncio = asyncio.run(scraper_asyncio(urls))
    time_asyncio = time.time() - start

    # Results
    print("\n" + "=" * 60)
    print("BENCHMARK RESULTS")
    print("=" * 60)
    print(f"Threading: {len(results_threading)} pages in {time_threading:.2f}s")
    print(f"AsyncIO:   {len(results_asyncio)} pages in {time_asyncio:.2f}s")
    print(f"\nAsyncIO is {time_threading / time_asyncio:.1f}x faster! ⚡")


if __name__ == "__main__":
    benchmark()