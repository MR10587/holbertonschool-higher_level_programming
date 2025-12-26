#!/usr/bin/python3
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area: {3.14159265359 * (self.radius ** 2)}"

    def perimeter(self):
        return f"Perimeter: {2 * 3.14159265359 * abs(self.radius)}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Area: {self.width * self.height}"

    def perimeter(self):
        return f"Perimeter: {2 * (self.width + self.height)}"


def shape_info(fiqur):
    print(fiqur.area())
    print(fiqur.perimeter())
