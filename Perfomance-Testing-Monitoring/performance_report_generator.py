import time
import psutil
import json

def sample_function():
    time.sleep(0.2)
    return "done"

def generate_performance_report():
    process = psutil.Process()
    start_time = time.time()
    result = sample_function()
    end_time = time.time()
    report = {
        "result": result,
        "latency": end_time - start_time,
        "cpu_usage": process.cpu_percent(interval=1),
        "memory_usage_mb": process.memory_info().rss / (1024 * 1024)
    }
    with open("performance_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Performance report generated:")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    generate_performance_report()
