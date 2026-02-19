from pytest_framework.pages.home_page import HomePage
from pytest_framework.pages.product_page import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_add_product_to_cart(driver, csv_row):
    product_name = csv_row["search_product"]
    quantity = csv_row["quantity"]


    home = HomePage(driver)
    home.search_product(product_name)

    product = ProductPage(driver)
    product.add_to_cart()

    cart_item = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, product_name))
    )

    assert cart_item.is_displayed()