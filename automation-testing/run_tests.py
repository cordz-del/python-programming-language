# run_tests.py
import unittest

if __name__ == "__main__":
    # Discover and run all test files matching the pattern 'test_*.py' in the current directory.
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=".", pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)
