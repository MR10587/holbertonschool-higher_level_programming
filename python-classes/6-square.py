#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)"""
    def __init__(self, size=0, position=(0, 0)):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            count = 0
            for item in value:
                if item > 0:
                    count += 1
            if count == 2:
                self.__position = value
            raise TypeError('position must be a tuple of 2 positive integers')

        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        self.__area = self.__size ** 2
        return self.__area

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print('#' * self.__size)
        else:
            print('')
