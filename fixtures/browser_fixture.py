import os

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

    grid_url = os.getenv("GRID_URL")

    if grid_url:

        driver = webdriver.Remote(

            command_executor=grid_url,

            options=chrome_options,

            keep_alive=True
        )

    else:

        driver = webdriver.Chrome(
            options=chrome_options
        )

    driver.implicitly_wait(5)

    yield driver

    driver.quit()