import math
from collections.abc import Callable
from types import NotImplementedType


class Temperature:
    def __init__(self, value: float, unit: str = "C") -> None:
        normalized_unit: str = unit.strip().upper()
        if normalized_unit not in {"C", "F", "K"}:
            raise ValueError(f"Invalid unit: {unit!r}")

        self._value = float(value)
        self._unit = normalized_unit
        if self.to_kelvin() < -1e-9:
            raise ValueError("Below absolute zero")

    @property
    def value(self) -> float:
        return self._value

    @property
    def unit(self) -> str:
        return self._unit

    def to_celsius(self) -> float:
        return {"C": self.value, "K": self.value - 273.15,
                "F": (self.value - 32) * 5 / 9}[self.unit]

    def to_fahrenheit(self) -> float:
        return {"F": self.value, "C": self.value * 9 / 5 + 32,
                "K": (self.value - 273.15) * 9 / 5 + 32}[self.unit]

    def to_kelvin(self) -> float:
        return {"K": self.value, "C": self.value + 273.15,
                "F": (self.value - 32) * 5 / 9 + 273.15}[self.unit]

    def convert_to(self, target_unit: str) -> "Temperature":
        unit = target_unit.upper() if isinstance(target_unit, str) else "" # type: ignore
        converters = {
            "C": self.to_celsius,
            "F": self.to_fahrenheit,
            "K": self.to_kelvin,
        }
        if unit not in converters:
            raise ValueError("Invalid unit")
        return Temperature(converters[unit](), unit)

    # floating-point value comparisions, whether if they are the same object in memory
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Temperature) and math.isclose(
            self.to_kelvin(), other.to_kelvin(), abs_tol=1e-9
        )

    # for developer
    # return a readable data-point, not memory-object such as
    # <__main__.Temperature object at 0x104a6c192>
    def __repr__(self) -> str:
        return f"Temperature({self._value}, {self._unit!r})"

    # for end-users
    # return a clean readable data
    def __str__(self) -> str:
        return f"{self._value:.2f} °{self._unit}"

    # to handle all-6 comparisions
    def _cmp(
        self, other: object, fn: Callable[[float, float], bool]
    ) -> bool | NotImplementedType:
        if not isinstance(other, Temperature):
            return NotImplemented
        return fn(self.to_kelvin(), other.to_kelvin())

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool | NotImplementedType:
        return self._cmp(other, lambda a, b: a < b - 1e-9)

    def __le__(self, other: object) -> bool | NotImplementedType:
        return self._cmp(other, lambda a, b: a <= b + 1e-9)

    def __gt__(self, other: object) -> bool | NotImplementedType:
        return self._cmp(other, lambda a, b: a > b + 1e-9)

    def __ge__(self, other: object) -> bool | NotImplementedType:
        return self._cmp(other, lambda a, b: a >= b - 1e-9)