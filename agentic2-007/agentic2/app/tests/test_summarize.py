# tests/test_summarize.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize():
    response = client.post("/api/summarize", json={"text": "FastAPI is a modern, fast web framework for building APIs with Python."})
    assert response.status_code == 200
    assert "summary" in response.json()

# Add this to test_summarize.py temporarily
def test_simple():
    assert 1 == 1