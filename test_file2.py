from file1 import add_numbers, multiply_numbers, operation

def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-1, -1) == -2

def test_multiply_numbers():
    assert multiply_numbers(3, 5) == 15
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0

def operation():
    sum_result, multi_result = operation(3, 5)
    assert sum_result == 8
    assert multi_result == 15