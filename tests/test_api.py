from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "AI Receptionist API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_business_info():
    response = client.get("/business-info/")

    assert response.status_code == 200

    data = response.json()

    assert "business_name" in data
    assert "opening_hours" in data
    assert "services" in data