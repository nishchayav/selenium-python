import os
import logging
import configparser
import csv
import random
import string
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Utils:

    # ---------------- CONFIG ----------------
    @staticmethod
    def read_config():
        config = configparser.ConfigParser()
        config.read("pytest_framework/config.ini")
        return config


    # ---------------- DRIVER ----------------
    @staticmethod
    def get_driver():
        config = Utils.read_config()

        browser = config["browser"]["name"].lower()
        base_url = config["browser"]["base_url"]
        implicit_wait = int(config["browser"]["implicit_wait"])

        if browser == "edge":
            options = EdgeOptions()
            options.add_argument("--start-maximized")

            driver = webdriver.Edge(options=options)

        elif browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)

        else:
            raise Exception(f"Unsupported Browser: {browser}")

        driver.implicitly_wait(implicit_wait)
        driver.get(base_url)

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        return driver


    # ---------------- LOGGING ----------------
    @staticmethod
    def get_logger(name="automation"):

        reports_path = "pytest_framework/reports"
        if not os.path.exists(reports_path):
            os.makedirs(reports_path)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(f"{reports_path}/automation.log")
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger


    # ---------------- EXPLICIT WAIT ----------------
    @staticmethod
    def wait_for_element(driver, locator, timeout=20):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(
            EC.presence_of_element_located(locator)
        )
        wait.until(
            EC.element_to_be_clickable(locator)
        )
        return element


    # ---------------- SCREENSHOT ----------------
    @staticmethod
    def capture_screenshot(driver, name="screenshot"):

        screenshots_path = "pytest_framework/screenshots"
        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)

        file_path = f"{screenshots_path}/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(file_path)

        return file_path


    # ---------------- RANDOM EMAIL ----------------
    @staticmethod
    def generate_random_email():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"automation_{random_string}_{timestamp}@testmail.com"


    # ---------------- SAVE USER ----------------
    @staticmethod
    def save_user_to_csv(user_data):
        file_path = "pytest_framework/data/registered_users.csv"
        file_exists = os.path.isfile(file_path)

        with open(file_path, mode="a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["first_name", "last_name", "email", "telephone", "password"]
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(user_data)
