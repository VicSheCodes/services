"""

A generator is a simpler way to create iterators. Instead of writing a whole class with __init__, __iter__, and __next__, you just write a function with yield.
Simple everyday analogy
Think of a generator like a vending machine:
You press a button (call next())
It gives you one item (yields a value)
It pauses and remembers where it was
Press again, it gives you the next item
When empty, it stops
The magic word is yield — it's like a "pause button" that remembers everything.

"""

def even_numbers(start, end):
    if start % 2 != 0:
        start += 1

    while start <= end:
        yield start
        start += 2

if __name__ == '__main__':

    for num in even_numbers(1, 10):
        print(num)

# Example 1: Simple counter generator
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1