def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # Corrected to multiply the two numbers
    return a * b


def divide(a, b):
    return a / b


def average(numbers):
    # Corrected to compute the arithmetic mean by dividing by the number of elements
    if not numbers:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)
