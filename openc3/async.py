"""
Generators: functions using yield to produce items lazily. Good for streaming and batching.
Exceptions: try/except to catch errors; raise ValueError for bad inputs.
Context managers: with ensures resources (like file handles) are cleaned up. Custom managers implement __enter__ / __exit__ or use contextlib.
"""

# python
from contextlib import contextmanager
from typing import Iterable, Iterator, List, TypeVar

T = TypeVar("T")

def batch(iterable: Iterable[T], n: int) -> Iterator[List[T]]:
    """
    Yield successive batches of size n from iterable.
    Raises ValueError for invalid batch size.
    """
    if n <= 0:
        raise ValueError("batch size must be > 0")
    batch_list: List[T] = []
    for item in iterable:
        batch_list.append(item)
        if len(batch_list) == n:
            yield batch_list
            batch_list = []
    if batch_list:
        yield batch_list  # leftover smaller batch

# Example usage of batch + exceptions
data = range(1, 11)  # 1..10

try:
    for b in batch(data, 3):
        print("Batch:", b)
except ValueError as e:
    print("Bad input:", e)

# Built-in context manager for files: safe and simple
with open("data.txt", "w", encoding="utf-8") as f:
    for b in batch(range(1, 8), 3):
        f.write(", ".join(map(str, b)) + "\n")

# Custom context manager (class form) that wraps a file handle
class FileWriter:
    def __init__(self, path: str, mode: str = "w", encoding: str = "utf-8"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding=self.encoding)
        return self.file  # usable as the file handle inside `with`

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
        # return False -> propagate exceptions (usually desired)
        return False

# Using the custom context manager to append batches
with FileWriter("data.txt", "a") as f:
    for b in batch(range(8, 13), 4):
        f.write("APPEND: " + ", ".join(map(str, b)) + "\n")

# Alternative: contextlib decorator form (shorter)
@contextmanager
def open_file(path: str, mode: str = "r", encoding: str = "utf-8"):
    f = open(path, mode, encoding=encoding)
    try:
        yield f
    finally:
        f.close()

with open_file("data.txt", "r") as f:
    print("\nContents of `data.txt`:")
    print(f.read())