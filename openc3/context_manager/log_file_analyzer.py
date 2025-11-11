"""
Log File Analyzer (Generator + Exceptions + Context Manager)
Create a log analyzer similar to your artifact processing.
"""
from contextlib import contextmanager


@contextmanager
def log_analyzer(filename, fail_on_corrupt=False):
    """
    Context manager + generator that:
    - Opens a log file
    - Yields parsed log entries
    - Handles corrupt lines (skip or raise based on flag)
    - Generates a summary report
    - Always closes file
    """
    pass  # YOUR CODE HERE

# Test log file (create test.log):
# 2024-01-01 10:00:00 INFO Started
# CORRUPT LINE
# 2024-01-01 10:01:00 ERROR Failed
# 2024-01-01 10:02:00 INFO Recovered

# Usage:
with log_analyzer('test.log', fail_on_corrupt=False) as logs:
    for entry in logs:
        print(entry)
# Should skip corrupt line, yield 3 entries