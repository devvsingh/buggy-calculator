"""Simple calculator module providing basic arithmetic operations.

Functions:
- add(a, b): returns the sum of a and b.
- subtract(a, b): returns a minus b.
- multiply(a, b): returns the product of a and b.
- divide(a, b): returns a divided by b; raises ZeroDivisionError if b is zero.
- average(iterable): returns the arithmetic mean of the numbers in iterable.
"""

from __future__ import annotations
from typing import Iterable, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the result of *a* minus *b*."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return the division of *a* by *b*.

    Raises:
        ZeroDivisionError: If *b* is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def average(values: Iterable[Number]) -> float:
    """Return the arithmetic mean of the numbers in *values*.

    An empty iterable will raise a ``ZeroDivisionError`` because the mean
    of no numbers is undefined.
    """
    values_list = list(values)
    if not values_list:
        raise ZeroDivisionError("cannot compute average of empty iterable")
    return sum(values_list) / len(values_list)

__all__ = ["add", "subtract", "multiply", "divide", "average"]
