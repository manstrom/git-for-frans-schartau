import pytest

from src.calculator import add


def test_add_function():
    assert add(1, 2) == 3
