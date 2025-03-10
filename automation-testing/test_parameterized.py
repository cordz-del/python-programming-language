# test_parameterized.py
import pytest

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 5, 20),
    (0, 10, 0),
    (-1, 8, -8)
])
def test_multiply(a, b, expected):
    # Test multiply() with multiple sets of inputs.
    assert multiply(a, b) == expected
