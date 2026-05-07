from selenium.common.exceptions import TimeoutException


class SelfHealingLocator:

    def __init__(self, page):
        self.page = page

    def find_with_fallback(self, locators):
        
        for locator in locators:
            try:
                return self.page.find_element(locator)
            except TimeoutException:
                continue

        raise TimeoutException("All locator strategies failed")