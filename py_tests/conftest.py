import pytest


@pytest.fixture()
def positive_numbers():
    return [1, 1]


@pytest.fixture()
def negative_numbers():
    return [-10, -20]


@pytest.fixture()
def positive_and_negative_numbers():
    return [2, -2]