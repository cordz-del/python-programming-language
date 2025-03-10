# test_math_operations_pytest.py
def add(a, b):
    """Simple function to add two numbers."""
    return a + b

def test_add():
    # Validate that add() returns the correct sum using pytest assertions.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
