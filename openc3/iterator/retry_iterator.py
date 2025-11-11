"""
Create an iterator that retries failed operations.

__next__() called
      ↓
 Is _exhausted?
  ├─ Yes → raise StopIteration
  └─ No → Continue
      ↓
Try function call
  ├─ Success:
  │   ├─ Set _exhausted = True  ← INSIDE LOOP
  │   └─ return result
  └─ Exception:
      └─ Retry (up to max_retries)
          ↓
    All retries failed
      ├─ Set _exhausted = True  ← AFTER LOOP
      └─ raise last_exception


"""

class RetryIterator:
    """
    Iterator that attempts to call a function multiple times.
    Yields the result on success.
    Raises the last exception after max_retries.
    """
    def __init__(self, func, max_retries=3):
        self._exhausted = False
        self.func = func
        self.max_retries = max_retries

    def __iter__(self):
        return self

    def __next__(self):
        if self._exhausted:
            raise StopIteration

        last_exception = None

        for attempt in range(self.max_retries):
            try:
                res = self.func()  # ✅ Success! or ❌ Raises exception
                self._exhausted = True  # ← EXECUTES (success case) or ← NEVER EXECUTES
                return res  # ← Exits immediately or  ← NEVER EXECUTES
            except Exception as e:    # ❌ Never reached if was a Success!
                print(f"Attempt {attempt}/{self.max_retries} failed {e}")
                last_exception = e  # ← Executes instead

        self._exhausted = True  # only if NOT Success - EXECUTES (failure case)
        if last_exception:
            raise last_exception
        raise StopIteration

# Test with a flaky function:
import random

def flaky_operation():
    if random.random() < 0.9:  # 70% fail rate
        raise ConnectionError("Network error")
    return "Success!"

def test_it():
    # Should retry and eventually succeed or fail after 3 attempts:
    try:
        for result in RetryIterator(flaky_operation, max_retries=5):
            print(result)
            break  # Stop after first success
    except ConnectionError as e:
        print(f"Failed after retries: {e}")