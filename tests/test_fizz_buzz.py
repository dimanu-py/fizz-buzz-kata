import pytest

from fizz_buzz.fizz_buzz import fizz_buzz


@pytest.mark.parametrize("number, expected", [(1, "1"), (2, "2"), (4, "4")])
def test_return_string_when_non_divisible_number(number: int, expected: str):
    assert fizz_buzz(number) == expected


@pytest.mark.parametrize("number, expected", [(3, "Fizz"), (6, "Fizz"), (9, "Fizz"), (12, "Fizz"), (18, "Fizz")])
def test_return_fizz_when_divisible_by_3(number: int, expected: str):
    assert fizz_buzz(number) == expected

