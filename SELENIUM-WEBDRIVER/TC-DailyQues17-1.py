'''
Write a Selenium script that:
1. Fills text boxes
2. Selects radio buttons and checkboxes
3. Chooses an option from a drop-down list using the Select class
4. Submits the form and verifies a confirmation message
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


wait = WebDriverWait(driver, 10)

text_box = wait.until(EC.element_to_be_clickable((By.NAME, "my-text")))
text_box.send_keys("Selenium Automation")
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("test123")


radio_button = driver.find_element(By.ID, "my-radio-1")
radio_button.click()


checkbox = driver.find_element(By.ID, "my-check-1")
checkbox.click()


dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")
sleep(5)

submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
submit_button.click()

message = wait.until(EC.visibility_of_element_located((By.ID, "message"))).text
print("Confirmation Message:", message)

assert "Received!" in message

time.sleep(3)
driver.quit()
