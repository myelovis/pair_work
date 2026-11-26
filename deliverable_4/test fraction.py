
import pytest
from fraction import Fraction

# this test file is for testing the Fraction class

# Initialization tests
def test_initialization():
    f = Fraction(2, 4)

    assert f.numerator == 1
    assert f.denominator == 2


def test_default_denominator():
    f = Fraction(5)

    assert f.numerator == 5
    assert f.denominator == 1


def test_negative_denominator():
    f = Fraction(1, -2)

    assert f.numerator == -1
    assert f.denominator == 2


def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)


def test_non_integer_values():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

    with pytest.raises(TypeError):
        Fraction(1, 2.5)


# Comparison tests
def test_equality():
    assert Fraction(1, 2) == Fraction(2, 4)


def test_inequality():
    assert Fraction(1, 2) != Fraction(2, 3)


def test_less_than():
    assert Fraction(1, 3) < Fraction(1, 2)


def test_less_than_or_equal():
    assert Fraction(1, 2) <= Fraction(2, 4)


def test_greater_than():
    assert Fraction(3, 4) > Fraction(1, 2)


def test_greater_than_or_equal():
    assert Fraction(3, 4) >= Fraction(6, 8)


# Arithmetic tests
def test_addition():
    result = Fraction(1, 2) + Fraction(1, 4)

    assert result == Fraction(3, 4)


def test_subtraction():
    result = Fraction(3, 4) - Fraction(1, 4)

    assert result == Fraction(1, 2)


def test_multiplication():
    result = Fraction(2, 3) * Fraction(3, 4)

    assert result == Fraction(1, 2)


def test_division():
    result = Fraction(1, 2) / Fraction(3, 4)

    assert result == Fraction(2, 3)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 2) / Fraction(0, 1)


# Formatting tests
def test_string():
    assert str(Fraction(1, 2)) == "1/2"


def test_repr():
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"


# Read-only properties
def test_read_only():
    f = Fraction(1, 2)

    with pytest.raises(AttributeError):
        f.numerator = 5

    with pytest.raises(AttributeError):
        f.denominator = 10
