"""
 Create a context manager that writes to a file and prints when opening/closing.

What @contextmanager Does vs. Doesn't Do
❌ What it does NOT do:
@contextmanager does NOT automatically close your resources. It doesn't know what cleanup you need!
✅ What it DOES do:
@contextmanager automatically creates __enter__ and __exit__ methods that:
Run code before yield when entering with
Run code after yield when exiting with
But YOU must tell it what cleanup to do!

@contextmanager saves you from writing __enter__ and __exit__ methods,
but the cleanup logic inside them is YOURS to write.

❌ WITHOUT with — You MUST close manually:
file = open(filename, mode)  # ← Opens but doesn't auto-close!
# ...use file...
file.close()  # ← YOU must close it!
✅ WITH with — Closes automatically:
with open(filename, mode) as file:  # ← Opens AND auto-closes
    # ...use file...
# Automatically closes when exiting 'with' block

"""
from contextlib import contextmanager

# @contextmanager is a specialized decorator that has one specific job:
# convert a generator function into a context manager.
@contextmanager
def logged_file(filename, mode):
    print(f"Opening #1 {filename}")
    file = open(filename, mode)  # Direct open
    try:
        yield file
    finally:
        print(f"Closing #1 {filename}")
        file.close()  # Manual close ← YOU DO THIS

@contextmanager
def logged_file_nested(filename, mode):
    with open(filename, mode) as file:  # Built-in auto-close
        yield file
    # No explicit close() needed! Built-in 'with' handles it



if __name__ == '__main__':
    # 1
    try:
        with logged_file('test.txt', 'w') as f:
            f.write("Hello world!")
    except Exception as e:
        print(f"Error {e}")

    #2
    try:
        with open('second_test.txt', 'w') as f:
            f.write("Hello world!")
    except Exception as e:
        print(f" Error {e}")