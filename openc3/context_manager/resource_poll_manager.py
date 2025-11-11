"""
Create a context manager that manages a pool of resources.
"""

class ResourcePool:
    """
    Context manager + Iterator that:
    - Manages a pool of resources (e.g., connections)
    - Acquires a resource on __enter__
    - Releases it on __exit__
    - Iterates over available resources
    - Handles resource exhaustion
    """
    def __init__(self, max_size=3):
        self.max_size = max_size
        self.available = list(range(max_size))  # Simulated resources
        self.in_use = set()

    def acquire(self):
        """
        Get a resource from the pool.
        Raise ResourceError if pool is exhausted.
        """
        pass  # Your code here

    def release(self, resource):
        """
        Return a resource to the pool.
        """
        pass  # Your code here

    def __enter__(self):
        pass  # Your code here

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass  # Your code here

    def __iter__(self):
        """Iterate over available resources"""
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