"""
Line-by-Line File Processor (Generator + Multiple Exceptions)
reate a generator that processes file lines and handles different errors per line.
"""

def process_json_lines(filename):
    """
    Generator that:
    - Reads a file line-by-line
    - Parses each line as JSON
    - Yields parsed objects
    - Skips invalid JSON lines (logs error)
    - Raises FileNotFoundError if file missing
    - Always closes file
    """
    pass  # Your code here

# Test file content (create test.jsonl):
# {"name": "Alice", "age": 30}
# {"invalid json
# {"name": "Bob", "age": 25}

# Test:
for obj in process_json_lines('test.jsonl'):
    print(obj)
# Should print Alice and Bob, skip invalid line