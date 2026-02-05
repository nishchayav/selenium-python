'''
Write a Selenium script that:
1.Triggers a Python alert
2.Accepts the alert and prints its message
3.Dismisses a confirmation pop - up
4.Enters text in a prompt alert and accepts it
5.Verifies the result displayed on the page
'''


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID, "accept").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
sleep(5)


driver.find_element(By.ID, "prompt").click()
alert=driver.switch_to.alert
print(alert.text)
alert.send_keys("Nishchaya")
alert.accept()
sleep(5)
driver.quit()