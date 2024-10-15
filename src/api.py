import requests


class PyAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        """Makes a GET request to the given endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        self._handle_errors(response)
        return response.json()

    def post(self, endpoint, data):
        """Makes a POST request to the given endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        self._handle_errors(response)
        return response.json()

    def put(self, endpoint, data):
        """Makes a PUT request to the given endpoint"""
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        self._handle_errors(response)
        return response.json()

    def _handle_errors(self, response):
        """Handles errors for HTTP responses"""
        if not response.ok:
            raise Exception(
                "API request failed with status code "
                f"{response.status_code}: "
                f"{response.text}"
            )
