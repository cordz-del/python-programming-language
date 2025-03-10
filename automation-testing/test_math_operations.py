# test_math_operations.py
import unittest

def add(a, b):
    """Simple function to add two numbers."""
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # Validate that add() returns the correct sum.
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
