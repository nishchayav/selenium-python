from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ecommerce-playground.lambdatest.io/")

# Search and Add to Cart
search_input = driver.find_element(By.NAME, "search")
search_input.send_keys("HP LP3065")
search_input.submit()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "div.product-thumb h4 a").click()
time.sleep(3)

# Click Add to Cart
btns = driver.find_elements(By.CSS_SELECTOR, ".button-cart")
for b in btns:
    if b.is_displayed():
        driver.execute_script("arguments[0].click();", b)
        break

time.sleep(15)
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# Click Cart Icon
driver.find_element(By.CSS_SELECTOR, ".widget-cart a").click()
time.sleep(2)

# Find and Click Edit Cart
all_links = driver.find_elements(By.TAG_NAME, "a")
for link in all_links:
    if "edit" in link.get_attribute("textContent").lower() and "cart" in link.get_attribute("textContent").lower():
        driver.execute_script("arguments[0].click();", link)
        break

time.sleep(5)
print(f"Title: {driver.title}")

# Find the quantity input
qty_input = driver.find_element(By.CSS_SELECTOR, "input[name^='quantity']")
print(f"Qty Input HTML: {qty_input.get_attribute('outerHTML')}")

# Find parent div and siblings
parent = qty_input.find_element(By.XPATH, "..")
print(f"Parent HTML: {parent.get_attribute('outerHTML')}")

# Try to find the sync/update button within the same table row
row = qty_input.find_element(By.XPATH, "./ancestor::tr")
print(f"Row HTML snippet: {row.get_attribute('outerHTML')[:1000]}")

# Find all buttons in that row
row_btns = row.find_elements(By.TAG_NAME, "button")
for b in row_btns:
    print(f"Row Button: Class='{b.get_attribute('class')}', Title='{b.get_attribute('title')}', HTML='{b.get_attribute('outerHTML')}'")

driver.quit()
