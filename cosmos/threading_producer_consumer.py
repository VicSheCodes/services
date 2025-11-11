# threading_producer_consumer.py
"""
Creates a producer-consumer pipeline with Queue
Multiple worker threads process jobs concurrently
Uses a Lock to protect a shared counter safely
"""

import threading
import time
from queue import Queue

def io_bound_task(x):
    # Simulate I/O latency
    time.sleep(0.1)
    return x * x

class Worker(threading.Thread):
    def __init__(self, q, counter, counter_lock):
        super().__init__(daemon=True)
        self.q = q
        self.counter = counter
        self.counter_lock = counter_lock

    def run(self):
        while True:
            item = self.q.get()
            if item is None:  # shutdown signal
                self.q.task_done()
                break
            result = io_bound_task(item)
            # Safely update shared counter
            with self.counter_lock:
                self.counter["processed"] += 1
            # In real code, write result to another queue or DB
            self.q.task_done()

def main():
    q = Queue(maxsize=100)
    counter = {"processed": 0}
    counter_lock = threading.Lock()

    workers = [Worker(q, counter, counter_lock) for _ in range(4)]
    for w in workers:
        w.start()

    # Produce jobs
    for i in range(100):
        q.put(i)

    # Signal shutdown
    for _ in workers:
        q.put(None)

    q.join()
    for w in workers:
        w.join()

    print("Processed:", counter["processed"])

if __name__ == "__main__":
    main()