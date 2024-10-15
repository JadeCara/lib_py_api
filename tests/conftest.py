import pytest
from unittest.mock import MagicMock
from src.api import PyAPI


@pytest.fixture
def client():
    return PyAPI("http://example.com")


@pytest.fixture
def mock_response():
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {"key": "value"}
    return mock_response


@pytest.fixture
def mock_fail():
    mock_response = MagicMock()
    mock_response.ok = False
    mock_response.status_code = 404
    mock_response.text = "Not Found"
    return mock_response
