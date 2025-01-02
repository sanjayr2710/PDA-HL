import pytest
from Base.page_base import PageBase
from Locators.Login_Locators import LoginPageLocators
from helpers.UtilFuntions import WaitAndAssert, HardWait, XlsReader


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def Login_to_RA(self, username=None, passWord=None):
        self.open()
        loginHilabsLogo = LoginPageLocators.HilabsLOGO
        WaitAndAssert.waitAndAssert(self.driver, loginHilabsLogo, 10)
        self.driver.find_element(*LoginPageLocators.user_id_textbox).click()
        self.driver.find_element(*LoginPageLocators.user_id_textbox).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password_textbox).click()
        self.driver.find_element(*LoginPageLocators.password_textbox).send_keys(passWord)
        HardWait.hard_wait(5)
        self.driver.find_element(*LoginPageLocators.loginBtn).click()
