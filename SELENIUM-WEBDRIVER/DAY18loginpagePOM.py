from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username =(By.NAME, "username")
    password =(By.NAME, "password")
    loginBtn = (By.XPATH, "//button[@type='submit']")

    def enteruser(self,user):
        self.driver.find_element(*self.username).send_keys("Admin")

    def enterpwd(self,pwd):
        self.driver.find_element(*self.password).send_keys("admin123")

    def clicklogin(self):
        self.driver.find_element(*self.loginBtn).click()
