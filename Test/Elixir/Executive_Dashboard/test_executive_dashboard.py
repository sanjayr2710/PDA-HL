import unittest
import pytest
from Pages.Elixir.LoginPage import LoginPage
from helpers.UtilFuntions import XlsReader, WaitAndAssert, HardWait


@pytest.mark.usefixtures("test_setup")
class TestLogin(unittest.TestCase):
    def test_Login_success(self):
        login = LoginPage(self.driver)
        login.Login_to_PDA()
        HardWait.hard_wait(2)
        # WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        login.Logout_from_PDA()

    def test_NavigateToExecutiveDB(self):
        login = LoginPage(self.driver)
        login.Login_to_PDA()
        HardWait.hard_wait(2)
        # WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        # self.driver.find_element(*ExecutiveDashboardPageLocators.executiveDashboardBtn).click()
        # WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.EDHeading, 10)
        login.Logout_from_PDA()

