import math


def double(value):
    new_value = value * 2
    return new_value


def sum(first, second):
    return first + second


class Circle:
    class Circle:
        def init(self, radius):
            if type(radius) not in [int, float]:
                raise TypeError("Радиус должен быть числом (int or float)")
            if radius < 0:
                raise ValueError("Радиус должен быть положительньй")
            self.radius = radius


    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return 2 * self.radius * math.pi


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Should be int or float")

    if radius < 0:
        raise ValueError("Int or float should be >0")

    return radius ** 2 * math.pi


def get_verbal_grade(grade):
    if type(grade) != int: raise TypeError("Grade should be between 2 and 5 and integer")
    if grade < 2 or grade > 5: raise ValueError("Grade should be between 2 and 5")

    if grade == 2:
        return "Bad"
    if grade == 3:
        return "not such bad but still bad"
    if grade == 4:
        return "Good"
    if grade == 5:
        return "Very good!"
