from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import platform
import os


class DriverFactory:
    @staticmethod
    def get_chrome_version():
        """
        Get the installed Chrome version based on the operating system.
        """
        if platform.system() == "Windows":
            try:
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                if not os.path.exists(chrome_path):
                    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                version_output = subprocess.check_output([chrome_path, "--version"], stderr=subprocess.STDOUT)
                return version_output.decode("utf-8").strip().split()[-1]
            except Exception as e:
                raise RuntimeError("Unable to locate Chrome version on Windows.") from e
        elif platform.system() == "Linux":
            try:
                version_output = subprocess.check_output(["google-chrome", "--version"], stderr=subprocess.STDOUT)
                return version_output.decode("utf-8").strip().split()[-1]
            except Exception as e:
                raise RuntimeError("Unable to locate Chrome version on Linux.") from e
        else:
            raise RuntimeError(f"Unsupported OS: {platform.system()}")

    @staticmethod
    def get_driver(config, testcase_name):
        if config["browser"] == "chrome":
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            if config.get("headless_mode", False):
                options.add_argument("--headless")

            # Use ChromeDriverManager to automatically handle the driver
            driver_path = ChromeDriverManager().install()

            driver_obj = webdriver.Chrome(service=Service(driver_path), options=options)
            return driver_obj

        raise Exception("Provide valid driver name")
