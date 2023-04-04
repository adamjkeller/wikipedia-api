# test_main.py
import json
from fastapi.testclient import TestClient
from main import app, Search, WikiSummarySearch

client = TestClient(app)

# Mock wiki.get_summary
def mock_get_summary(self, term):
    if term == "valid_term":
        return {
            "Status": "Success",
            "Response": "Valid term summary."
        }
    elif term == "error_term":
        return {
            "Status": "Error",
            "Response": "Error fetching summary."
        }
    elif term == "":
        return {
            "Status": "Error",
            "Response": "Please provide a search value"
        }
    else:
        return {
            "Status": "NotFound",
            "Response": "Term not found."
        }

WikiSummarySearch.get_summary = mock_get_summary

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"Response": "Healthy"}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Response": "Please navigate to /docs for API documentation"}

def test_return_summary_result_success():
    search_term = Search(term="valid_term")
    response = client.post("/summary", json=search_term.dict())
    assert response.status_code == 200
    assert response.json() == {
        "Status": "Success",
        "Response": "Valid term summary."
    }

def test_return_summary_result_error():
    search_term = Search(term="error_term")
    response = client.post("/summary", json=search_term.dict())
    assert response.status_code == 404
    assert response.json() == {
        "Status": "Error",
        "Response": "Error fetching summary."
    }

def test_return_summary_result_not_found():
    search_term = Search(term="invalid_term")
    response = client.post("/summary", json=search_term.dict())
    assert response.status_code == 404
    assert response.json() == {
        "Status": "NotFound",
        "Response": "Term not found."
    }