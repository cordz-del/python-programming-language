import time

def sample_function():
    # Simulate a workload with a shorter delay.
    time.sleep(0.3)
    return "done"

def benchmark_batch(iterations=10):
    latencies = []
    for _ in range(iterations):
        start = time.time()
        sample_function()
        latencies.append(time.time() - start)
    avg_latency = sum(latencies) / iterations
    print(f"Average latency over {iterations} iterations: {avg_latency:.3f} seconds")
    return avg_latency

if __name__ == "__main__":
    benchmark_batch()
