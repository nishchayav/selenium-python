from selenium.webdriver.common.by import By
from pytest_framework.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LogoutPage(BasePage):

    SIDEBAR_LOGOUT = (By.XPATH, "//a[contains(@href,'route=account/logout') and contains(@class,'list-group-item')]")

    LOGOUT_HEADER = (By.XPATH, "//h1[contains(text(),'Account Logout')]")

    def logout(self):
        wait = WebDriverWait(self.driver, 20)

        # Ensure login
        wait.until(EC.url_contains("account"))

        wait.until(
            EC.element_to_be_clickable(self.SIDEBAR_LOGOUT)
        ).click()

        # for logout
        wait.until(
            EC.visibility_of_element_located(self.LOGOUT_HEADER)
        )

    def is_logout_successful(self):
        return "Account Logout" in self.driver.page_source
