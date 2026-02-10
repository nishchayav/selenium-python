'''	Question – Automation Framework (POM)
Write a Selenium automation framework that:
1. Implements Page Object Model (POM)
2. Separates page classes, test scripts, and configuration
3. Creates reusable methods for common actions (click, input, select)
4. Runs a test using pytest or unittest and prints results	'''


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge()
driver.get("https://letcode.in/frame")
driver.implicitly_wait(10)

iframe=driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.NAME,"fname").send_keys("Nishhh")
driver.find_element(By.NAME,"lname").send_keys("Vishhh")
sleep(5)
driver.switch_to.default_content()
insight=driver.find_element(By.XPATH,"//p[text()=' Insight ']").is_displayed()
print("insight is displayed:",insight)