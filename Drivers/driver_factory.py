from chromedriver_py import binary_path
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from extenstions.webdriver_extended import WebDriverExtended
from helpers.webdriver_listener import WebDriverListener

class DriverFactory:
    @staticmethod
    def get_driver(config, testcase_name) -> WebDriverExtended:
        if config["browser"] == "chrome":
            # Configure Chrome options
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")  # Required for Linux
            options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resources in containers
            options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration (optional for stability)
            options.add_argument("--window-size=1920,1080")  # Set fixed size for headless
            # options.add_argument("--remote-debugging-port=9222")  # Debugging support if required

            # Enable headless mode if configured
            if config.get("headless_mode", False):
                options.add_argument("--headless")

            # Logging preferences for debugging (optional)
            options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

            # Use WebDriverManager to install the appropriate ChromeDriver
            driver_obj = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options
            )

            # Initialize an extended driver with listener
            driver = WebDriverExtended(driver_obj, WebDriverListener(testcase_name), config)
            return driver

        # Raise exception if a browser type is invalid
        raise Exception("Provide valid driver name")
