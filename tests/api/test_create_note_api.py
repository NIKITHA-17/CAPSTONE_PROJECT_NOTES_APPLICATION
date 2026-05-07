from services.auth_service import AuthService
from services.notes_service import NotesService


def test_create_note_api():
    token = AuthService().login()
    notes_service = NotesService(token)

    payload = {
        "title": "API Automation Note",
        "description": "This note is created using API automation.",
        "category": "Home"
    }

    response = notes_service.client.post(
        "/notes",
        json=payload,
        headers=notes_service.headers
    )

    assert response.status_code in [200, 201]

    data = response.json()
    assert "data" in data
    assert data["data"]["title"] == payload["title"]