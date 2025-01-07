import pytest
import unittest
from Pages.LoginPage import LoginPage
from helpers.UtilFuntions import WaitAndAssert
from Locators.ExecutiveDashboardLocators import ExecutiveDashboardPageLocators


@pytest.mark.usefixtures("setup")
class TestLogin(unittest.TestCase):
    def test_Login_success(self):
        login = LoginPage(self.driver)
        login.Login_to_RA(username="test_user", password="test_password")
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
