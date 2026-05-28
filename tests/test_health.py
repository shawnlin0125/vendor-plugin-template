import pytest
from app.main import app


@pytest.fixture
def client():
    """Use FastAPI TestClient for proper ASGI support."""
    from fastapi.testclient import TestClient
    return TestClient(app)


def test_health_returns_ok(client):
    """GET /health must return 200 with status=ok."""
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "uptime_seconds" in data
    assert isinstance(data["uptime_seconds"], int)


def test_root_returns_message(client):
    """GET / must return 200 with a message."""
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "message" in data
