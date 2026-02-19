from time import sleep

from selenium.webdriver.common.by import By
from pytest_framework.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CartPage(BasePage):

    CART = (By.XPATH, "//button[contains(@class,'btn-inverse')]")
    VIEW_CART = (By.XPATH, "//strong[text()=' View Cart']")
    QUANTITY = (By.XPATH, "//input[contains(@name,'quantity')]")
    UPDATE_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class,'btn-primary')]")
    REMOVE_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class,'btn-danger')]")

    def __init__(self, driver):
        self.driver = driver

    def is_product_in_cart(self, product_name):
        return self.driver.find_element(By.LINK_TEXT, product_name).is_displayed()

    def update_quantity(self, qty):
        wait = WebDriverWait(self.driver, 20)

        # Wait for quantity field
        quantity_field = wait.until(
            EC.presence_of_element_located(self.QUANTITY)
        )

        # Clear and set new quantity
        quantity_field.clear()
        quantity_field.send_keys(qty)

        # Wait for update button presence
        update_button = wait.until(
            EC.presence_of_element_located(self.UPDATE_BUTTON)
        )

        # Scroll to button
        self.driver.execute_script("arguments[0].scrollIntoView(true);", update_button)

        # Click using JS (more reliable)
        self.driver.execute_script("arguments[0].click();", update_button)
        sleep(5)

    def remove_product(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        ).click()

        # wait for cart to become empty or success alert
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".alert-success")
            )
        )
        sleep(5)






