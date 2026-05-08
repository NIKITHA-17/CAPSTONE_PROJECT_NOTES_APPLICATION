import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import (
    Options
)


@pytest.fixture
def driver():

    chrome_options = Options()

    chrome_options.add_argument(
        "--start-maximized"
    )

    chrome_options.add_argument(
        "--no-sandbox"
    )

    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )

    driver = webdriver.Remote(

        command_executor=
        "http://localhost:4444/wd/hub",

        options=chrome_options,

        keep_alive=True
    )

    driver.implicitly_wait(5)

    yield driver

    driver.quit()