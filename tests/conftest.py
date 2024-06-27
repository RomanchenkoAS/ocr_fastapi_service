import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def test_client():
    """
    Set up a TestClient as a substitute for the usual FastAPI app
    """

    client = TestClient(app)
    yield client
