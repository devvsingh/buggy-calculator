def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    return a / b


def average(numbers):
    """Return the arithmetic mean of a list of numbers.

    The function calculates the sum of the numbers and divides by the
    count of elements. It assumes ``numbers`` is a non‑empty iterable of
    numeric values.
    """
    if not numbers:
        raise ValueError("Cannot compute the average of an empty sequence")
    return sum(numbers) / len(numbers)
