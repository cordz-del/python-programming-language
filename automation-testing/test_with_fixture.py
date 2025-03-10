# test_with_fixture.py
import pytest

@pytest.fixture
def sample_data():
    # Setup: create sample data that can be used by tests.
    data = {"value": 42}
    yield data
    # Teardown: cleanup if needed.
    data.clear()

def test_using_fixture(sample_data):
    # Use the fixture data in a test.
    assert sample_data["value"] == 42
