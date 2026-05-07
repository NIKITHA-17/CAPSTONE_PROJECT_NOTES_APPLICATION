import requests
from config.environment import API_BASE_URL


class APIClient:

    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()

    def post(self, endpoint, json=None, headers=None):
        return self.session.post(
            self.base_url + endpoint,
            json=json,
            headers=headers
        )

    def get(self, endpoint, headers=None):
        return self.session.get(
            self.base_url + endpoint,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return self.session.delete(
            self.base_url + endpoint,
            headers=headers
        )