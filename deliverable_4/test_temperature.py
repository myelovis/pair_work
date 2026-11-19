import pytest  
from temperature import Temperature


def test_init():
    t = Temperature(25)
    assert (t.value, t.unit) == (25.0, "C")

    t_f = Temperature(77, "f")
    assert (t_f.value, t_f.unit) == (77.0, "F")

    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "K"


@pytest.mark.parametrize(  # pyright: ignore[reportUnknownMemberType, reportUntypedFunctionDecorator]
    "v, u",
    [(25, "X"), (-273.16, "C"), (-459.68, "F"), (-0.01, "K")],
)
def test_validation(v, u):
    with pytest.raises(ValueError):
        Temperature(v, u)


@pytest.mark.parametrize(
    "c, f, k",
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (37.0, 98.6, 310.15),
        (100.0, 212.0, 373.15),
    ],
)
def test_conversions(c, f, k):
    tc, tf, tk = Temperature(c, "C"), Temperature(f, "F"), Temperature(k, "K")
    assert tc.to_fahrenheit() == pytest.approx(f)
    assert tc.to_kelvin() == pytest.approx(k)
    assert tf.to_celsius() == pytest.approx(c)
    assert tf.to_kelvin() == pytest.approx(k)
    assert tk.to_celsius() == pytest.approx(c)
    assert tk.to_fahrenheit() == pytest.approx(f)


def test_round_trip():
    t = Temperature(23.45, "C")
    assert t.convert_to("F").convert_to("K").convert_to("C") == t


def test_comparisons():
    c0, f32, c100 = Temperature(0, "C"), Temperature(32, "F"), Temperature(100, "C")
    assert c0 == f32
    assert not (c0 != f32)
    assert c0 < c100
    assert c0 <= f32 <= c100
    assert c100 > f32
    assert c100 >= c0
    assert (c0 == 0) is False
    with pytest.raises(TypeError):
        c0 < 0


def test_formatting():
    t = Temperature(25, "C")
    assert repr(t) == "Temperature(25.0, 'C')"
    assert str(t) == "25.00 °C"