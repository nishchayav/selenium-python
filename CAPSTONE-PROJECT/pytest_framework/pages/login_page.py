from selenium.webdriver.common.by import By
from pytest_framework.pages.base_page import BasePage
from pytest_framework.utils import Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    MY_ACCOUNT = (By.XPATH, "//a[@data-toggle='dropdown']//span[contains(text(),'My account')]")
    REGISTER = (By.LINK_TEXT, "Register")
    LOGIN = (By.LINK_TEXT, "Login")

    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM = (By.ID, "input-confirm")
    AGREE = (By.NAME, "agree")
    CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")
    SUCCESS_CONTINUE = (By.LINK_TEXT, "Continue")

    LOGIN_EMAIL = (By.ID, "input-email")
    LOGIN_PASSWORD = (By.ID, "input-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[value='Login']")

    def register_user(self, user):
        self.click(self.MY_ACCOUNT)
        self.click(self.REGISTER)

        self.send_keys(self.FIRST_NAME, user["first_name"])
        self.send_keys(self.LAST_NAME, user["last_name"])
        self.send_keys(self.EMAIL, user["email"])
        self.send_keys(self.TELEPHONE, user["telephone"])
        self.send_keys(self.PASSWORD, user["password"])
        self.send_keys(self.CONFIRM, user["password"])
        agree_checkbox = self.driver.find_element(*self.AGREE)
        self.driver.execute_script("arguments[0].click();", agree_checkbox)

        self.click(self.CONTINUE)


    def login_user(self, email, password):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT)).click()
        wait.until(EC.element_to_be_clickable(self.LOGIN)).click()

        wait.until(EC.presence_of_element_located(self.LOGIN_EMAIL)).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

        # Wait until account page loads
        wait.until(EC.url_contains("account"))

