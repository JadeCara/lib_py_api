import pytest
from src.api import PyAPI


@pytest.fixture
def client():
    return PyAPI("http://example.com")
