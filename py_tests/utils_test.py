import pytest
from conftest import positive_numbers,negative_numbers,positive_and_negative_numbers

from utils import ticket_price, double, sum_func, get_verbal_grade, Circle


class TestTicketPrice:

    def test_0(self):
        assert ticket_price(0) == "Бесплатно", "Ошибкадля 0 лет"

    def test_1(self):
        assert ticket_price(1) == "Бесплатно", "Ошибкадля 1 лет"

    def test_7(self):
        assert ticket_price(7) == "100 рублей", "Ошибкадля 7 лет"

    def test_18(self):
        assert ticket_price(18) == "200 рублей", "Ошибкадля 18 лет"

    def test_25(self):
        assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"

    def test_60(self):
        assert ticket_price(60) == "Бесплатно", "Ошибкадля 60 лет"

    def test_minus_1(self):
        assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"


class CircleTest:
    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, "Radius Error"

    def test_get_diametr(self):
        circle = Circle(1)
        assert circle.get_diameter() == 2, "Diameter Error"

    def test_get_perimeter(self):
        circle = Circle(1)
        assert round(circle.get_perimeter(), 2) == 6.28, "Perimeter Error"

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle("Один")

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)


class TestSumFunc:
    def test_sum_positive(self, positive_numbers):
        c = sum_func(positive_numbers[0], positive_numbers[1])
        assert c > 0
        assert c == 2

    def test_sum_negative(self, negative_numbers):
        c = sum_func(negative_numbers[0], negative_numbers[1])
        assert c < 0
        assert c == -30

    def test_sum_positive_and_negative(self, positive_and_negative_numbers):
        c = sum_func(positive_and_negative_numbers[0], positive_and_negative_numbers[1])
        assert c == 0


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected


#sum_of_two_params = [(0, 0, 0), (1, 1, 2), (10.0, 20.0, 30.0), (-3, -6, -9)]

# @pytest.mark.parametrize(
#     "first, second, expected",
#     sum_of_two_params
# )
# def test_double(first, second, expected):
#     assert sum(first, second) == expected


grade_params = [(2, "Bad"), (3, "not such bad but still bad"), (4, "Good"), (5, "Very good!"), ]


@pytest.mark.parametrize("grade_int, grade_str", grade_params)
def test_get_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str


grade_exceptions = [(1, ValueError), (6, ValueError), ("Пять", TypeError), (5.0, TypeError)]


@pytest.mark.parametrize("grade_int , exception", grade_exceptions)
def test_get_verbal_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        assert get_verbal_grade(grade_int)





