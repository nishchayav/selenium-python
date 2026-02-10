import pytest

from TC01_DAY20_driverfac import getdriver

@pytest.mark.parametrize("browser",["chrome","firefox","edge"])
def test_google_title(browser):
    driver=getdriver(browser)
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_google_serach(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com/")
    serachbox=driver.find_element("name","q")
    serachbox.send_keys("Selenium Grid")
    serachbox.submit()
    assert "selenium grid" in driver.title.lower()

    driver.quit()
