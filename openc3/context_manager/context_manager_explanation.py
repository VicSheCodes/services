"""
A context manager is a tool that helps you automatically clean up resources (like files, database connections, locks) when you're done with them — even if errors happen.
Simple everyday analogy
Think of a context manager like automatic doors at a store:
You approach → door opens automatically (setup)
You walk through and shop (use the resource)
You leave → door closes automatically (cleanup)
Even if you run out → door still closes (cleanup happens even with errors)
The magic words are with — Python's way of saying "handle setup and cleanup for me".

Context Manager                   Generator                 Iterator
Manages resources (setup/cleanup) Produces values on demand Provides sequential access
Uses with                         Uses yield                Uses next()
Always cleans up                  Pauses and resumes        Iterates until exhausted
__enter__ and __exit__            yield statements         __iter__ and __next__

When to use context managers
Working with files (reading/writing)
Database connections (open/close)
Network connections (connect/disconnect)
Locks in threading (acquire/release)
Temporary changes (change and revert)
Timers (start/stop measurement)
Any resource that needs guaranteed cleanup
Key benefits
Automatic cleanup — no forgetting to close files!
Error-safe — cleanup happens even if exceptions occur
Cleaner code — no try/finally everywhere
Reusable — write once, use many times
"""