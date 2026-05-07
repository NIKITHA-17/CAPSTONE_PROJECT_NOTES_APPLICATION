from services.api_client import APIClient
from config.environment import TEST_EMAIL, TEST_PASSWORD


def test_api_login():
    client = APIClient()

    payload = {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    }

    response = client.post("/users/login", json=payload)

    assert response.status_code == 200
    assert "token" in response.text