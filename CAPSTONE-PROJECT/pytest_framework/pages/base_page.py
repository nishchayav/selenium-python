from pytest_framework.utils import Utils

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        Utils.wait_for_element(self.driver, locator).click()

    def send_keys(self, locator, text):
        element = Utils.wait_for_element(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return Utils.wait_for_element(self.driver, locator).text
