from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def type_text(self, locator, text):

        element = self.find_element(locator)

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        return self.find_element(locator).text

    # JavaScript page load wait
    def wait_for_page_load(self):

        WebDriverWait(
            self.driver,
            TIMEOUT
        ).until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )