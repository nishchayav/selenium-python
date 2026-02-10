from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


from DAY18loginpagePOM import LoginPage


driver = webdriver.Edge()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
loginobj=LoginPage(driver)

loginobj.enteruser("Admin")
loginobj.enterpwd("admin123")
sleep(5)
loginobj.clicklogin()