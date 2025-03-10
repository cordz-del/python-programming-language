import time
import psutil

def sample_memory_intensive_task():
    # Allocate a large list to simulate memory usage.
    return [i for i in range(1000000)]

def detect_memory_leak(iterations=10):
    process = psutil.Process()
    for i in range(iterations):
        sample_memory_intensive_task()
        mem_usage = process.memory_info().rss / (1024 * 1024)  # in MB
        print(f"Iteration {i+1}: Memory usage: {mem_usage:.2f} MB")
        time.sleep(0.5)

if __name__ == "__main__":
    detect_memory_leak()
