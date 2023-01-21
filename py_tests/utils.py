import math


def double(value):
    new_value = value * 2
    return new_value


def sum(first, second):
    return first + second


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Should be int or float")

    if radius < 0:
        raise ValueError("Int or float should be >0")

    return radius ** 2 * math.pi
