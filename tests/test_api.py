import pytest
from unittest.mock import patch


class TestAPI:

    @patch("src.api.requests.get")
    def test_get_success(self, mock_get, client, mock_response):
        mock_get.return_value = mock_response
        result = client.get("test-endpoint")

        mock_get.assert_called_once_with("http://example.com/test-endpoint")
        assert result == {"key": "value"}

    @patch("src.api.requests.get")
    def test_get_failure(self, mock_get, client, mock_fail):
        mock_get.return_value = mock_fail

        with pytest.raises(Exception, match="API request failed with status code 404"):
            client.get("invalid-endpoint")

    @patch("src.api.requests.post")
    def test_post_success(self, mock_post, client, mock_response):
        mock_post.return_value = mock_response
        result = client.post("test-endpoint", {"key": "value"})

        mock_post.assert_called_once_with("http://example.com/test-endpoint", json={"key": "value"})
        assert result == {"key": "value"}

    @patch("src.api.requests.put")
    def test_put_success(self, mock_put, client, mock_response):
        mock_put.return_value = mock_response
        result = client.put("test-endpoint", {"key": "value"})

        mock_put.assert_called_once_with("http://example.com/test-endpoint", json={"key": "value"})
        assert result == {"key": "value"}
