'''Write a Selenium WebDriver script that:
1. Opens a browser and navigates to https://example.com
2. Navigates to another page on the same site
3. Uses back(), forward(), and refresh()
4. Prints the page title after each navigation
5. Closes the browser	'''

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Edge()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
print("title is",driver.title)
driver.get("https://www.google.com")
print("title is",driver.title)
time.sleep(5)
driver.back()
print("title after back",driver.title)
driver.forward()
print("title after forward",driver.title)
driver.quit()