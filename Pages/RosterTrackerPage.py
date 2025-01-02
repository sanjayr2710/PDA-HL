from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from Base.page_base import PageBase
from helpers.UtilFuntions import WaitAndAssert, HardWait, helpersUtil
from Locators.RosterTracker_Locators import RosterTrackerLocatorsL1, RosterTrackerLocatorsL2, PizzaTrackerL3, \
    ApproveOrEditMappingL3
from Locators.RAMainPage_Locators import RAMainPage_Locators


class RosterTrackerPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enterValuesOnFilter(self, value, locator):
        try:
            WaitAndAssert.waitAndAssert(self.driver, locator, 10)
            HardWait.hard_wait(1)
            self.driver.find_element(*locator).click()
            HardWait.hard_wait(1)
            self.driver.find_element(*locator).send_keys(value)
            HardWait.hard_wait(1)
            # Click on the result displayed on Status input filter
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ARROW_DOWN).perform()
            HardWait.hard_wait(1)
            actions.send_keys(Keys.ENTER).perform()
            HardWait.hard_wait(1)
        finally:
            print("Values were entered")

    def enterMultipleValuesOnFilter(self, values, locators):
        try:
            for ro_id in values:
                WaitAndAssert.waitAndAssert(self.driver, locators, 10)
                self.driver.find_element(*locators).click()
                HardWait.hard_wait(4)
                self.driver.find_element(*locators).send_keys(ro_id)
                HardWait.hard_wait(4)
                # Click on the result displayed on ticket input filter
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()
                HardWait.hard_wait(2)
                actions.send_keys(Keys.ENTER).perform()
                HardWait.hard_wait(4)
        finally:
            print("Multiple Values were entered")

    def clickOnAnyWebElement(self, locator):
        WaitAndAssert.waitAndAssert(self.driver, locator, 10)
        HardWait.hard_wait(2)
        self.driver.find_element(*locator).click()
        HardWait.hard_wait(2)
    """
    Returns elements from the input list starting from a given index and then at intervals.

    :param input_list: List of elements.
    :param start_index: Starting index (0-based index).
    :param interval: Interval between indices.
    :return: List of elements at the specified intervals.
    """
    @staticmethod
    def returnDataOnIndex(self, List, start_index, interval):
        result = []
        index = start_index

        while index < len(List):
            result.append(List[index])
            index += interval

        return result

    @staticmethod
    def readDateAndCalculateTheDifference(Date):
        date_str1, date_str2 = Date.split(" ~ ")
        date_format = "%d-%b-%y"

        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        # calculate the difference
        date_diff = (date2 - date1).days + 1

        return date_diff

    @staticmethod
    def ValidateDatesWithinRange(date_list, date_range):
        date_format_list = "%m/%d/%Y, %H:%M:%S EST"
        date_format_range = "%d-%b-%y"
        # Parse the start and end dates from the date range string
        date_str1, date_str2 = date_range.split(" ~ ")
        date_start = datetime.strptime(date_str1, date_format_range)
        date_end = datetime.strptime(date_str2, date_format_range)

        # Check if all dates in the list are within the range
        for date_str in date_list:
            date = datetime.strptime(date_str, date_format_list)
            if not (date_start <= date <= date_end):
                return False

        return True

    def assertRostersPresenceOnTrackerPage(self, ROID):
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        self.driver.find_element(*RAMainPage_Locators.rosterTrackerMenu).click()
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        dynamic_Xpath = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.RosterDetailsRow, ROID)
        print(dynamic_Xpath)
        HardWait.hard_wait(10)
        while True:
            try:
                # Attempt to find the element using the dynamic XPath
                element = self.driver.find_element(By.XPATH, dynamic_Xpath)

                # Check if the element is visible
                if element.is_displayed():
                    print("Element Found")

                    # Wait for the element to be ready for interaction
                    WaitAndAssert.waitAndAssert(self.driver, dynamic_Xpath, 10)
                    HardWait.hard_wait(5)

                    # Click the element once it is visible
                    element.click()
                    break
                else:
                    print("Element is present but not visible.")

            # Handle cases where the element is not found
            except NoSuchElementException:
                print("Element Not Found, clicking on refresh")

                # Find and click the refresh button
                self.driver.find_element(*RosterTrackerLocatorsL1.RefreshBtn).click()

            # Add a short wait before the next attempt
            HardWait.hard_wait(5)

        HardWait.hard_wait(10)


        element.click()

    # Verify
    def navigateToRosterTrackerL2Page(self, ROID, FileStatus, Market):
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.rosterTrackerMenu, 10)
        self.driver.find_element(*RAMainPage_Locators.rosterTrackerMenu).click()
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        dynamic_xpath_roid = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.RosterDetailsRow, ROID)
        while True:
            if dynamic_xpath_roid is not True:
                self.driver.find_element(*RosterTrackerLocatorsL2.refreshBtnL2).click()
            else:
                WaitAndAssert.waitAndAssert(self.driver, dynamic_xpath_roid, 90)
                self.driver.find_element(dynamic_xpath_roid).click()
                break
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL2.RosterTrackerHeading, 10)

    def AssertMsgDisplayedOnLabelL2(self, ROID=None, Market=None, FileStatus=None, ReasonDescription=None):
        # Verify the ROID is same as that is displayed on L2 screen
        if ROID is not None:
            TicketNoROID = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL2.TicketNoLabel)
            try:
                assert TicketNoROID == ROID, f"Assertion failed: {TicketNoROID} is not same as {ROID}"
            except AssertionError as E:
                print(E)

        # Verify the MARKET is same as that is displayed in L2 screen
        if Market is not None:
            MarketDisplayedOnHeader = helpersUtil.readTextFromWebElement(self.driver,
                                                                         RosterTrackerLocatorsL2.MarketLabelHD)
            MarketDisplayedOnTable = helpersUtil.readTextFromWebElement(self.driver,
                                                                        RosterTrackerLocatorsL2.MarketLabelTD)
            try:
                assert MarketDisplayedOnHeader == Market, f"Assertion Failed: {MarketDisplayedOnHeader} is not same as {Market}"
                assert MarketDisplayedOnTable == Market, f"Assertion Failed: {MarketDisplayedOnTable} is not same as {Market}"
            except AssertionError as E:
                print(E)

        # Verify the FileStatus is same as that is displayed in L2 screen
        if FileStatus is not None:
            FileStatusDisplayedOnTable = helpersUtil.readTextFromWebElement(self.driver,
                                                                            RosterTrackerLocatorsL2.FileStatusLabel)
            try:
                assert FileStatusDisplayedOnTable == FileStatus, f"Assertion Failed: {FileStatusDisplayedOnTable} is not same as {FileStatus}"
            except AssertionError as E:
                print(E)

        # Verify the Reason Description is displayed with appropriate Message
        if ReasonDescription is not None:
            ReasonDescriptionDisplayedOnTable = helpersUtil.readTextFromWebElement(self.driver,
                                                                                   RosterTrackerLocatorsL2.ReasonDescriptionTD)
            try:
                assert ReasonDescriptionDisplayedOnTable == ReasonDescription, f"Assertion Failed: {ReasonDescriptionDisplayedOnTable} is not same as {ReasonDescription}"
            except AssertionError as E:
                print(E)

    def EditMappingForRoster(self, ROID):
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL2.RosterTrackerHeading, 10)
        # Verify the RO ID is displayed
        TicketNoROID = helpersUtil.readTextFromWebElement(self.driver, RosterTrackerLocatorsL2.TicketNoLabel)
        try:
            assert TicketNoROID == ROID, f"Assertion failed: {TicketNoROID} is not same as {ROID}"
        except AssertionError as E:
            print(E)
        # To Verify the File Status is AI Mapping Complete that enables Edit mapping button
        FileStatusRequired = "AI Mapping Complete"
        # Loops/Waits until the file status is AI Mapping Complete
        while True:
            # Click the refresh button
            self.driver.find_element(*RosterTrackerLocatorsL2.refreshBtnL2).click()
            # Read the text from the File Status Label
            FileStatusDataOnLabel = helpersUtil.readTextFromWebElement(self.driver,
                                                                       RosterTrackerLocatorsL2.FileStatusLabel)

            # Check the status and act accordingly
            if FileStatusDataOnLabel == "Roster received in MCheck":
                print("Status: Roster received in MCheck ")
                dynamic_Xpath_FileStatus = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL2.FileStatusLabel,
                                                                             "Roster received in MCheck")
                WaitAndAssert.waitAndAssert(self.driver, dynamic_Xpath_FileStatus, 10)

            elif FileStatusDataOnLabel == "AI Mapping to start":
                print("Status: AI Mapping to start ")
                dynamic_Xpath_FileStatus = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL2.FileStatusLabel,
                                                                             "AI Mapping In-Progress")
                WaitAndAssert.waitAndAssert(self.driver, dynamic_Xpath_FileStatus, 10)

            elif FileStatusDataOnLabel == FileStatusRequired:
                print("Status:  AI Mapping In-Progress")
                dynamic_Xpath_FileStatus = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL2.FileStatusLabel,
                                                                             "AI Mapping In-Progress")
                WaitAndAssert.waitAndAssert(self.driver, dynamic_Xpath_FileStatus, 10)

            elif FileStatusDataOnLabel == "AI Mapping Complete":
                print("Status: AI Mapping Complete")
                dynamic_Xpath_FileStatus = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL2.FileStatusLabel,
                                                                             "AI Mapping Complete")
                WaitAndAssert.waitAndAssert(self.driver, dynamic_Xpath_FileStatus, 10)
                WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL2.EditMappingBtn, 10)
                break  # Exit the loop when the final status is reached

            else:
                print(f"Unexpected status: {FileStatusDataOnLabel}")
        # Wait for Edit mapping btn to display
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL2.EditMappingBtn, 20)
        self.driver.find_element(self.driver, RosterTrackerLocatorsL2.EditMappingBtn).click()

    def ApproveMappings(self):
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.ApproveEditHeader, 10)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.SheetsBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.ColumnMappingBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.DownloadColumnMappingBtn, 10)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.CancelBtn, 10)
        HardWait.hard_wait(20)
        # click on column tab
        self.driver.find_element(*ApproveOrEditMappingL3.ColumnMappingBtn).click()
        # Verify that Approve and Save Button is displayed
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.SaveBtn, 20)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.ApproveBtn, 20)
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.CancelBtn, 20)
        self.driver.find_element(*ApproveOrEditMappingL3.ApproveBtn).click()
        # Waits for the success popup
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.ApprovedSucessMsg, 20)
        MessageDisplayedOnApproveMappings = helpersUtil.readTextFromWebElement(self.driver,
                                                                               ApproveOrEditMappingL3.ApprovedSucessMsg)
        print(MessageDisplayedOnApproveMappings, "Automation script is Approving the Mapping")
        HardWait.hard_wait(10)
        self.driver.find_element(*ApproveOrEditMappingL3.ApproveBtnOnApprove).click()
        # Waits for the success popup for approving mapping
        WaitAndAssert.waitAndAssert(self.driver, ApproveOrEditMappingL3.EditMappingApprovedSuccessMsg, 20)
        MessageDisplayedOnApproveSuccess = helpersUtil.readTextFromWebElement(self.driver,
                                                                              ApproveOrEditMappingL3.EditMappingApprovedSuccessMsg)
        print(MessageDisplayedOnApproveSuccess)
        HardWait.hard_wait(10)
        # Click on Ok
        self.driver.find_element(*ApproveOrEditMappingL3.OkBtnOnApprove).click()

    def VerifyPlanTemplateGenerationComplete(self, ROID):
        # wait for the element visibility
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.ActionMenuPizzaTracker, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.ExpandPizzaTracker, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.DownloadTrackerReportBtn, 10)
        # Verify the RO ID displayed
        dynamic_roid = helpersUtil.readTextFromWebElement(self.driver, PizzaTrackerL3.PLMNoLabelPizzaTracker)
        try:
            assert dynamic_roid == ROID, f"Assertion failed: {dynamic_roid} is not same as {ROID}"
        except AssertionError as E:
            print(E)
        HardWait.hard_wait(10)
        # Expand the pizza tracker and verify the Success Image till plan template generation complete
        self.driver.find_element(*PizzaTrackerL3.ExpandPizzaTracker).click()
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.collapsePizzaTracker, 10)
        # assert all the success image for "Roster Received, Auto Mapping Completed, Converted to Standard Format,
        # Converted to QNXT"
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.SuccessImgOnRosterReceived, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.SuccessImgOnMappingCompleted, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.SuccessImgOnISF, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.SuccessImgOnQNXT, 10)

    def DownloadTrackerReport(self, ROID):
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.ExpandPizzaTracker, 10)
        WaitAndAssert.waitAndAssert(self.driver, PizzaTrackerL3.DownloadTrackerReportBtn, 10)
        # Verify the RO ID displayed
        dynamic_roid = helpersUtil.readTextFromWebElement(self.driver, PizzaTrackerL3.PLMNoLabelPizzaTracker)
        try:
            assert dynamic_roid == ROID, f"Assertion failed: {dynamic_roid} is not same as {ROID}"
        except AssertionError as E:
            print(E)
        HardWait.hard_wait(10)
        # Click on Download Tracker Report
        self.driver.find_element(*PizzaTrackerL3.DownloadTrackerReportBtn).click()
        HardWait.hard_wait(10)

    # This method will enter details on the Ticket No Filter and Navigates to Roster Tracker L2 Screen
    def EnterDetailsOnTicketFilters(self, ROID):
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TicketNoFilter)
        self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoFilter).click()
        # Enter the RO ID In the Ticket no Filter
        HardWait.hard_wait(10)
        self.driver.find_element(*RosterTrackerLocatorsL1.TicketNoFilter).send_keys(ROID)
        HardWait.hard_wait(10)
        # Find the Element Presence of RO ID on the dropDown
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.TNDropDownFirstDetails, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.TNDropDownFirstDetails).click()
        # Entered ROID will be displayed, Replace ROID in TICKET No Table details and click on it
        dym_TicketNo = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.TicketNoWriteTableData, ROID)
        WaitAndAssert.waitAndAssert(self.driver, dym_TicketNo, 10)
        self.driver.find_element(dym_TicketNo).click()  # Roster Tracker L2 screen will be displayed

    # This method will enter details on the Provider Group Filter and Navigates to Roster Tracker L2 Screen
    def EnterDetailsOnProviderFilter(self, orgName, ROID, Market):
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.ProviderGroupFilter)
        self.driver.find_element(*RosterTrackerLocatorsL1.ProviderGroupFilter).click()
        # Enter the Org Name In the Provider group Filter
        HardWait.hard_wait(10)
        self.driver.find_element(*RosterTrackerLocatorsL1.ProviderGroupFilter).send_keys(orgName)
        HardWait.hard_wait(10)
        # Find the Element Presence of OrgName on the dropDown
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.PGDropDowFirstDetails, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.PGDropDowFirstDetails).click()
        # Entered ROID will be displayed, Replace ROID in TICKET No Table details and click on it
        dym_TicketNo = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.TicketNoWriteTableData, ROID)
        WaitAndAssert.waitAndAssert(self.driver, dym_TicketNo, 10)
        # Replace the Market to Xpath and Assert the Market displayed on the table details
        dym_Market = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.ReplaceTableDetailsOnXpath, Market)
        WaitAndAssert.waitAndAssert(self.driver, dym_Market, 10)
        self.driver.find_element(dym_TicketNo).click()  # Roster Tracker L2 screen will be displayed

    def EnterDetailsOnMarketFilter(self, Market, ROID):
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.RosterTrackerHeading, 10)
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.MarketFilter)
        self.driver.find_element(*RosterTrackerLocatorsL1.MarketFilter).click()
        # Enter the Market In the Market Filter
        HardWait.hard_wait(10)
        self.driver.find_element(*RosterTrackerLocatorsL1.ProviderGroupFilter).send_keys(Market)
        HardWait.hard_wait(10)
        # Find the Element Presence of OrgName on the dropDown
        WaitAndAssert.waitAndAssert(self.driver, RosterTrackerLocatorsL1.MarketDropDownFirstDetails, 10)
        self.driver.find_element(*RosterTrackerLocatorsL1.MarketDropDownFirstDetails).click()
        # Entered ROID will be displayed, Replace ROID in TICKET No Table details and click on it
        dym_TicketNo = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.TicketNoWriteTableData, ROID)
        WaitAndAssert.waitAndAssert(self.driver, dym_TicketNo, 10)
        # Replace the Market to Xpath and Assert the Market displayed on the table details
        dym_Market = helpersUtil.replaceXpathAtRuntime(RosterTrackerLocatorsL1.ReplaceTableDetailsOnXpath, Market)
        WaitAndAssert.waitAndAssert(self.driver, dym_Market, 10)
        self.driver.find_element(dym_TicketNo).click()   # Roster Tracker L2 screen will be displayed

