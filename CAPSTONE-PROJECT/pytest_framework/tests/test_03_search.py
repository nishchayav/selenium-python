from pytest_framework.pages.home_page import HomePage

def test_search_and_view_product(driver, test_data):
    home = HomePage(driver)
    home.search_product(test_data["search_product"])

    # Assert search result page loaded
    assert test_data["search_product"] in driver.page_source

    # Assert product detail page opened
    assert "Add to Cart" in driver.page_source
    home.open_first_product()