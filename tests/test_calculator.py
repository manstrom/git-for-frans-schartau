import pytest

from src.calculator import add


def test_add_function_tommy():
    assert add(1, 2) == 3


def test_add_function_ronny():
    assert add(-1, -1) == -2

def test_add_function_eric_gran():
    assert add(hej, hopp) == 203232