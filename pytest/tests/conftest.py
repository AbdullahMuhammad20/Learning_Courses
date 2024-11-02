import pytest

# from stuff.accum import Accumulator


@pytest.fixture
def accum():
    yield Accumulator()
    print("Done with test case using fixture")
