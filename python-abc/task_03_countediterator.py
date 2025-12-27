#!/usr/bin/python3
class CountedIterator:

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item


data = [1, 2, 3, 4,5]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
