"""
Race conditions can occur when two or more threads access a shared piece of data or resource.
In this example, you’re going to create a large race condition that happens every time,
but be aware that most race conditions are not this obvious. This race condition will happen every time,
and you’ll walk through it in detail to explain what is happening.

 write a class that updates a fake database.
"""
import threading
import time
import concurrent.futures


class FakeDatabaseBroken:
    def __init__(self):
        self.value = 0

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        time.sleep(0.001)  # Shorter sleep to run faster
        self.value = local_copy

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        """
        Simulates a database update with a race condition.

        Race condition happens because:
        1. Thread reads value
        2. Thread increments local copy
        3. Thread sleeps (other thread can read old value!)
        4. Thread writes back
        """
        print(f"\nThread {name}: starting update")
        print(f"\nThread {name} about to lock")
        with self._lock:
            local_copy = self.value  # ← Read shared data
            local_copy += 1
            time.sleep(0.01)  # ← Other threads can read old value during this sleep!
            self.value = local_copy  # ← Write back (overwrites other thread's work!)
            print(f"\nThread {name} about to release lock")

        print(f"\nThread {name} after  release lock")
        print(f"\nThread {name}: finishing update")


def test_database(db_class, num_threads=10):
    """Test database with multiple threads"""
    db = db_class()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            executor.submit(db.update, f"thread_{i}")

    return db.value

def test_runner():
    print("Testing broken version (10 threads)...")
    for run in range(5):
        result = test_database(FakeDatabaseBroken, num_threads=10)
        print(f"  Run {run + 1}: Expected 10, Got {result} {'❌' if result != 10 else '✅'}")

    print("\nTesting fixed version (10 threads)...")
    for run in range(5):
        result = test_database(FakeDatabase, num_threads=10)
        print(f"  Run {run + 1}: Expected 10, Got {result} {'✅' if result == 10 else '❌'}")


if __name__ == "__main__":

    database = FakeDatabase()
    print(f"\nTesting update. Starting value is {database.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, f"thread_num_{index}")

    print(f"\nTesting update. Ending value is {database.value}")