"""
 Even Numbers Iterator (Medium)
Create a custom iterator class called EvenNumbers that generates even numbers from a start value up to (and including) an end value.

Requirements:
Takes start and end in __init__
Only yields even numbers in that range
If start is odd, begin from the next even number
"""

class EvenNumber:

    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        if self.start % 2 != 0:
            self.start += 1

        val = self.start
        self.start += 2

        return val

if __name__ == '__main__':
    evens_iter = EvenNumber(1, 10)

    for num in evens_iter:
        print(num)
