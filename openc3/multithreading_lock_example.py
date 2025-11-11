import threading
import logging

NUM_CONSUMERS = 5
NUM_PRODUCERS = 5
MAX_ITEMS = 50

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class Queue:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def is_empty(self):
        logger.info("Queue is empty" if len(self.items) == 0 else "Queue is not empty")
        return len(self.items) == 0

    def is_full(self):
        logger.info("Queue is full" if len(self.items) >= MAX_ITEMS else "Queue is not full")
        return len(self.items) >= MAX_ITEMS

    def enqueue(self, item):
        with self.lock:
            logger.info("Acquired lock for enqueue operation")
            if len(self.items) < MAX_ITEMS:
                logger.info("Queue is not full")
                logger.info(f"Enqueuing item: {item}")
                self.items.append(item)
                logger.info(f"Item {item} enqueued successfully. Current queue size: {len(self.items)}")
            else:
                raise Exception ("Queue is full")

    def dequeue(self):
        with self.lock:
            logger.info("Acquired lock for dequeue operation")
            if not len(self.items) == 0:
                logger.info("Queue is not empty")
                item = self.items.pop(0)
                logger.info(f"{item} dequeued successfully. Current queue size: {len(self.items)}")
                return item
            else:
                raise Exception("Queue is empty")

class Producer:
    def __init__(self, queue):
        self.queue = queue

    def producer(self):
        for i in range(MAX_ITEMS):
            try:
                self.queue.enqueue(i)
                logger.info(f"Produced item: {i}\n")
            except Exception as e:
                logger.error(f"Producer error: {e}")
                continue

class Consumer:
    def __init__(self, queue):
        self.queue = queue

    def consumer(self):
        for _ in range(MAX_ITEMS):
            try:
                item = self.queue.dequeue()
                logger.info(f"Consumed item: {item}\n")
            except Exception as e:
                logger.error(f"Consumer error: {e}")
                continue

def test_multithreading_lock_example():
    queue = Queue()
    P = Producer(queue)
    C = Consumer(queue)

    threads = []
    for _ in range(NUM_PRODUCERS):
        t = threading.Thread(target=P.producer)
        threads.append(t)
        t.start()

    for _ in range(NUM_CONSUMERS):
        t = threading.Thread(target=C.consumer)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for i in queue.items:
        logger.info(f"{i}=")

    assert queue.is_empty(), "Queue should be empty after all items are consumed"