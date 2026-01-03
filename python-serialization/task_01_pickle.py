#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display():
        print(f'Name: {self.__name}\nAge: {self.__age}\nIs Student: {self.__is_student}')

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, UnicodeDecodeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.load(f)
        except (FileNotFoundError, UnicodeDecodeError):
            return None
