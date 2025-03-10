import time
import psutil

def sample_task():
    time.sleep(0.4)
    return "completed"

def log_performance_metrics():
    process = psutil.Process()
    start_time = time.time()
    result = sample_task()
    end_time = time.time()
    latency = end_time - start_time
    cpu_usage = process.cpu_percent(interval=1)
    mem_usage = process.memory_info().rss / (1024 * 1024)
    with open("performance_log.txt", "a") as f:
        f.write(f"Task result: {result}\n")
        f.write(f"Latency: {latency:.3f} seconds, CPU: {cpu_usage}%, Memory: {mem_usage:.2f} MB\n\n")
    print("Performance metrics logged.")

if __name__ == "__main__":
    log_performance_metrics()
