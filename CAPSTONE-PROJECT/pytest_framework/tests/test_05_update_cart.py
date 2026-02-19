from pytest_framework.pages.home_page import HomePage
from pytest_framework.pages.product_page import ProductPage
from pytest_framework.pages.cart_page import CartPage

def test_update_cart_quantity_and_remove(driver, csv_row):
    home = HomePage(driver)
    home.search_product(csv_row["search_product"])

    product = ProductPage(driver)
    product.add_to_cart()

    success_message = product.get_success_message()
    assert "Success" in success_message

    product.go_to_cart()
    cart = CartPage(driver)

    cart.update_quantity(csv_row["quantity"])
    assert "Success" in driver.page_source

    cart.remove_product()
    assert "Your shopping cart is empty!" in driver.page_source
