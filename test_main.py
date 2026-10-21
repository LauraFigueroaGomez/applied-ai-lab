from unittest.mock import Mock

import main
from main import StudyNotesResult
from main import app
from fastapi.testclient import TestClient


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

def test_study_notes_too_short():
    response = client.post(
        "/study-notes",
        json={"notes":"too short"}
    )
    assert response.status_code == 422

def test_study_notes_too_long():
    response = client.post(
        "/study-notes",
        json={"notes":"a" * 3001}
    )
    assert response.status_code == 422

def test_study_notes_missing():
    response = client.post(
        "/study-notes",
        json={}
    )
    assert response.status_code == 422

def test_study_notes_success(monkeypatch):
    parsed = StudyNotesResult(
        summary="FastAPI validates input.",
        key_points=["one", "two", "three"],
        practice_question="What does Pydantic check?"
    )
    fake_response = Mock(output_parsed=parsed)
    fake_client = Mock()
    fake_client.responses.parse.return_value = fake_response
    monkeypatch.setattr(main, "OpenAI", lambda **kwargs: fake_client)

    response = client.post(
        "/study-notes",
        json={"notes": "FastAPI uses Pydantic to validate request bodies."}
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "FastAPI validates input.",
        "key_points": ["one", "two", "three"],
        "practice_question": "What does Pydantic check?"
    }