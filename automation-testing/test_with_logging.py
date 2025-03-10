# test_with_logging.py
import logging
import unittest

logging.basicConfig(level=logging.INFO)

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

class TestLogging(unittest.TestCase):
    def test_subtract(self):
        result = subtract(10, 3)
        logging.info("Subtraction result: %s", result)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()
