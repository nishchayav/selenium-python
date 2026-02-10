'''	Question– Handling iFrames and Windows
Write a Selenium script that:
1. Switches to an iframe and enters text in an input field inside it
2. Switches back to the main content
3. Opens a new browser window or tab
4. Switches between windows and prints each window title
5. Closes the child window and returns to the parent'''


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