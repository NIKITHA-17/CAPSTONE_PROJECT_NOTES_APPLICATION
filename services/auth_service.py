from services.api_client import APIClient
from config.environment import TEST_EMAIL, TEST_PASSWORD


class AuthService:

    def __init__(self):
        self.client = APIClient()

    def login(self):
        payload = {
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }

        response = self.client.post("/users/login", json=payload)
        assert response.status_code == 200

        data = response.json()
        return data["data"]["token"]