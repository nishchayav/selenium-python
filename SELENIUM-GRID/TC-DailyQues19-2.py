from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

GRID_URL = "http://192.168.1.6:4444"

browsers = [
    ("edge", "WINDOWS"),
    ("firefox", "WINDOWS")
]

for browser, platform in browsers:
    print("\nStarting test on:", browser)

    if browser == "edge":
        options = EdgeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()

    options.set_capability("platformName", platform)

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.get("https://example.com")

    # Verify page title
    title = driver.title
    assert "Example Domain" in title

    # Print execution details
    print("Browser Name:", browser)
    print("Platform:", platform)
    print("Page Title:", title)

    driver.quit()
