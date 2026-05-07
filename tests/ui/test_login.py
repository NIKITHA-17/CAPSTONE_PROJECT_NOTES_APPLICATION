from pages.login_page import LoginPage
from config.environment import TEST_EMAIL, TEST_PASSWORD
from utils.logger import get_logger


logger = get_logger(__name__)


def test_valid_login(driver):

    logger.info("Starting valid login test")

    login_page = LoginPage(driver)

    login_page.open_login_page()
    logger.info("Login page opened")

    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    logger.info("Login submitted with valid credentials")

    assert "notes" in driver.current_url.lower()

    logger.info("Valid login test passed")


def test_invalid_login(driver):

    logger.info("Starting invalid login test")

    login_page = LoginPage(driver)

    login_page.open_login_page()
    logger.info("Login page opened")

    login_page.login(
        "invalid@gmail.com",
        "wrongpassword"
    )

    logger.info("Login submitted with invalid credentials")

    assert "login" in driver.current_url.lower()

    logger.info("Invalid login test passed")