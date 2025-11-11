"""
The Producer-Consumer problem is a classic threading scenario where:
Producers create data
Consumers process that data
They share a queue to pass data between them

Queue handles thread safety automatically!

Producer Thread 1 ──┐
Producer Thread 2 ──┼──► Queue ──► Consumer Thread 1 ──┐
Producer Thread 3 ──┘             Consumer Thread 2 ──┼──► Results
                                  Consumer Thread 3 ──┘

Flow:
Producers create tasks and put them in the queue
Queue safely stores tasks (thread-safe!)
Consumers take tasks from the queue and process them

Real-World Examples:
Scenario            Producer            Queue            Consumer
Web Scraper         Finds URLs          URL queue        Downloads pages
Image Processor     Reads files         Image queue      Applies filters
Log Analyzer        Reads log lines     Line queue       Parses and stores
Task Worker         API requests        Task queue       Processes requests
"""


"""
Producer-Consumer Pattern with Queue

queue.Queue() is Thread-Safe 
 
task_queue = queue.Queue()

# No locks needed! Queue handles it internally
task_queue.put(item)   # Thread-safe add
item = task_queue.get()  # Thread-safe remove
 
"""
import threading
import queue
import time
import random


def producer(name, task_queue, num_tasks):
    """
    Producer creates tasks and adds them to the queue.
    """
    for i in range(num_tasks):
        task = f"Task-{name}-{i}"
        print(f"Producer {name}: Creating {task}")
        task_queue.put(task)  # ← Thread-safe! No lock needed
        time.sleep(random.uniform(0.1, 0.5))  # Simulate work

    print(f"Producer {name}: Finished")


def consumer(name, task_queue):
    """
    Consumer takes tasks from queue and processes them.
    """
    while True:
        try:
            # Get task (wait up to 1 second)
            task = task_queue.get(timeout=1)
            print(f"Consumer {name}: Processing {task}")
            time.sleep(random.uniform(0.5, 1.0))  # Simulate processing
            task_queue.task_done()  # ← Signal task is complete
        except queue.Empty:
            # No more tasks
            print(f"Consumer {name}: Queue empty, exiting")
            break


if __name__ == "__main__":
    # Create a shared queue
    task_queue = queue.Queue(maxsize=5)  # Max 5 items in queue

    # Create producer threads
    producers = [
        threading.Thread(target=producer, args=("P1", task_queue, 3)),
        threading.Thread(target=producer, args=("P2", task_queue, 3)),
    ]

    # Create consumer threads
    consumers = [
        threading.Thread(target=consumer, args=("C1", task_queue)),
        threading.Thread(target=consumer, args=("C2", task_queue)),
    ]

    # Start all threads
    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    # Wait for producers to finish
    for p in producers:
        p.join()

    # Wait for queue to be empty
    task_queue.join()  # ← Waits for all tasks to be marked done

    print("All tasks completed!")