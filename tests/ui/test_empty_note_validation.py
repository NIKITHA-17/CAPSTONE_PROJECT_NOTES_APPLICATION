from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.home_page import HomePage

from config.environment import TEST_EMAIL, TEST_PASSWORD


def test_empty_note_validation(driver):

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_login_page()

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD
    )

    wait = WebDriverWait(driver, 15)

    # Wait until notes page loads
    wait.until(
        EC.url_contains("notes")
    )

    # Click Add Note
    home_page.click_add_note()

    # Click Save without entering data
    home_page.click(home_page.SAVE_BUTTON)

    # Verify still on notes page
    assert "notes" in driver.current_url.lower()