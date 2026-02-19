from selenium.webdriver.common.by import By
from pytest_framework.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def search_product(self, product):
        self.send_keys(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)

    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-thumb']//h4/a)[1]")

    def open_first_product(self):
        wait = WebDriverWait(self.driver, 20)

        # Wait for search results to appear
        wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT))

        # Click first product
        wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT)).click()

        # Wait until product details page loads
        wait.until(EC.url_contains("route=product/product"))
