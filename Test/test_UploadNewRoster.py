import unittest
import pytest
from Pages.LoginPage import LoginPage
from helpers.UtilFuntions import XlsReader, WaitAndAssert, HardWait
from Locators.UploadPageLocators import uploadPageLocators
from Locators.RAMainPage_Locators import RAMainPage_Locators
from Pages.UploadNewRosterPage import UploadNewRosterPage


@pytest.mark.usefixtures("setup")
class TestUploadNewRoster(unittest.TestCase):
    # TC01	Verify the element presence in the upload page(Market, Lob, OrgName, TIN, NPI, choose file and upload btn)
    def test_element_presence(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'UserCreds', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.uploadRosterMenu, 10)
        self.driver.find_element(*RAMainPage_Locators.uploadRosterMenu).click()
        HardWait.hard_wait(10)

        # Assert if elements are displayed
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.RosterUploadHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.MarketTextBox, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.LineOfBusinessTextBox, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.NPITextBox, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.TaxIDTextBox, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.OrgNameTextBox, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.chooseFileBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadBtn, 10)

    # TC02	Upload a Roster, with all the field values and Verify that RO ID is displayed in the success pop-up on
    # EH User
    def test_UploadNewRosterEH(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadNewRosterEH', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadNewRoster.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        get_ROID = uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        print(get_ROID)

    # TC03	Upload a Roster, with Market as CA, Lob as Medicare, OrgName and Verify the RO ID is displayed in the
    # success pop-up
    def test_UploadNewRosterMandatoryFieldsEH(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadNewRosterMandatoryEH', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        print(Market, NPI, TaxID, LOB, OrgName)
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadNewRosterMandatoryFields.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        get_roid = uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        print(get_roid)

    # TC04	Upload a Roster, with all the field values and Verify that RO ID is displayed in the success pop-up on
    # Molina User
    def test_UploadNewRosterMolina(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadNewRosterMolina', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadNewRoster.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        get_ROID = uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        print(get_ROID)

    # TC05	Upload a Roster, with Market as CA, Lob as Medicare, OrgName and Verify the RO ID is displayed in the
    # success pop-up on Molina user
    def test_UploadNewRosterMandatoryFieldsMolina(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadNewRosterMandatoryMol', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        print(Market, NPI, TaxID, LOB, OrgName)
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadNewRosterMandatoryFields.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        get_roid = uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        print(get_roid)

    # TC06	Upload a roster with all invalid details and verify that RO ID is not displayed in the pop-up on EH User
    def test_UploadRosterWithInvalidDetailsEH(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadRosterInvalidEH', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadRosterWithInvalidDetails.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.RosterUploadHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.chooseFileBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadBtn, 10)

    # TC06	Upload a roster with all invalid details and verify that RO ID is not displayed in the pop-up on EH User
    def test_UploadRosterWithInvalidDetailsMolina(self):
        login = LoginPage(self.driver)
        login.open()
        # Read user creds data from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(10)
        # Read details from Excel to upload a Roster
        Roster_details_file_path = ("C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input "
                                    "Files/GetNewRosterDetails.xlsx")
        columns = ['market', 'lob', 'npi', 'taxID', 'orgName']

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_UploadRosterInvalidMolina', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UploadRosterFiles/TC_UploadRosterWithInvalidDetails.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.RosterUploadHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.chooseFileBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadBtn, 10)


