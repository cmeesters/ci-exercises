import pytest
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(25) == 77.0


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(77) == 25.0


def test_invalid_input():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("abc")
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("xyz")
