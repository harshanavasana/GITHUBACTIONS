from src.math_operations import add_numbers, sub_numbers

def test_add():
    assert add_numbers(2,3) == 5
    assert add_numbers(1,1) == 2

def test_sub():
    assert sub_numbers(5,3) == 2
    assert sub_numbers(10,4) == 6