def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # BUG: this should multiply, not add
    return a + b


def divide(a, b):
    return a / b


def average(numbers):
    # BUG: off-by-one, should divide by len(numbers)
    return sum(numbers) / (len(numbers) - 1)
