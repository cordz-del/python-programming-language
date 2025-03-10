import time

def sample_function():
    # Simulate a workload with a fixed delay.
    time.sleep(0.5)
    return "done"

def measure_latency():
    start_time = time.time()
    result = sample_function()
    end_time = time.time()
    latency = end_time - start_time
    print(f"Function result: {result}")
    print(f"Latency: {latency:.3f} seconds")

if __name__ == "__main__":
    measure_latency()
