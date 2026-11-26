
from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if not isinstance(numerator, int) or isinstance(numerator, bool):
            raise TypeError("Numerator must be an integer")

        if not isinstance(denominator, int) or isinstance(denominator, bool):
            raise TypeError("Denominator must be an integer")

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify the fraction
        common = gcd(abs(numerator), denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator

    # Equality
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )

    def __ne__(self, other: object) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    # Comparison operators
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            <= other.numerator * self.denominator
        )

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            > other.numerator * self.denominator
        )

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            >= other.numerator * self.denominator
        )

    # Addition
    def __add__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Subtraction
    def __sub__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    # Multiplication
    def __mul__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented

        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    # Division
    def __truediv__(self, other: object):
        if not isinstance(other, Fraction):
            return NotImplemented

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    # String representation
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    # Developer representation
    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"
