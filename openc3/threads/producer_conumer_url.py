"""
Producer-Consumer Problem

Scenario: Web scraper
- Producers: Find URLs to scrape
- Consumers: Download and process pages

Day 2: Threading - Producer-Consumer Pattern
"""
import threading
import queue
import time
import random


class URLProducer:
    """Simulates finding URLs to scrape"""

    def __init__(self, name, url_queue, num_urls):
        self.name = name
        self.url_queue = url_queue
        self.num_urls = num_urls

    def run(self):
        """Generate URLs and add to queue"""
        for i in range(self.num_urls):
            url = f"https://example.com/page-{self.name}-{i}"
            print(f"[Producer {self.name}] Found URL: {url}")
            self.url_queue.put(url)
            time.sleep(random.uniform(0.1, 0.3))  # Simulate search time

        print(f"[Producer {self.name}] Finished finding URLs")


class PageConsumer:
    """Simulates downloading and processing pages"""

    def __init__(self, name, url_queue):
        self.name = name
        self.url_queue = url_queue

    def run(self):
        """Process URLs from queue"""
        while True:
            try:
                # Get URL from queue (wait up to 2 seconds)
                url = self.url_queue.get(timeout=2)
                print(f"[Consumer {self.name}] Downloading: {url}")
                time.sleep(random.uniform(0.5, 1.0))  # Simulate download
                print(f"[Consumer {self.name}] Processed: {url}")
                self.url_queue.task_done()

            except queue.Empty:
                print(f"[Consumer {self.name}] No more URLs, exiting")
                break


def main():
    """Run producer-consumer simulation"""
    print("=" * 60)
    print("Producer-Consumer: Web Scraper Simulation")
    print("=" * 60)

    # Create shared queue
    url_queue = queue.Queue(maxsize=10)  # Buffer max 10 URLs

    # Create producers (2 threads finding URLs)
    producers = [
        URLProducer("A", url_queue, num_urls=5),
        URLProducer("B", url_queue, num_urls=5),
    ]

    # Create consumers (3 threads downloading pages)
    consumers = [
        PageConsumer("1", url_queue),
        PageConsumer("2", url_queue),
        PageConsumer("3", url_queue),
    ]

    # Start producer threads
    producer_threads = []
    for producer in producers:
        t = threading.Thread(target=producer.run)
        t.start()
        producer_threads.append(t)

    # Start consumer threads
    consumer_threads = []
    for consumer in consumers:
        t = threading.Thread(target=consumer.run)
        t.start()
        consumer_threads.append(t)

    # Wait for producers to finish
    for t in producer_threads:
        t.join()

    print("\n[Main] All producers finished. Waiting for consumers...")

    # Wait for all tasks to be processed
    url_queue.join()

    print("\n[Main] All tasks completed!")

    # Wait for consumer threads to exit
    for t in consumer_threads:
        t.join()

    print("\n[Main] All threads finished.")


if __name__ == "__main__":
    main()