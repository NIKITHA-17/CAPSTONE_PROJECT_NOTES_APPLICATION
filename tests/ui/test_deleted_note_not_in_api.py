from services.auth_service import AuthService
from services.notes_service import NotesService


def test_deleted_note_not_present_in_api():

    token = AuthService().login()

    notes_service = NotesService(token)

    payload = {
        "title": "Temporary Delete Check",
        "description": "Delete validation",
        "category": "Home"
    }

    create_response = notes_service.create_note(payload)

    note_id = create_response.json()["data"]["id"]

    delete_response = notes_service.delete_note(note_id)

    assert delete_response.status_code in [200, 204]

    notes_response = notes_service.get_notes()

    notes_data = notes_response.json()["data"]

    deleted_note_exists = any(
        note["id"] == note_id
        for note in notes_data
    )

    assert not deleted_note_exists