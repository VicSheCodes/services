"""
An iterator is like a pointer that moves through a collection of items one by one.
It allows you to access each item in the collection without needing to know the details of
how the collection is structured.

Key concepts (very simple):
Iterator = an object that "knows" how to give you the next item
__iter__() = says "I am iterable" (returns the iterator itself)
__next__() = gives you the next item, or says "I'm done" (raises StopIteration)
next() = function you use to get the next item from an iterator
iter() = function that turns an iterable (like a list) into an iterator

Iterable = something you CAN loop over (list, string, tuple). Has __iter__().
Iterator = the actual object doing the looping. Has both __iter__() AND __next__().

When to use iterators
When you want to save memory (process one item at a time instead of loading everything)
When working with large files or data streams
When you need to create your own custom way of looping through data
"""

# Example 1: List is iterable, but NOT an iterator yet
fruits = ["apple", "banana", "cherry"]

# Turn the list into an iterator using iter()
fruit_iterator = iter(fruits)

# Get items one by one using next()
print(next(fruit_iterator))  # apple
print(next(fruit_iterator))  # banana
print(next(fruit_iterator))  # cherry
# next(fruit_iterator)  # This would raise StopIteration (no more items)


# Example 2: String to iterator
word = "hello"
word_iter = iter(word)

print(next(word_iter))  # h
print(next(word_iter))  # e
print(next(word_iter))  # l

# Example 3: for loop uses iterators automatically
for fruit in fruits:
    print(fruit)  # Behind the scenes, Python uses iter() and next()

# Example 4: Behind the scenes of a for loop
fruits = ["apple", "banana"]

# These two are the same:
# Option A - Python does this automatically
for fruit in fruits:
    print(fruit)

# Option B - What Python actually does under the hood
fruit_iter = iter(fruits)  # Convert to iterator
while True:
    try:
        fruit = next(fruit_iter)  # Get next item
        print(fruit)
    except StopIteration:  # Stop when done
        break


# Example 5: Creating your own simple iterator
class CountTo:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        # This method makes it iterable
        return self

    def __next__(self):
        # This method gives the next value
        if self.current > self.max_num:
            raise StopIteration  # Signal we're done

        value = self.current
        self.current += 1
        return value


# Using our custom iterator
counter = CountTo(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# next(counter) would raise StopIteration

# Or use it in a loop
counter2 = CountTo(3)
for num in counter2:
    print(num)  # prints 1, 2, 3

"""
iter() converts an iterable (list, string, tuple) into an iterator so you can use next() on it. If something is already 
an iterator (like your CountTo class), you don't need iter().
"""

