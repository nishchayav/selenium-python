from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.amazon.in")
sleep(5)
driver.execute_script("alert('Hello, this is bcs of Java Script Executor')")
sleep(5)
driver.execute_script("window.scrollBy(0,1000)")
sleep(5)
