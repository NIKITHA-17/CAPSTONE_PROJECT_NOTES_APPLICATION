import allure

from services.auth_service import AuthService
from services.notes_service import NotesService


def test_get_notes_api():

    token = AuthService().login()

    notes_service = NotesService(token)

    response = notes_service.get_notes()

    allure.attach(
        response.text,
        name="GET Notes API Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200

    assert response.elapsed.total_seconds() < 10

    data = response.json()

    assert "data" in data