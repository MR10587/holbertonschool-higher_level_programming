#!/usr/bin/python3
"""Salam"""


class Student:
    """Students"""
    def __init__(self, first_name, last_name, age):
        """Student Data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        if isinstance(attrs, list):
            final = {}
            for i in attrs:
                if isinstance(i, str) and hasattr(self, i):
                    final[i] = getattr(self, i)
            return final
        return vars(self)

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
