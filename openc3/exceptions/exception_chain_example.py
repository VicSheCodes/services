import pytest
from functools import wraps

# Decorator to print exception chain for tests expecting any exception

def print_exception_chain_any(test_func):
    @wraps(test_func)
    def wrapper(*args, **kwargs):
        try:
            test_func(*args, **kwargs)
        except Exception as e:
            chain = []
            exc = e
            while exc:
                chain.append(f"{type(exc).__name__}: {exc}")
                exc = exc.__cause__
            chain_str = "\n".join(chain)
            raise AssertionError(f"Exception chain:\n{chain_str}") from e
    return wrapper

class C:
    def do_c(self):
        try:
            # Simulate an error in C
            raise ValueError("Error in C")
        except Exception as e:
            raise RuntimeError("C failed") from e

class B:
    def do_b(self):
        try:
            c = C()
            c.do_c()
        except Exception as e:
            raise RuntimeError("B failed") from e

class A:
    def do_a(self):
        try:
            b = B()
            b.do_b()
        except Exception as e:
            raise RuntimeError("A failed") from e

@print_exception_chain_any
def test_exception_chain():
    a = A()
    a.do_a()
