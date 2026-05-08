import time

from selenium.webdriver.support.ui import (
    WebDriverWait
)

from selenium.webdriver.support import (
    expected_conditions as EC
)

from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)

from config.environment import TIMEOUT


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            TIMEOUT
        )

    def open_url(self, url):

        self.driver.get(url)

    def find_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # This method is to find elements
    # with primary and fallback locators.
    def find_element_with_fallback(
        self,
        primary_locator,
        fallback_locator=None
    ):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    primary_locator
                )
            )

        except TimeoutException:

            if fallback_locator:

                return self.wait.until(
                    EC.visibility_of_element_located(
                        fallback_locator
                    )
                )

            raise

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Safe retry click handling
    def safe_click_with_retry(
        self,
        locator,
        retries=3
    ):

        for attempt in range(retries):

            try:

                element = self.wait.until(
                    EC.element_to_be_clickable(
                        locator
                    )
                )

                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);",
                    element
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                return

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException
            ):

                if attempt == retries - 1:

                    raise

    def type_text(self, locator, text):

        element = self.find_element(locator)

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        return self.find_element(locator).text

    # Get element attribute values
    def get_element_attribute(
        self,
        locator,
        attribute_name
):

        element = self.find_element(
            locator
        )

        return element.get_attribute(
            attribute_name
        )

    # Check whether page is fully loaded
    def is_page_loaded(self, driver):

        return driver.execute_script(
            "return document.readyState"
        ) == "complete"

    # JavaScript page load wait
    def wait_for_page_load(self):

        WebDriverWait(
            self.driver,
            TIMEOUT
        ).until(
            self.is_page_loaded
        )

    # Measure page load performance
    def measure_page_load_time(self):

        start_time = time.time()

        WebDriverWait(
            self.driver,
            TIMEOUT
        ).until(
            self.is_page_loaded
        )

        end_time = time.time()

        return round(
            end_time - start_time,2
        )
    def wait_for_page_ready(self):
        def page_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"

        WebDriverWait(self.driver, 10).until(page_loaded)    