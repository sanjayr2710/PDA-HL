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
            driver_obj = webdriver.Chrome(service=Service(executable_path=binary_path), options=options)
            driver = WebDriverExtended(driver_obj, WebDriverListener(testcase_name), config)
            '''driver = WebDriverExtended(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener(), config
            )'''
            return driver
        raise Exception("Provide valid driver name")
