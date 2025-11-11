"""

Practice Exercises — Iterators, Generators, Exceptions, Context Managers
Here are exercises that combine everything you've learned. Start with Level 1, then progress through harder levels.
<hr></hr>
Level 1: Basics
Exercise 1.1: Safe File Reader (Context Manager + Exceptions)
Create a context manager that safely reads a file and handles errors gracefully.
class SafeFileReader:

    Context manager that:
    - Opens a file
    - Returns None if file doesn't exist (don't raise)
    - Always closes the file
    - Logs any errors that occur

    def __init__(self, filename):
        pass  # Your code here

    def __enter__(self):
        pass  # Your code here

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # Your code here

# Test it:
with SafeFileReader('data.txt') as file:
    if file:
        print(file.read()

Should handle missing file gracefull
Requirements:
Use try/except inside __enter__
Always close file in __exit__
Return None if file not found
Don't let exceptions propagate
<hr></hr>
Exercise 1.2: Number Generator (Generators + Exceptions)
Create a generator that yields even numbers but stops on invalid input.
def safe_even_numbers(max_num):

    Generate even numbers from 0 to max_num.
    Raise ValueError if max_num is negative.
    Raise TypeError if max_num is not an integer.

    pass  # Your code here

# Test cases:
# Should work:
for num in safe_even_numbers(10):
    print(num)  # 0, 2, 4, 6, 8, 10

# Should raise ValueError:
try:
    for num in safe_even_numbers(-5):
        print(num)
except ValueError as e:
    print(f"Caught: {e}")

# Should raise TypeError:
try:
    for num in safe_even_numbers("10"):
        print(num)
except TypeError as e:
    print(f"Caught: {e}")
<hr></hr>
Exercise 1.3: Retry Iterator (Iterator + Exceptions)
Create an iterator that retries failed operations.
class RetryIterator:

    Iterator that attempts to call a function multiple times.
    Yields the result on success.
    Raises the last exception after max_retries.

    def __init__(self, func, max_retries=3):
        pass  # Your code here

    def __iter__(self):
        pass  # Your code here

    def __next__(self):
        pass  # Your code here

# Test with a flaky function:
import random

def flaky_operation():
    if random.random() < 0.7:  # 70% fail rate
        raise ConnectionError("Network error")
    return "Success!"

# Should retry and eventually succeed or fail after 3 attempts:
try:
    for result in RetryIterator(flaky_operation, max_retries=5):
        print(result)
        break  # Stop after first success
except ConnectionError as e:
    print(f"Failed after retries: {e}")
<hr></hr>
Level 2: Intermediate
Exercise 2.1: Database Connection Manager (Context Manager + Nested Exceptions)
Create a context manager for database connections that handles errors at different levels.
class DatabaseConnection:

    Context manager that:
    - Connects to a database
    - Handles connection errors gracefully
    - Rolls back on query errors
    - Always closes connection
    - Logs all errors

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction_active = False

    def __enter__(self):

        Connect to database.
        If connection fails, raise ConnectionError.

        pass  # Your code here

    def __exit__(self, exc_type, exc_val, exc_tb):

        If exception occurred during queries:
        - Rollback if transaction active
        - Log the error
        - Don't suppress the exception

        Always:
        - Close connection

        pass  # Your code here

    def execute(self, query):

        Execute a query.
        Start transaction if not active.

        pass  # Your code here

# Mock database for testing:
class MockDB:
    def __init__(self, fail_on_connect=False):
        self.fail_on_connect = fail_on_connect
        self.closed = False
        self.transaction_active = False

    def connect(self, connection_string):
        if self.fail_on_connect:
            raise ConnectionError("Failed to connect")
        return self

    def execute(self, query):
        if "FAIL" in query:
            raise ValueError("Query error")
        return "Success"

    def rollback(self):
        self.transaction_active = False
        print("Transaction rolled back")

    def close(self):
        self.closed = True
        print("Connection closed")

# Test it:
try:
    with DatabaseConnection("localhost:5432") as db:
        db.execute("SELECT * FROM users")
        db.execute("UPDATE users SET name = 'FAIL'")  # This should rollback
except ValueError:
    print("Query failed, but connection was cleaned up")
<hr></hr>
Exercise 2.2: Line-by-Line File Processor (Generator + Multiple Exceptions)
Create a generator that processes file lines and handles different errors per line.
def process_json_lines(filename):

    Generator that:
    - Reads a file line-by-line
    - Parses each line as JSON
    - Yields parsed objects
    - Skips invalid JSON lines (logs error)
    - Raises FileNotFoundError if file missing
    - Always closes file

    pass  # Your code here

# Test file content (create test.jsonl):
# {"name": "Alice", "age": 30}
# {"invalid json
# {"name": "Bob", "age": 25}

# Test:
for obj in process_json_lines('test.jsonl'):
    print(obj)
# Should print Alice and Bob, skip invalid line
<hr></hr>
Exercise 2.3: Resource Pool Manager (Context Manager + Iterator)
Create a context manager that manages a pool of resources.
class ResourcePool:

    Context manager + Iterator that:
    - Manages a pool of resources (e.g., connections)
    - Acquires a resource on __enter__
    - Releases it on __exit__
    - Iterates over available resources
    - Handles resource exhaustion

    def __init__(self, max_size=3):
        self.max_size = max_size
        self.available = list(range(max_size))  # Simulated resources
        self.in_use = set()

    def acquire(self):

        Get a resource from the pool.
        Raise ResourceError if pool is exhausted.

        pass  # Your code here

    def release(self, resource):

        Return a resource to the pool.

        pass  # Your code here

    def __enter__(self):
        pass  # Your code here

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # Your code here

    def __iter__(self):
        Iterate over available resources
        pass  # Your code here

class ResourceError(Exception):
    pass

# Test:
pool = ResourcePool(max_size=2)

try:
    with pool as res1:
        print(f"Acquired {res1}")
        with pool as res2:
            print(f"Acquired {res2}")
            with pool as res3:  # Should fail
                print(f"Acquired {res3}")
except ResourceError:
    print("Pool exhausted!")
<hr></hr>
Level 3: Advanced (Mimicking Your Real Code)
Exercise 3.1: State Machine Executor (Everything Combined)
Create a state machine executor similar to your on_fail() method.
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class ExecutorState:
    IDLE = 'idle'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'

class ServiceExecutor:

    State machine that:

"""
from contextlib import contextmanager


