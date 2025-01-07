import pytest

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        if not url:
            raise ValueError("URL must be provided to open the page.")
        self.driver.get(url)
