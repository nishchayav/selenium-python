from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()


driver.implicitly_wait(10)


search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("MacBook")


wait = WebDriverWait(driver, 10)
search_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default.btn-lg"))
)

print("Explicit wait: Search button is clickable")
search_button.click()


fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,        # polling every 2 seconds
    ignored_exceptions=[Exception]
)

product = fluent_wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h4/a"))
)


print("Fluent wait: Product is available for interaction ->", product.text)

time.sleep(3)
driver.quit()
