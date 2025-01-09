import unittest
import pytest

from Pages.LoginPage import LoginPage
from helpers.UtilFuntions import XlsReader, WaitAndAssert, HardWait
from Locators.BCBSMA.ExecutiveDashboardLocators import ExecutiveDashboardPageLocators


@pytest.mark.usefixtures("setup")
class TestLogin(unittest.TestCase):
    # TC01	Verify that on entering valid username and password home page with executive dashboard is displayed
    def test_Login_success(self):
        login = LoginPage(self.driver)
        login.open()
        # Read data from Excel
        file_path1 = "C:/Users/sanjay.r/OneDrive - H-Ilabs/Desktop/DV/Pytest/PDA-HL/PDA-VDI/PDA-HL/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)

