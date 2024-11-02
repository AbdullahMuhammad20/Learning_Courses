import pytest

'''
This is a test module for Accumulator class. 
It contains a fixture for initializing an Accumulator object to know how we can test unit test.
We can use this fixture in any test function to test the Accumulator class.
'''


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute"):
        accum.count = 100
