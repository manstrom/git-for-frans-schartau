from lesson_1.assignment.calculator_functions import addition_func


def test_addition():
    assert addition_func(10, 10) == 20, "Det förväntade resultatet är 20."
    assert addition_func(100, 100) == 200, "Det förväntade resultatet är 200."
    assert addition_func(10, 10) != 11, "Det förväntade resultatet är inte 11."