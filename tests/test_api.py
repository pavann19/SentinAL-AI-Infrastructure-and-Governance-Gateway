import pytest
from fastapi.testclient import TestClient
from api.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("api.main.assess_risk")
def test_assess_endpoint_clean(mock_assess_risk):
    # Mock assess_risk to return low risk so we don't trigger ML models in unit tests
    mock_assess_risk.return_value = ("LOW", {"semantic_score": 0.1, "source": "mock"})
    
    response = client.post("/api/v1/assess", json={"prompt": "Hello world", "role": "GENERAL"})
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "LOW"
    assert "decision" in data
    assert "clean_prompt" in data

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
