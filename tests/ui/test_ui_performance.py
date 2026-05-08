import logging

import allure

from pages.login_page import LoginPage

from config.environment import (
    TEST_EMAIL,
    TEST_PASSWORD
)

logger = logging.getLogger(__name__)


def test_ui_page_load_performance(driver):

    login_page = LoginPage(driver)

    login_page.open_login_page()

    page_load_time = (
        login_page.measure_page_load_time()
    )

    logger.info(
        f"UI Performance | Page Load Time: "
        f"{page_load_time} seconds"
    )

    allure.attach(
        str(page_load_time),
        name="UI Page Load Time",
        attachment_type=allure.attachment_type.TEXT
    )

    print(
        f"\nPage Load Time: "
        f"{page_load_time} seconds"
    )

    # Basic performance validation
    assert page_load_time < 5

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD
    )
