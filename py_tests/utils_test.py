import pytest

from main import ticket_price
from utils import double, sum


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


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected


sum_of_two_params = [(0, 0, 0), (1, 1, 2), (10.0, 20.0, 30.0), (-3, -6, -9)]


@pytest.mark.parametrize(
    "first, second, expected",
    sum_of_two_params
)
def test_double(first, second, expected):
    assert sum(first, second) == expected
