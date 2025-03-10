import asyncio
import time
import httpx

async def async_request(url):
    async with httpx.AsyncClient() as client:
        start = time.time()
        response = await client.get(url)
        latency = time.time() - start
        print(f"Async request latency: {latency:.3f} seconds")
        return response.status_code, latency

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    asyncio.run(async_request(url))
