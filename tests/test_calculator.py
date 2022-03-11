import pytest

from calculator import add


def test_add_function_tommy():
    assert add(1, 2) == 3

def test_add_function_eric_gran():
    assert add(hej, hopp) == 203232
    
def test_add_function_RickardJStad():
    assert add(20, 30) != 40
