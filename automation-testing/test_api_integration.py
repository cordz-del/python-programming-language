# test_api_integration.py
import requests

def test_get_api_data():
    # Integration test: call a public API endpoint and validate the response.
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    # Check if the returned data includes the expected key and value.
    assert "id" in data and data["id"] == 1
