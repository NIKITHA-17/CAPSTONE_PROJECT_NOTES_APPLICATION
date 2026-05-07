from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.home_page import HomePage

from services.auth_service import AuthService
from services.notes_service import NotesService

from config.environment import TEST_EMAIL, TEST_PASSWORD


def test_api_delete_note_reflected_in_ui(driver):

    note_title = "Delete E2E Note"
    note_description = "This note will be deleted using API"

    # API Login
    token = AuthService().login()
    notes_service = NotesService(token)

    # Create note using API
    payload = {
        "title": note_title,
        "description": note_description,
        "category": "Home"
    }

    create_response = notes_service.create_note(payload)

    assert create_response.status_code in [200, 201]

    note_id = create_response.json()["data"]["id"]

    # UI Login
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_login_page()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    wait = WebDriverWait(driver, 15)

    note_locator = (
        By.XPATH,
        f"//*[contains(text(), '{note_title}')]"
    )

    # Wait until note appears
    wait.until(
        EC.visibility_of_element_located(note_locator)
    )

    assert home_page.is_note_visible(note_title)

    # Delete note using API
    delete_response = notes_service.delete_note(note_id)

    assert delete_response.status_code in [200, 204]

    # Refresh page
    driver.refresh()

    # Wait until note disappears
    wait.until(
        EC.invisibility_of_element_located(note_locator)
    )

    assert not home_page.is_note_visible(note_title)