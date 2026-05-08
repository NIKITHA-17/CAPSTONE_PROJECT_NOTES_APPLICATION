import os
import pytest
import allure

from datetime import datetime


pytest_plugins = [
    "fixtures.browser_fixture"
]


# Screenshot capture on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    # Capture screenshot only if test fails
    if (
        report.when == "call"
        and report.failed
    ):

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

            screenshots_dir = (
                "screenshots"
            )

            os.makedirs(
                screenshots_dir,
                exist_ok=True
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_name = (
                f"{item.name}_{timestamp}.png"
            )

            screenshot_path = os.path.join(
                screenshots_dir,
                screenshot_name
            )

            driver.save_screenshot(
                screenshot_path
            )

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_{timestamp}",
                attachment_type=
                allure.attachment_type.PNG
            )

            print(
                f"\nScreenshot saved: "
                f"{screenshot_path}"
            )