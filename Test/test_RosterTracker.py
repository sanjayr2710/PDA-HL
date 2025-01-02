import unittest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from Pages.LoginPage import LoginPage
from Pages.UploadNewRosterPage import UploadNewRosterPage
from Pages.RosterTrackerPage import RosterTrackerPage
from helpers.UtilFuntions import XlsReader, HardWait, WaitAndAssert, Capture_Screenshot, helpersUtil
from Locators.RAMainPage_Locators import RAMainPage_Locators
from Locators.RosterTracker_Locators import RosterTrackerLocatorsL1, RosterTrackerLocatorsL2, PizzaTrackerL3, ApproveOrEditMappingL3
from Locators.ExecutiveDashboardLocators import ExecutiveDashboardPageLocators
from helpers.webdriver_listener import WebDriverListener


@pytest.mark.usefixtures("setup")
class RosterTracker(unittest.TestCase):
    # TC01	Verify on login with valid user ID and password RA Tracker New displayed in side menu bar
    def test_AssertRosterTrackerNewMenu(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        # Expected result: Assert Roster Tracker Menu bar is displayed
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC01_AssertRosterTrackerNewMenu')  # Capture screenshot

    # TC02	Verify the Roster tracker page has 8 filters (TicketNo, Provider, Date, market, Lob, Tin, Status and
    # Source) is displayed
    def test_ValidateFiltersOnRosterTracker(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        # Expected result: Assert the Filter elements presence on Roster Tracker Page
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TicketNoFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ProviderGroupFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.MarketFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.LOBFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TINFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.StatusFilter, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.SourceSystemFilter, 10)
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC02_ValidateFiltersOnRosterTracker')

    # TC03	Verify the Roster Tracker page has Download and Print button is displayed
    def test_ValidateDownload_Refresh_Reset_Btn(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        # Expected result: Assert the Filter elements presence on Roster Tracker Page
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.L1DownloadBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RefreshBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ResetBtn, 10)
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_03_ValidateDownload_Refresh_Reset_Btn')

    # TC04 Verify upon clicking the download button in Roster Tracker page the pop-up is displayed
    def test_ValidateDownloadSuccess(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, ExecutiveDashboardPageLocators.executiveDashboardHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        # Expected result: Assert the Filter elements presence on Roster Tracker Page
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.L1DownloadBtn, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.L1DownloadBtn)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.L1DownloadSuccessPopUp, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.L1OkBtnOnDownloadSuccessPopup, 10)
        # Assert the success message displayed on the popup
        popup_element = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div[3]/p")
        popup_text = popup_element.text
        print(popup_text)
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_04_ValidateDownloadSuccess')
        self.driver.find_element(*RosterTrackerLocatorsL1.L1OkBtnOnDownloadSuccessPopup).click()

    # TC05	Verify the Roster tracker page has a drop-down to set the page size (5,10, 15, 20)
    def test_ValidatePaginationPagesDropDown(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify the Page sizes are displayed in the Pagination drop-down
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeTen, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeTwenty, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeThirty, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeFifty, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeFifty, 10)
        Capture_Screenshot.capture_screenshot(self.driver, "RT-TC_05_ValidatePaginationPagesDropDown")

    # TC06	Verify When a user selects 10 as a page size only 10 Record details should be displayed
    def test_ValidatePaginationTenRecords(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify when a user selects 10 as page size 10 Record details should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeTen, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeTwenty).click()
        HardWait.hard_wait(4)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeTen).click()
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        if record_elements:
            for i, record in enumerate(record_elements):
                print(f"Record {i + 1}: {record.text}")

        # Assert that the number of records displayed is 10
        assert len(record_elements) == 10, f"Expected 10 records, but found {len(record_elements)}"
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_06_ValidatePaginationTenRecords')

    # TC07	Verify When a user selects 20 as a page size only 20 Record details should be displayed
    def test_ValidatePaginationTwentyRecords(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify when a user selects 20 as page size 20 Record details should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeTwenty, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeTwenty).click()
        HardWait.hard_wait(4)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        if record_elements:
            for i, record in enumerate(record_elements):
                print(f"Record {i + 1}: {record.text}")

        # Assert that the number of records displayed is 20
        assert len(record_elements) == 20, f"Expected 20 records, but found {len(record_elements)}"
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_07_ValidatePaginationTwentyRecords')

    # TC08	Verify When a user selects 30 as a page size only 30 Record details should be displayed
    def test_ValidatePaginationThirtyRecords(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify when a user selects 30 as page size 30 Record details should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeThirty, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeThirty).click()
        HardWait.hard_wait(4)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        if record_elements:
            for i, record in enumerate(record_elements):
                print(f"Record {i + 1}: {record.text}")

        # Assert that the number of records displayed is 30
        assert len(record_elements) == 30, f"Expected 30 records, but found {len(record_elements)}"
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_08_ValidatePaginationThirtyRecords')

    # TC09	Verify When a user selects 40 as a page size only 40 Record details should be displayed
    def test_ValidatePaginationFortyRecords(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify when a user selects 40 as page size 40 Record details should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeForty, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeForty).click()
        HardWait.hard_wait(4)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        if record_elements:
            for i, record in enumerate(record_elements):
                print(f"Record {i + 1}: {record.text}")

        # Assert that the number of records displayed is 40
        assert len(record_elements) == 40, f"Expected 40 records, but found {len(record_elements)}"
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_09_ValidatePaginationFortyRecords')

    # TC10	Verify When a user selects 50 as a page size only 50 Record details should be displayed
    def test_ValidatePaginationFiftyRecords(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationDropDown, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.PaginationDropDown).click()
        HardWait.hard_wait(2)
        # Expected Result: Verify when a user selects 50 as page size 50 Record details should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PageSizeFifty, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PageSizeFifty).click()
        HardWait.hard_wait(4)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        if record_elements:
            for i, record in enumerate(record_elements):
                print(f"Record {i + 1}: {record.text}")

        # Assert that the number of records displayed is 50
        assert len(record_elements) == 50, f"Expected 50 records, but found {len(record_elements)}"
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_10_ValidatePaginationFiftyRecords')

    # TC11	Verify the Roster tracker page is displayed with pagination for the page size selected from the drop-down
    def test_ValidatePaginationNavigators(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Verify that Pagination option available to Navigate to the Next and Previous page
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationNavigateToNextPage, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationNavigateToPreviousPage, 10)
        Capture_Screenshot.capture_screenshot(self.driver, 'RT-TC_11_ValidatePaginationNavigators')

    # TC12	Verify that user can Navigate to the Previous page and Next Page to search records
    def test_NavigateToPagesWithPaginationNavigators(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationNavigateToNextPage, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PaginationNavigateToPreviousPage, 10)
        HardWait.hard_wait(2)
        # Expected Result: Assert the Presence of Roster on Page 1 and Page 2 and Validate that same RO ID is not displayed
        # Collect records on Page 1
        record_elements_page_one = self.driver.find_elements(By.XPATH,
                                                             "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_page_one = [element.text for element in record_elements_page_one]
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_12A_NavigateToPagesWithPaginationNavigators')
        # Navigate to Page 2
        pagination_next = self.driver.find_element(*RosterTrackerLocatorsL1.PaginationNavigateToNextPage)
        self.driver.execute_script("arguments[0].click();", pagination_next)
        HardWait.hard_wait(2)
        # Collect records on Page 2
        record_elements_page_two = self.driver.find_elements(By.XPATH,
                                                             "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_page_two = [element.text for element in record_elements_page_two]
        # Assert that the records on Page 1 are not present on Page 2
        for record in record_texts_page_one:
            assert record not in record_texts_page_two, f"Record {record} found on both pages"

        print("Records on Page 1:", record_texts_page_one)
        print("Records on Page 2:", record_texts_page_two)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_12B_NavigateToPagesWithPaginationNavigators')

    # TC13	"Verify the Roster tracker page has records displayed with table headers(
    # TICKET NO,
    # ROSTER STATUS
    # MARKET
    # PERCENT COMPLETE
    # RECORDS IN ROSTER
    # RECORDS IN-SCOPE
    # RECORDS FULLY PROCESSED
    # RECORDS PARTIALLY PROCESSED
    # RECORDS THAT FAILED)"
    def test_ValidateTableHeadersL1(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate and assert the presence of table headers displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableHeadersOnTracker, 10)
        tableHeaders = ['TICKET NO', 'ROSTER STATUS', 'MARKET', 'PERCENT COMPLETE', 'RECORDS IN ROSTER',
                        'RECORDS IN-SCOPE', 'RECORDS FULLY PROCESSED', 'RECORDS PARTIALLY PROCESSED',
                        'RECORDS THAT FAILED', 'LATEST FILE RECEIVED TIME', 'RECORDS OUT OF SCOPE', 'RACT STATUS',
                        'ACTION']
        tableHeaders_element = self.driver.find_elements(*RosterTrackerLocatorsL1.TableHeadersOnTracker)
        tableHeadersOnTrackerPage = [element.text for element in tableHeaders_element]
        assert tableHeadersOnTrackerPage == tableHeaders, f"Expected headers: {tableHeaders}, but found: {tableHeadersOnTrackerPage}"
        print("Table Headers on Tracker Page:", tableHeadersOnTrackerPage)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_13_ValidateTableHeadersL1')

    # TC14	Verify in Roster Tracker page when a user wants to search for the Ticket No, Validate the searched record is displayed
    def test_ValidateTicketNoFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on Ticket No Filter and Validate that searched record is displayed
        ROID = ['ROEH1106']
        RosterTrackerPage.enterValuesOnFilter(self, ROID, RosterTrackerLocatorsL1.TicketNoFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_page_one = [element.text for element in record_elements]
        assert str(ROID) == str(record_texts_page_one), f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_elements}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA_TC_14_ValidateTicketNoFilterWithSingleValue')

    # TC15	Verify in Roster Tracker page Ticket No filter can accept Multiple values
    def test_ValidateTicketNoFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on Ticket No Filter and Validate all the searched records are displayed
        ROID = ['ROEH1106', 'ROEH1105', 'ROEH1083']
        HardWait.hard_wait(2)
        RosterTrackerPage.enterMultipleValuesOnFilter(self, ROID, RosterTrackerLocatorsL1.TicketNoFilter)
        HardWait.hard_wait(2)

        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_page_one = [element.text for element in record_elements]
        assert str(ROID) == str(record_texts_page_one), f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_elements}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_15_ValidateTicketNoFilterWithMultipleValues')

    # TC16	Verify in Roster Tracker page when user wants to search for the Provider Group, Validate the searched
    # record is displayed
    def test_ValidateProviderFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on Provider Filter and Validate that searched record is displayed
        ProviderGroup = 'Prime Health Care'
        ROID = ['ROMol1010']
        RosterTrackerPage.enterValuesOnFilter(self, ProviderGroup, RosterTrackerLocatorsL1.ProviderGroupFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert str(ROID) == str(record_texts), f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_16_ValidateProviderFilterWithSingleValue')

    # TC17	Verify in Roster Tracker page Provider filter can accept multiple values
    def test_ValidateProviderFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on Ticket No Filter and Validate all the searched records are displayed
        ProviderDetails = ['Prime Health Care', 'Vasan Health Care']
        ROID = ['ROMol1011', 'ROMol1010']
        RosterTrackerPage.enterMultipleValuesOnFilter(self, ProviderDetails, RosterTrackerLocatorsL1.ProviderGroupFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_17_ValidateProviderFilterWithMultipleValue')

    # TC18	Verify in Roster Tracker page when a user wants to search for the Market, Validate the searched record is
    # displayed
    def test_ValidateMarketFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on Market Filter and Validate that searched record is displayed
        marketDetails = 'GA'
        ROID = ['ROMol1010']
        RosterTrackerPage.enterValuesOnFilter(self, marketDetails, RosterTrackerLocatorsL1.MarketFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_18_ValidateMarketFilterWithSingleValue')

    # TC19	Verify in Roster Tracker page Market filter can accept Multiple values
    def test_ValidateMarketFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on Market Filter and Validate all the searched records are displayed
        MarketDetails = ['GA', 'CA']
        ROID = ['ROMol1011', 'ROMol1010']
        RosterTrackerPage.enterMultipleValuesOnFilter(self, MarketDetails, RosterTrackerLocatorsL1.MarketFilter)
        HardWait.hard_wait(2)

        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_19_ValidateMarketFilterWithMultipleValues')

    # TC20	Verify in Roster Tracker page when a user wants to search for the LOB, Validate the searched record is
    # displayed
    def test_ValidateLOBFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on Lob Filter and Validate that searched record is displayed
        lobDetails = 'Commercial'
        ROID = ['ROMol1010', 'ROMol1009']
        RosterTrackerPage.enterValuesOnFilter(self, lobDetails, RosterTrackerLocatorsL1.LOBFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_20_ValidateLOBFilterWithSingleValue')

    # TC21	Verify in Roster Tracker page LOB filter can accept Multiple values
    def test_ValidateLOBFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on LOB Filter and Validate all the searched records are displayed
        LobDetails = ['Commercial', 'Medicare']
        ROID = ['ROMol1011', 'ROMol1010', 'ROMol1009']
        RosterTrackerPage.enterMultipleValuesOnFilter(self, LobDetails, RosterTrackerLocatorsL1.LOBFilter)
        HardWait.hard_wait(2)

        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_21_ValidateLOBFilterWithMultipleValues')

    # TC22	Verify in Roster Tracker page when user wants to search for the TIN, Validate the searched record is displayed
    def test_ValidateTINFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on TIN Filter and Validate that searched record is displayed
        tinDetails = '81828384'
        ROID = ['ROMol1010']
        RosterTrackerPage.enterValuesOnFilter(self, tinDetails, RosterTrackerLocatorsL1.TINFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_22_ValidateTINFilterWithSingleValue')

    # TC23	Verify in Roster Tracker page TIN filter can accept Multiple values
    def test_ValidateTINFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on TIN Filter and Validate all the searched records are displayed
        TinDetails = ['81828384', '28272625']
        ROID = ['ROMol1011', 'ROMol1010']
        RosterTrackerPage.enterMultipleValuesOnFilter(self, TinDetails, RosterTrackerLocatorsL1.TINFilter)
        HardWait.hard_wait(2)

        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_23_ValidateTINFilterWithMultipleValues')

    # DEFECT - MCPRA-863
    # TC24	Verify in Roster Tracker page when a user wants to search for the Status, Validate the searched record is displayed
    def test_ValidateStatusFilterWithSingleValue(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Enter a Value on Status Filter and Validate that searched record is displayed
        StatusDetails = 'In Progress'
        ROID = ['ROMol1010']
        RosterTrackerPage.enterValuesOnFilter(self, StatusDetails, RosterTrackerLocatorsL1.StatusFilter)
        HardWait.hard_wait(2)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_24_ValidateStatusFilterWithSingleValue')

    # TC25	Verify in Roster Tracker page Status filter can accept Multiple values
    def test_ValidateStatusFilterWithMultipleValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RemoveDateFromFilter, 10)
        HardWait.hard_wait(2)
        # Expected Result: Enter Multiple Values on Status Filter and Validate all the searched records are displayed
        StatusDetails = ['In Progress', 'Incompatible']
        ROID = ['ROMol1011', 'ROMol1010']
        RosterTrackerPage.enterMultipleValuesOnFilter(self, StatusDetails, RosterTrackerLocatorsL1.StatusFilter)
        HardWait.hard_wait(2)

        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert ROID == record_texts, f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_25_ValidateStatusFilterWithMultipleValues')

    # TC26	Verify in Roster Tracker page when a user enters all the Filter values - The Resulted records should be displayed in the Result table
    def test_ValidateAllFiltersWithValues(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        ROID = ['ROMol1010']
        providerGroup = 'Prime Health Care'
        market = 'GA'
        lob = 'Commercial'
        tin = '81828384'
        status = 'In Progress'
        # Enter Ticket No
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, ROID, RosterTrackerLocatorsL1.TicketNoFilter)
        # Enter Provider Group
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, providerGroup, RosterTrackerLocatorsL1.ProviderGroupFilter)
        # Enter Market
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, market, RosterTrackerLocatorsL1.MarketFilter)
        # Enter LOB
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, lob, RosterTrackerLocatorsL1.LOBFilter)
        # Enter TIN
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, tin, RosterTrackerLocatorsL1.TINFilter)
        # Enter status
        HardWait.hard_wait(2)
        RosterTrackerPage.enterValuesOnFilter(self, status, RosterTrackerLocatorsL1.StatusFilter)
        # Assert the presence of Roster displayed
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts = [element.text for element in record_elements]
        assert str(ROID) == str(record_texts), f'Searched Records and displayed records are not the same'
        print(f"Records displayed on the Tracker Screen: {record_texts}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_26_ValidateAllFiltersWithValues')

    # TC27	Verify in Roster Tracker page that user is able to sort the Ticket No Table Header
    def test_SortTicketNoTableHeaders(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Sorting Ticket No Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.SortTicketNoTableHeader, 10)
        HardWait.hard_wait(2)
        # Read all the Ticket No displayed on the Tracker Before Sorting
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_before_sort = [element.text for element in record_elements]
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.SortTicketNoTableHeader).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//p[@class='MuiTypography-root MuiTypography-body1 css-xvjzky']")
        record_texts_after_sort = [element.text for element in record_elements]
        assert record_texts_before_sort != record_texts_after_sort, f'Unable to Sort Ticket No Table header'
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_27_SortTicketNoTableHeaders')

    # TC28	Verify in Roster Tracker page that a user is able to sort the Roster Status Table Header
    def test_SortRosterStatusTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'MOLINAUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Sorting Roster Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[1].click()
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-v7v99c']")
        record_texts_ascending_sort = [element.text for element in record_elements]
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-v7v99c']")
        record_texts_descending_sort = [element.text for element in record_elements]
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_28_SortRosterStatusTableHeader')

    # TC29	Verify in Roster Tracker page that user is able to sort the Market Table Header
    def test_SortMarketTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Sorting Roster Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[2].click()    # click on the 3rd presence of the element
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH, "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 2, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH, "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 2, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_29_SortMarketTableHeader')

    # TC30	Verify in Roster Tracker page that user is able to sort the Percent Complete Table Header
    def test_SortPercentCompleteTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[3].click()  # click on the 4th presence of the element
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH, "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 3, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 3, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_30_SortPercentCompleteTableHeader')

    # TC31	Verify in Roster Tracker page that user is able to sort the Records in Roster Table Header
    def test_SortRecordsInRosterTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[4].click()  # click on the 5th presence of the element
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 4, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 4, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_31_SortRecordsInRosterTableHeader')

    # TC32	Verify in Roster Tracker page that user is able to sort the Records In-Scope Table Header
    def test_SortRecordsInScopeTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[5].click()  # click on the 6th presence of the element
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 5, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 5, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_32_SortRecordsInScopeTableHeader')

    # TC33	Verify in Roster Tracker page that user is able to sort the Records Fully Processed Table Header
    def test_SortRecordsFullyProcessedTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[6].click()  # click on the 7th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 6, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 6, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_33_SortRecordsFullyProcessedTableHeader')

    # TC34	Verify in Roster Tracker page that user is able to sort the Records Partially Processed Table Header
    def test_SortRecordsPartiallyProcessedTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[7].click()  # click on the 8th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 7, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 7, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_34_SortRecordsPartiallyProcessedTableHeader')

    # TC35	Verify in Roster Tracker page that user is able to sort the Records that failed Table Header
    def test_SortRecordsThatFailedTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[8].click()  # click on the 8th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 8, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 8, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_35_SortRecordsThatFailedTableHeader')

    # TC36	Verify in Roster Tracker page that user is able to sort the Latest File Received Time Table Header
    def test_SortLatestFileReceivedTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[9].click()  # click on the 8th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_36_SortLatestFileReceivedTableHeader')

    # TC37	Verify in Roster Tracker page that user is able to sort the Records out of scope Table Header
    def test_SortRecordsOutOfScopeTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[10].click()  # click on the 8th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 10, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 10, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_37_SortRecordsOutOfScopeTableHeader')

    # TC38	Verify in Roster Tracker page that user is able to sort the RACT Status Table Header
    def test_SortRACTStatusTableHeader(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that Percent Complete Status Table header is possible
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TableSortOff, 10)
        HardWait.hard_wait(2)
        roster_status = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1bicmub']")
        roster_status[11].click()  # click on the 8th presence of the element (index from 0)
        # Read all the Roster Status displayed on the Tracker in Ascending order
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_ascending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 11, 13)
        # click on Ticket No Table Sort
        HardWait.hard_wait(2)
        self.driver.find_element(*RosterTrackerLocatorsL1.TableSortAscendingDescending).click()
        # Read all the Ticket No displayed on the Tracker After Sorting
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterStatusTDReadData, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_descending_sort = RosterTrackerPage.returnDataOnIndex(self, record_texts, 11, 13)
        assert record_texts_ascending_sort != record_texts_descending_sort, f'Unable to Sort Ticket No Table header'
        print(record_texts_ascending_sort)
        print(record_texts_descending_sort)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_38_SortRACTStatusTableHeader')

    # TC39	Verify in Roster Tracker page that when user clicks on Date Filter, Validate the Date Pop is displayed with 2 Months Calender
    def test_ValidateDatePickerPopUp(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate when a user clicks on Date filter, The Date filter pop-up should be displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp, 10)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_39_ValidateDatePickerPopUp')

    # TC40 Verify in Roster Tracker page that when a user clicks on date filter, Validate the presence of Last 7 Days, last 15 Days, Last 20 Days, Last 30 Days and Ok button is displayed
    def test_ValidateElementsPresenceOnDatePicker(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that when a user clicks on Date filter, all the elements in the date picker are displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.Last7DaysButton, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.Last15DaysButton, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.Last20DaysButton, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.Last30DaysButton, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.OkButtonOnDatePickerPopUp, 10)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_40_ValidateElementsPresenceOnDatePicker')

    # TC 41 Verify in Roster Tracker page that when user Click on Date Filter and select Last 7 days, Validate last 7 days is selected in the pop-up
    def test_ValidateDateOnLast7DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that when a user clicks on last 7 days btn, assert the Date displayed (7 days == 7 days)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last7DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        diff_date = RosterTrackerPage.readDateAndCalculateTheDifference(Date_displayed)
        assert diff_date == 7
        print(f"Difference between the dates are: {diff_date}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_41_ValidateDateOnLast7DaysButton')

    # TC42	Verify in Roster Tracker page that when user Click on Date Filter and select Last 15 days, Validate last 15 days is selected in the pop-up
    def test_ValidateDateOnLast15DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that when a user clicks on last 15 days btn, assert the Date displayed (15 days == 15 days)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last15DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        diff_date = RosterTrackerPage.readDateAndCalculateTheDifference(Date_displayed)
        assert diff_date == 15
        print(f"Difference between the dates are: {diff_date}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_42_ValidateDateOnLast15DaysButton')

    # TC43	Verify in Roster Tracker page that when user Click on Date Filter and select Last 20 days, Validate last 20 days is selected in the pop-up
    def test_ValidateDateOnLast20DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that when a user clicks on last 20 days btn, assert the Date displayed (20 days == 20 days)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last20DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        diff_date = RosterTrackerPage.readDateAndCalculateTheDifference(Date_displayed)
        assert diff_date == 20
        print(f"Difference between the dates are: {diff_date}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_43_ValidateDataOnLast20DaysButton')

    # TC44	Verify in Roster Tracker page that when user Click on Date Filter and select Last 30 days, Validate last 30 days is selected in the pop-up
    def test_ValidateDateOnLast30DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Validate that when a user clicks on last 30 days btn, assert the Date displayed (30 days == 30 days)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last30DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        diff_date = RosterTrackerPage.readDateAndCalculateTheDifference(Date_displayed)
        assert diff_date == 30
        print(f"Difference between the dates are: {diff_date}")
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_44_ValidateDataOnLast30DaysButton')

    # TC45	Verify in Roster Tracker page that when a user clicks on Last 7 days button, validate only last 7 days Records are displayed in the Tracker
    def test_ValidateRecordsOnLast7DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Verify that whether last 15-day Records are displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last7DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.OkButtonOnDatePickerPopUp)
        # Read all the Roster Status displayed on the Tracker
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_Last7_days = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        is_valid = RosterTrackerPage.ValidateDatesWithinRange(record_texts_Last7_days, Date_displayed)
        assert is_valid == True, f"Dates were not not in the given range"
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_45_ValidateRecordsOnLast7DaysButton')

    # TC46	Verify in Roster Tracker page that when a user clicks on Last 15 days button, validate only last 15 days Records are displayed in the Tracker
    def test_ValidateRecordsOnLast15DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Verify that whether last 20-day Records are displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last15DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.OkButtonOnDatePickerPopUp)
        # Read all the Roster Status displayed on the Tracker
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_Last15_days = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        is_valid = RosterTrackerPage.ValidateDatesWithinRange(record_texts_Last15_days, Date_displayed)
        assert is_valid == True, f"Dates were not not in the given range"
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_46_ValidateRecordsOnLast15DaysButton')

    # TC47	Verify in Roster Tracker page that when a user clicks on Last 20 days button, validate only last 20 days Records are displayed in the Tracker
    def test_ValidateRecordsOnLast20DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Verify that whether last 7-day Records are displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last20DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.OkButtonOnDatePickerPopUp)
        # Read all the Roster Status displayed on the Tracker
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_Last20_days = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        is_valid = RosterTrackerPage.ValidateDatesWithinRange(record_texts_Last20_days, Date_displayed)
        assert is_valid == True, f"Dates were not not in the given range"
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_47_ValidateRecordsOnLast15DaysButton')

    # TC48	Verify in Roster Tracker page that when a user clicks on Last30 days button, validate only last 30-day Records are displayed in the Tracker
    def test_ValidateRecordsOnLast30DaysButton(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
        file_path1 = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/UserCreds.xlsx"
        columns = ['username', 'password']
        data = XlsReader.get_data_from_xlsx(file_path1, 'EHUSERCREDS', columns)

        if data:
            username = data[0].username
            passWord = data[0].password
        # login to RA
        login.Login_to_RA(username, passWord)
        HardWait.hard_wait(3)
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RAMainPage_Locators.rosterTrackerMenu)
        HardWait.hard_wait(2)
        # Expected Result: Verify that whether last 30-day Records are displayed
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DateFilter, 10)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.DatePickerPopUp, 10)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.Last30DaysButton)
        HardWait.hard_wait(2)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.DateFilter)
        Date_displayed = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL1.DateRangeOnPopUp)
        print(Date_displayed)
        RosterTrackerPage.clickOnAnyWebElement(self, RosterTrackerLocatorsL1.OkButtonOnDatePickerPopUp)
        # Read all the Roster Status displayed on the Tracker
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ReadTableDetailsOnXpath, 10)
        record_elements = self.driver.find_elements(By.XPATH,
                                                    "//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeSmall css-19115l7']")
        record_texts = [element.text for element in record_elements]
        record_texts_Last7_days = RosterTrackerPage.returnDataOnIndex(self, record_texts, 9, 13)
        is_valid = RosterTrackerPage.ValidateDatesWithinRange(record_texts_Last7_days, Date_displayed)
        assert is_valid == True, f"Dates were not not in the given range"
        Capture_Screenshot.capture_screenshot(self.driver, 'RA-TC_48_ValidateRecordsOnLast30DaysButton')

    # Login for EH, upload a roster, Verify the roster presence on tracker page
    def test_UploadRosterAndVerifyInTracker(self):
        login = LoginPage(self.driver)
        login.open()
        # Read EH user creds from Excel
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

        data = XlsReader.get_data_from_xlsx(Roster_details_file_path, 'TC_Tracker_NewRoster', columns)
        if data:
            Market = data[0].market
            LOB = data[0].lob
            NPI = data[0].npi
            TaxID = data[0].taxID
            OrgName = data[0].orgName
        # Roster file path
        Roster_file_path = "C:/Users/sanjay.r/PycharmProjects/Roster Automation/Input Files/Roster-GA-CA.xlsx"
        uploadRoster = UploadNewRosterPage(self.driver)
        get_ROID = uploadRoster.uploadNewRoster(Market, LOB, NPI, TaxID, OrgName, Roster_file_path)
        print(get_ROID)
        HardWait.hard_wait(10)
        NavigateToTracker = RosterTrackerPage(self.driver)
        NavigateToTracker.assertRostersPresenceOnTrackerPage(get_ROID)
