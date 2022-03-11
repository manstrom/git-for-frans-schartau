import pytest

from calculator import add


def test_add_function_tommy():
    assert add(1, 2) == 3

def test_add_function_rikard():
    assert add(2, 2) == 4

def test_add_function_eric_gran():
    assert add(hej, hopp) == 203232