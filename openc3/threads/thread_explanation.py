"""
What is a Thread? 🧵
A thread is a lightweight unit of execution within a process. Think of it as a "worker" that can run code
independently while sharing the same memory space with other threads.

In Python, a "thread" refers to a lightweight unit of execution within a program, managed by the threading module.
It allows for the concurrent execution of multiple tasks within the same process,
giving the illusion of simultaneous operations.

<hr></hr>
Key Concepts
1. Process vs Thread

Process (Your Python Program)
├── Memory Space (variables, objects)
├── Thread 1 (main thread) ──► Running your code
├── Thread 2 ──► Running other code
└── Thread 3 ──► Running other code
    ↑
    All threads share the same memory!

Process                         Thread
Independent program             Part of a process
Own memory space                Shares process memory
Heavy (slow to create)          Lightweight (fast to create)
Isolated (safe)                 Shared memory (risky!)

2. Why Use Threads?
Use threads for I/O-bound tasks (waiting for network, disk, database):
"""
import concurrent.futures
from threading import Thread

# Without threads (sequential):
def fetch_from_api_1():
    pass
def fetch_from_api_2():
    pass
def fetch_from_api_3():
    pass


data1 = fetch_from_api_1()  # Wait 2 seconds
data2 = fetch_from_api_2()  # Wait 2 seconds
data3 = fetch_from_api_3()  # Wait 2 seconds
# Total: 6 seconds

# With threads (parallel):
thread1 = Thread(target=fetch_from_api_1)
thread2 = Thread(target=fetch_from_api_2)
thread3 = Thread(target=fetch_from_api_3)
# Start all at once
# Total: ~2 seconds (they wait in parallel)

"""
Basic Thread Example
Creating and Running a Thread
"""

import threading
import time

def worker(name):
    """A simple task that runs in a thread"""
    print(f"Thread {name} starting")
    time.sleep(2)  # Simulate I/O wait
    print(f"Thread {name} finished")

# def test_worker():
#     # Create threads
#     thread1 = threading.Thread(target=worker, args=("A",))
#     thread2 = threading.Thread(target=worker, args=("B",))
#
#     # Start threads
#     thread1.start()
#     thread2.start()
#
#     # Wait for threads to finish
#     thread1.join()
#     thread2.join()
#
#     print("All threads completed")

"""
Key aspects of Python threading:
Concurrency vs. Parallelism: 
Due to the Global Interpreter Lock (GIL) in CPython (the standard implementation), Python threads do not achieve true 
parallelism for CPU-bound tasks (they cannot execute truly simultaneously on multiple cores). However, they are highly
effective for I/O-bound tasks, where threads can pause during I/O operations (like reading from disk or network 
requests) and allow other threads to run, improving overall program responsiveness.

Creating and Starting Threads: 
Threads are created using threading.Thread() and started with the .start() method. 
A target function is passed to the Thread constructor, defining the code the thread will execute.

Synchronization Primitives: 
The threading module provides various tools to manage shared resources and prevent race conditions between threads, including:
    Locks: (threading.Lock) To ensure only one thread can access a critical section of code at a time. 
    RLocks: (threading.RLock) Reentrant locks that can be acquired multiple times by the same thread. 
    Semaphores: (threading.Semaphore) To control access to a resource by limiting the number of concurrent users.
    Condition Variables: (threading.Condition) To allow threads to wait for specific conditions to become true before proceeding. 
    join() Method: The .join() method on a thread object is used to wait for that thread to complete its execution before the main program or another thread continues.
    Daemon Threads: Daemon threads are background threads that do not prevent the main program from exiting when they are still running. 
    They are useful for tasks that don't need to be explicitly waited for.
    

"""

import logging
import threading
import time

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

def thread_function(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(3)
    logging.info(f"Thread {name}: finishing")

# def test_thread_deamon():
#     logging.info("Main    : before creating thread")
#     # That line creates a `Thread` object configured to run a function in a separate thread, but it does not start the thread yet. `target` is the callable the thread will run; `args` is a tuple of positional arguments to pass to that callable when the thread starts.
#     #
#     # - `target=thread_function` means the thread will execute `thread_function(...)`.
#     # - `args=(1,)` means `thread_function` will be called as `thread_function(1)`. The trailing comma is required for a single-element tuple.
#     # - The thread runs only after `start()` is called; use `join()` to wait for it to finish.
#     #
#     # t = threading.Thread(target=thread_function, args=(1,))
#     # t.start()
#     # t.join()
#     x = threading.Thread(target = thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()    # runs thread_function(1) in a new thread
#     logging.info("Main    : wait for the thread to finish")
#     x.join()    # wait for the thread to finish , will wait even if it is daemon. comment out an see the difference with and without daemon parameter
#     logging.info("Main    : all done")
#
# def test_multiple_threads():
#     threads = list()
#     for index in range(3):
#         logging.info(f"Main    : create and start thread {index}")
#         x = threading.Thread(target = thread_function, args=(index,))
#         threads.append(x)   # adds the newly created threading.Thread instance x to the threads list. Can iterate it by order
#         x.start()
#
#     for index, thread in enumerate(threads):
#             logging.info(f"Main    : before joining {index}")
#             thread.join()
#             logging.info(f"Main    : thread {index} done")

# start up a group of threads
# The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool.
def thread_pool():
    print(f"\n thread_pool func  starts")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
    print(f"\n thread_pool func ended")


if __name__ == "__main__":
    print(f"\n main starts")
    thread_pool()
    print(f"\n main ended")
