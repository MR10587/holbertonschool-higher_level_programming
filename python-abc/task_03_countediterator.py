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
