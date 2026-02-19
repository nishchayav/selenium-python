from selenium.webdriver.common.by import By
from pytest_framework.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutPage(BasePage):

    MY_ACCOUNT = (By.XPATH, "//a[@data-toggle='dropdown']//span[contains(text(),'My account')]")
    LOGOUT = (By.LINK_TEXT, "Logout")
    LOGOUT_HEADER = (By.CSS_SELECTOR, "h1.page-title")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")

    def logout(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT)).click()
        wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        wait.until(EC.visibility_of_element_located(self.LOGOUT_HEADER))
        time.sleep(5)

    def is_logout_successful(self):
        return "Account Logout" in self.driver.page_source
