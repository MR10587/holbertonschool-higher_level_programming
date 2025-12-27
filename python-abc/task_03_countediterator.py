#!/usr/bin/python3
class CountedIterator:

    def __init__(self, iterator, counter=0):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        item = next(self.iterator)
        return item


data = [4, 3, 2, 1]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
