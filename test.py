import pytest


from sistema import (
    celsius_a_fahrenheit,
    km_a_millas,
    mxn_a_usd,
    usd_a_mxn,
)


# CP01 - RF01: Celsius a Fahrenheit
@pytest.mark.unit
def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(100) == 212.0


# CP02 - RF02 y RNF01: Kilómetros a Millas (parametrizada, 2 decimales)
@pytest.mark.unit
@pytest.mark.parametrize(
    "km, esperado",
    [
        (0, 0.0),
        (10, 6.21),
        (100, 62.14),
    ],
)
def test_km_a_millas(km, esperado):
    assert km_a_millas(km) == esperado


# CP03 - RF03: Pesos a Dólares y Dólares a Pesos (tasa fija 18.00)
@pytest.mark.unit
def test_conversion_pesos_dolares():
    assert mxn_a_usd(180) == 10.0
    assert usd_a_mxn(10) == 180.0