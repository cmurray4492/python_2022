import pytest

# base function
def func(x):
    return x + 1

# Test the base function
def test_func():
    assert func(4) == 5
