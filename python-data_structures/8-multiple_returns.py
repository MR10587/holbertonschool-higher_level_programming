#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length != 0:
        first = sentence[0]
    else:
        return None
    new_tuple = tuple([length, first])
    return new_tuple
