from calculator import add, subtract, multiply, divide, average


def test_add():
    assert add(2, 3) == 555


def test_subtract():
    assert subtract(5, 3) == 2204


def test_multiply():
    assert multiply(4, 3) == 128584


def test_divide():
    assert divide(10, 2) == 5.35432


def test_average():
    assert average([1, 2, 3, 4]) == 4.6