class SafeFileReader:

    def __init__(self, filename):
        self.file_name = filename
        self.file = None

    def __enter__(self):
        try:
            print(f"Opening file {self.file_name} for reading.")
            self.file = open(self.file_name, 'r')
            return self.file
        except FileNotFoundError:
            print(f"File not found")
            return None
        except Exception as e:
            print(f"Error opening file {e}")
            return None

    def __exit__(self,exc_type, exc_val, exc_tb):
        try:
            if self.file and not self.file.closed:
                print(f"Closing file {self.file_name} after reading")
                self.file.close()
        except Exception as e:
            print(f"Error closing file {self.file_name}: {e}")
            # Suppress exceptions so they don't propagate
        return True


@contextmanager
def open_files(filename, mode='r'):
    if not isinstance(mode, str):
        raise TypeError("mode must be a string")
    action = 'reading' if 'r' in mode and 'w' not in mode and 'a' not in mode else 'writing'
    print(f"Opening {filename} for {action}")
    file = None
    try:
        file = open(filename, mode)
        yield file
    except FileNotFoundError:
        print(f"File not found: {filename}")
        raise
    except Exception as e:
        print(f"Error opening file {filename}: {e}")
        raise
    finally:
        if file is not None:
            try:
                file.close()
                print(f"File closed {filename}")
            except Exception as e:
                print(f"Error closing file {filename}: {e}")



if __name__ == '__main__':
    try:
        with SafeFileReader('text_file.txt') as f:
            if f:
                print(f.read())
    except Exception as e:
        print("Error reading the file")

    try:
        with open_files('text_file.txt2', 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"{e}")
