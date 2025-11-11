from contextlib import contextmanager


@contextmanager
def logged_file_1(filename, mode):
    print(f"Opening {filename}")
    file = open(filename, mode)  # ← Manual open. NO 'with'! Must close manually
    try:
        yield file
    finally:
        print(f"Closing {filename}")
        file.close()  # ← Manual close.  REQUIRED because you didn't use 'with'


@contextmanager
def logged_file_2(filename, mode):
    print(f"Opening {filename}")
    with open(filename, mode) as file:  # ← Nested context manager using with
        yield file
    print (f"Closing file {filename}")  # no need to close