"""ALERTS"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
#Hey! Welcome to LetCode


driver = webdriver.Edge()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID, "accept").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(5)
driver.quit()




#Are you happy with LetCode?


driver = webdriver.Edge()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID, "confirm").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(5)
driver.quit()




#Enter your name


driver = webdriver.Edge()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID, "prompt").click()
alert=driver.switch_to.alert
print(alert.text)
alert.send_keys("Nishchaya")
alert.accept()
sleep(5)
driver.quit()
'''

#


driver = webdriver.Edge()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID, "modern").click()
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()
sleep(5)
driver.quit()