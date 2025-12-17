#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)"""
    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        self.area = self.__size ** 2
        return self.area
