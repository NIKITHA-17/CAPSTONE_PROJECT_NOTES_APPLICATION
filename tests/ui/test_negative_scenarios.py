from services.api_client import APIClient
from services.auth_service import AuthService
from services.notes_service import NotesService
from config.environment import TEST_EMAIL


def test_invalid_api_login():
    client = APIClient()

    payload = {
        "email": TEST_EMAIL,
        "password": "WrongPassword123"
    }

    response = client.post("/users/login", json=payload)

    assert response.status_code in [400, 401]
    assert response.json() is not None


def test_get_notes_without_token():
    client = APIClient()

    response = client.get("/notes")

    assert response.status_code in [401, 403]


def test_create_note_with_empty_payload():
    token = AuthService().login()
    notes_service = NotesService(token)

    payload = {}

    response = notes_service.client.post(
        "/notes",
        json=payload,
        headers=notes_service.headers
    )

    assert response.status_code in [400, 422]


def test_delete_note_with_invalid_id():
    token = AuthService().login()
    notes_service = NotesService(token)

    invalid_note_id = "invalid123"

    response = notes_service.delete_note(invalid_note_id)

    assert response.status_code in [400, 404]