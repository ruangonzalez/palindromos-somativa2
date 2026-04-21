import pytest

from main import somar, subtrair, multiplicar, dividir, eh_par


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 5) == 15


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(5) is False
