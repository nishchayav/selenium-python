from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pytest_framework.pages.base_page import BasePage


class ProductPage(BasePage):

    FIRST_PRODUCT_CARD = (By.XPATH, "(//div[contains(@class,'product-thumb')])[1]")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//div[contains(@class,'product-thumb')]//button[@title='Add to Cart'])[1]")

    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "#notification-box-top a.btn.btn-primary")
    SUCCESS_TOAST = (By.CSS_SELECTOR, "#notification-box-top .toast")


    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 20)

        # Wait for search results to load
        product_card = wait.until(
            EC.visibility_of_element_located(self.FIRST_PRODUCT_CARD)
        )

        # Hover over product card
        ActionChains(self.driver).move_to_element(product_card).perform()

        # Wait for overlay button to appear and click
        wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

        # Wait for popup
        wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST)
        )

        # Click View Cart inside popup
    """ wait.until(
            EC.element_to_be_clickable(self.VIEW_CART_BUTTON)
        ).click()

        wait.until(
            EC.url_contains("route=checkout/cart")
        )"""

    def get_success_message(self):
        wait = WebDriverWait(self.driver, 10)
        success_toast = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#notification-box-top .toast-body")
            )
        )
        return success_toast.text

    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(
            EC.element_to_be_clickable(self.VIEW_CART_BUTTON)
        ).click()

        wait.until(
            EC.url_contains("route=checkout/cart")
        )
