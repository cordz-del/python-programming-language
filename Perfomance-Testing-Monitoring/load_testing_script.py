import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def simulate_request(id):
    # Simulate network delay.
    time.sleep(0.5)
    return f"Response from request {id}"

def load_test(num_requests=20):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(simulate_request, i) for i in range(num_requests)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    load_test()
