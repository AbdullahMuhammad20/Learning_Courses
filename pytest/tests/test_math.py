import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)


'''
pytest 
doing parametrized tests using pytest.mark.parametrize
'''
# Multiply test ideas:
# two positive integers
# identinity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative
# floating point numbers

products = [
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floating point
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
