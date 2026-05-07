from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.home_page import HomePage

from services.auth_service import AuthService
from services.notes_service import NotesService

from config.environment import TEST_EMAIL, TEST_PASSWORD


def test_ui_to_api_validation(driver):

    note_title = "Hybrid E2E Note"
    note_description = "Created from UI and validated in API"

    # UI FLOW
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_login_page()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    wait = WebDriverWait(driver, 15)

    # Create note from UI
    home_page.create_note(
        note_title,
        note_description
    )

    note_locator = (
        By.XPATH,
        f"//*[contains(text(), '{note_title}')]"
    )

    # Wait until note appears
    wait.until(
        EC.visibility_of_element_located(note_locator)
    )

    assert home_page.is_note_visible(note_title)

    # API FLOW
    token = AuthService().login()

    notes_service = NotesService(token)

    response = notes_service.get_notes()

    assert response.status_code == 200

    notes_data = response.json()["data"]

    matched_note = any(
        note["title"] == note_title and
        note["description"] == note_description
        for note in notes_data
    )

    assert matched_note