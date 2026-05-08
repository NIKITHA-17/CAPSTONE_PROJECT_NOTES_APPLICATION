import allure

from services.auth_service import AuthService
from services.notes_service import NotesService


def test_get_notes_api():

    token = AuthService().login()

    notes_service = NotesService(token)

    response = notes_service.get_notes()

    response_time = (
        response.elapsed.total_seconds()
    )

    allure.attach(
        response.text,
        name="GET Notes API Response",
        attachment_type=allure.attachment_type.JSON
    )

    allure.attach(
        str(response_time),
        name="API Response Time",
        attachment_type=allure.attachment_type.TEXT
    )

    print(
        f"\nAPI Response Time: "
        f"{response_time} seconds"
    )

    assert response.status_code == 200

    # Performance validation
    assert response_time < 10

    data = response.json()

    assert "data" in data