import pytest

class PageBase:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.open()