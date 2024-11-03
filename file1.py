def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def operation(x, y):
    sum_result = add_numbers(x, y)
    multi_result = multiply_numbers(x, y)

    print(f"The sum of {x} and {y} is: {sum_result}")
    print(f"The Multiplication of {x} and {y} is: {multi_result}")

operation(3, 5)