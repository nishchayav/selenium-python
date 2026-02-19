import pytest
import json
import csv
from pytest_framework.utils import Utils


@pytest.fixture(scope="function")
def driver():
    driver = Utils.get_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def test_data():
    with open("pytest_framework/data/testdata.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def registered_user():
    user_data = {
        "first_name": "John",
        "last_name": "Automation",
        "email": Utils.generate_random_email(),
        "telephone": "9999999999",
        "password": "Test@123"
    }

    return user_data



def pytest_generate_tests(metafunc):
    if "csv_row" in metafunc.fixturenames:
        data = []

        with open("pytest_framework/data/testdata.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
                data.append(cleaned_row)

        metafunc.parametrize("csv_row", data)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if report.passed:
            print(f"\n✅ {item.name} PASSED")

        elif report.failed:
            print(f"\n❌ {item.name} FAILED")

            driver = item.funcargs.get("driver", None)
            if driver:
                screenshot_path = Utils.capture_screenshot(driver, item.name)
                print(f"📸 Screenshot saved at: {screenshot_path}")
