#!/usr/bin/python3
class CountedIterator:

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        item = next(self.iterator)
        return item
