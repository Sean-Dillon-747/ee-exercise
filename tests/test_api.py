from fastapi.testclient import TestClient
from unittest.mock import patch 
from application.main import app

client = TestClient(app)

def test_octocat_main():
    response = client.get("/octocat")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    if response.json():
        first_item = response.json()[0]
        assert "id" in first_item
        assert "html_url" in first_item
        assert "files" in first_item


def test_nonexistent_user():
    response = client.get("/21321321321")
    assert response.status_code == 200
    assert response.json() == []

def test_empty_username():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

@patch("application.gists.requests.get")
def test_github_api_forbidden_user(mock_get):
    mock_get.return_value.status_code = 403
    response = client.get("/octocat")
    assert response.status_code == 403
    assert response.json() == {"detail": "Access forbidden"}

@patch("application.gists.requests.get")
def test_github_api_server_error(mock_get):
    mock_get.return_value.status_code = 500
    response = client.get("/octocat")
    assert response.status_code == 500
    assert response.json() == {"detail": "GitHub server error"}