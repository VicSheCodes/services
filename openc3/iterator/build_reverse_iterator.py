"""
Exercise 1: Build a Reverse Iterator (Easy-Medium)
Create a custom iterator class called ReverseIterator that takes a list and iterates through it backwards.
Requirements:
Takes a list in __init__
Implements __iter__() and __next__()
Should work with for loops and next()
"""

class ReverseIterator:

    def __init__(self, lst):
        self.list = lst
        self.current = len(lst)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        value = self.list[self.current]
        self.current -= 1

        return value


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    rev_iter = ReverseIterator(nums)

    for num in rev_iter:
        print(num)