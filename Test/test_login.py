import unittest
import pytest
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from helpers.UtilFuntions import XlsReader, WaitAndAssert, HardWait
from Locators.Login_Locators import LoginPageLocators
from Locators.ExecutiveDashboardLocators import ExecutiveDashboardPageLocators
from Locators.RAMainPage_Locators import RAMainPage_Locators
from Locators.RosterTracker_Locators import RosterTrackerLocatorsL1
from helpers.UtilFuntions import helpersUtil


@pytest.mark.usefixtures("setup")
class TestLogin(unittest.TestCase):
    # TC01	Verify that on entering valid username and password home page with executive dashboard is displayed
    def test_Login_success(self):
        login = LoginPage(self.driver)
        login.open()
        # Read data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)

    #  TC02	Verify that on entering invalid username and password home page is not displayed
    def test_Login_Failure(self):
        login = LoginPage(self.driver)
        login.open()
        # Read data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'INVALIDCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.HilabsLOGO, 10)

    # TC03	Verify when user login with EH user creds, Application should display only EH data
    def test_Login_successForEH(self):
        login = LoginPage(self.driver)
        login.open()
        # Read data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        self.driver.find_element(*RAMainPage_Locators.rosterTrackerMenu).click()
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        HardWait.hard_wait(10)
        TicketNo = self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoReadTableData)
        ROID = TicketNo.text
        print(ROID)
        replaceROID = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.TicketNoWriteTableData, ROID)
        if 'EH' in ROID:
            AssertTicketNo = self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoReadTableData)
            is_visible = AssertTicketNo.is_displayed()
            assert is_visible, f"Element found"
        else:
            element = self.driver.find_element(By.XPATH, replaceROID)
            is_visible = element.is_displayed()
            assert not is_visible, f"Element is not visible"

    # TC04	Verify when user login with Molina user creds, Application should display only Molina data
    def test_Login_successForMolina(self):
        login = LoginPage(self.driver)
        login.open()
        # Read data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        self.driver.find_element(*RAMainPage_Locators.rosterTrackerMenu).click()
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        HardWait.hard_wait(10)
        TicketNo = self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoReadTableData)
        ROID = TicketNo.text
        print(ROID)
        replaceROID = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.TicketNoWriteTableData, ROID)
        if 'EH' in ROID:
            AssertTicketNo = self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoReadTableData)
            is_visible = AssertTicketNo.is_displayed()
            assert is_visible, f"Element found"
        else:
            element = self.driver.find_element(By.XPATH, replaceROID)
            is_visible = element.is_displayed()
            assert not is_visible, f"Element is not visible"

    # TC05	Verify in Login page that, user_id(textbox), password, Login(btn) elements are displayed
    def test_ElementPresence(self):
        login = LoginPage(self.driver)
        login.open()
        HardWait.hard_wait(10)

        # Assert if elements are displayed
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.HilabsLOGO, 10)
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.user_id_textbox, 10)
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.password_textbox, 10)
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.loginBtn, 10)
