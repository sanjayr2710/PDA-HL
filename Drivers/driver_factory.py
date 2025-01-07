from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from extenstions.webdriver_extended import WebDriverExtended
from helpers.webdriver_listener import WebDriverListener


class DriverFactory:
    @staticmethod
    def get_driver(config, testcase_name) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")  # Required for Linux
                options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resources in containers
                options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration (optional for stability)
                options.add_argument("--window-size=1920,1080")  # Set fixed size for headless
                options.add_argument("--remote-debugging-port=9222")  # Debugging support if required
            driver_obj = webdriver.Chrome(service=Service(executable_path=binary_path), options=options)
            driver = WebDriverExtended(driver_obj, WebDriverListener(testcase_name), config)
            '''driver = WebDriverExtended(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener(), config
            )'''
            return driver
        raise Exception("Provide valid driver name")
