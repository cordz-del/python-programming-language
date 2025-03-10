# performance_test.py
import timeit

def slow_function():
    """A dummy function that performs a simple loop."""
    total = 0
    for i in range(1000):
        total += i
    return total

# Measure the execution time of slow_function over 1000 runs.
execution_time = timeit.timeit("slow_function()", setup="from __main__ import slow_function", number=1000)
print(f"Execution time for 1000 runs: {execution_time:.4f} seconds")
