import pytest

from src.calculator import add


def test_add_function_oskar():
    assert add(10, 10) == 100
