import time
import psutil

def heavy_computation():
    # Perform a heavy calculation.
    sum([i ** 2 for i in range(10000000)])

def monitor_cpu_usage():
    process = psutil.Process()
    # Sample CPU usage before and after computation.
    cpu_before = process.cpu_percent(interval=1)
    heavy_computation()
    cpu_after = process.cpu_percent(interval=1)
    print(f"CPU usage during computation: {cpu_after}%")

if __name__ == "__main__":
    monitor_cpu_usage()
