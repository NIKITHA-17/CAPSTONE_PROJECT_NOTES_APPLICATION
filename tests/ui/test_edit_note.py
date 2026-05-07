from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from config.environment import TEST_EMAIL, TEST_PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)


def test_edit_note(driver):

    logger.info("Starting edit note test")

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD
    )

    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.url_contains("notes")
    )

    logger.info("Login successful")

    # Click EDIT button specifically
    edit_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(text(),'Edit')]"
            )
        )
    )

    # JS click to avoid click interception
    driver.execute_script(
        "arguments[0].click();",
        edit_button
    )

    logger.info("Clicked Edit button")

    # Wait for title input in modal
    title_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "title")
        )
    )

    title_input.clear()

    updated_title = "Updated Hybrid E2E Note"

    title_input.send_keys(
        updated_title
    )

    logger.info("Updated title")

    # Description
    description_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "description")
        )
    )

    description_input.clear()

    description_input.send_keys(
        "Updated using Selenium automation"
    )

    logger.info("Updated description")

    # Save button
    save_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[text()='Save']"
            )
        )
    )

    # JS click for save
    driver.execute_script(
        "arguments[0].click();",
        save_button
    )

    logger.info("Clicked Save")

    # Verify updated note visible
    updated_note = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                f"//*[contains(text(), '{updated_title}')]"
            )
        )
    )

    assert updated_note.is_displayed()

    logger.info("Edit note test passed")