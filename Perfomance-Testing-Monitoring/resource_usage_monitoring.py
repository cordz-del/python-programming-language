import time
import psutil

def sample_workload():
    # Simulate workload by performing a computation.
    return [i ** 2 for i in range(100000)]

def monitor_resource_usage():
    process = psutil.Process()
    # Record initial memory usage (in MB)
    start_mem = process.memory_info().rss / (1024 * 1024)
    result = sample_workload()
    # Wait a moment to allow CPU sampling
    time.sleep(1)
    cpu_usage = process.cpu_percent(interval=1)
    end_mem = process.memory_info().rss / (1024 * 1024)
    print(f"CPU usage: {cpu_usage}%")
    print(f"Memory usage: {end_mem:.2f} MB (was {start_mem:.2f} MB)")
    return result

if __name__ == "__main__":
    monitor_resource_usage()
