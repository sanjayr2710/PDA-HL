import pytest
from Base.page_base import PageBase
from Locators.Login_Locators import LoginPageLocators
from helpers.UtilFuntions import WaitAndAssert, HardWait, XlsReader


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "http://10.60.0.62:83/auth/login"  # Replace with the actual login URL

    def open(self):
        super().open(self.base_url)

    def Login_to_RA(self, username=None, password=None):
        self.open()
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.HilabsLOGO, 10)
        self.driver.find_element(*LoginPageLocators.user_id_textbox).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password_textbox).send_keys(password)
        HardWait.hard_wait(5)
        self.driver.find_element(*LoginPageLocators.loginBtn).click()
