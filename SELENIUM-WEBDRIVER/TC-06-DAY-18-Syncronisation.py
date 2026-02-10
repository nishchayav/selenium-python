from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Edge()
#driver.implicitly_wait(10)
wait=WebDriverWait(driver,5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

element=wait.until(expected_conditions.element_to_be_clickable((By.NAME,"username")))
element.send_keys("Admin")
#time.sleep(5)
#driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()