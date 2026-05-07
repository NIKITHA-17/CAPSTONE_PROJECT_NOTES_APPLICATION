from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.home_page import HomePage

from config.environment import (
    TEST_EMAIL,
    TEST_PASSWORD
)


def test_create_note_via_ui(driver):

    login_page = LoginPage(driver)

    home_page = HomePage(driver)

    note_title = "QA Automation Note"

    note_description = (
        "This note is created using Selenium Python Pytest."
    )

    # Open login page
    login_page.open_login_page()

    login_page.wait_for_page_load()

    # Login
    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD
    )

    wait = WebDriverWait(driver, 15)

    # Wait until notes page loads
    wait.until(
        EC.url_contains("notes")
    )

    home_page.wait_for_page_load()

    # Create note
    home_page.create_note(
        note_title,
        note_description
    )

    note_locator = (
        By.XPATH,
        f"//*[contains(text(), '{note_title}')]"
    )

    # Wait until note appears dynamically
    wait.until(
        EC.visibility_of_element_located(
            note_locator
        )
    )

    # Validate note visible in UI
    assert home_page.is_note_visible(
        note_title
    )

    # Validate DOM updated without refresh
    assert note_title in driver.page_source