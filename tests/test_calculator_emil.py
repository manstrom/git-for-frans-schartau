import pytest

from src.calculator import add, multiply


def test_multiplication_function():
    assert multiply(2, 2) == 4

def test_multiplication2_function():
    assert multiply(2, 5) == 10

def test_add_function_tommy_updates_same_file():
    assert multiply(10, 2) == 20
