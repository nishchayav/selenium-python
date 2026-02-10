from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    @property
    def username(self):
        return self.driver.find_element(By.NAME,"username")

    @property
    def password(self):
        return self.driver.find_element(By.NAME,"password")

    @property
    def loginBtn(self):
        return self.driver.find_element(By.XPATH,"//button[@type='submit']")




    def enteruser(self,user):
        self.username.send_keys(user)

    def enterpwd(self,pwd):
        self.password.send_keys(pwd)

    def clicklogin(self):
        self.loginBtn.click()
