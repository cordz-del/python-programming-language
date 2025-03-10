# test_exception.py
import pytest

def divide(a, b):
    """Function to divide two numbers; raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def test_divide_exception():
    # Ensure that dividing by zero raises the correct exception.
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Division by zero" in str(excinfo.value)
