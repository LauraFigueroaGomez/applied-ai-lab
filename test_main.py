from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_empty_prompt():
    response = client.post(
        "/generate",
        json={"prompt": ""}
    )
    assert response.status_code == 422

def test_echo():
    response = client.post(
        "/echo",
        json={"text": "hello"}
    )
    assert response.status_code == 200
    assert response.json() == {"received": "hello"}

def test_echo_missing_text():
    response = client.post(
        "/echo",
        json={}
    )
    assert response.status_code == 422

