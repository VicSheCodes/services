"""
dead lock:
The basic functions to do this are .acquire() and .release().
A thread will call my_lock.acquire() to get the lock. If the lock is already held, the calling thread will wait
until it is released. There’s an important point here.
If one thread gets the lock but never gives it back, your program will be stuck.

Python’s Lock will also operate as a context manager, so you can use it in a with statement,
and it gets released automatically when the with block exits for any reason

RLock
It allows a thread to .acquire() an RLock multiple times before it calls .release().
That thread is still required to call .release() the same number of times it called .acquire(),
but it should be doing that anyway.
"""