from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


# custom class for selenium expected condition
# checks if element's text is not empty
class wait_for_non_empty_text(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = EC._find_element(driver, self.locator)
            if element.text.strip() != "":
                return element
            else:
                return False
        except StaleElementReferenceException:
            return False
