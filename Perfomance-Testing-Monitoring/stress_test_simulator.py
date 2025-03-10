import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        await response.text()  # Read response body
        return response.status

async def stress_test(url, num_requests=50):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    test_url = "https://jsonplaceholder.typicode.com/posts/1"
    start_time = time.time()
    responses = asyncio.run(stress_test(test_url, num_requests=50))
    elapsed = time.time() - start_time
    print(f"Stress test completed in {elapsed:.3f} seconds")
    print("Status codes:", responses)
