import re
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Base.page_base import PageBase
from Locators.RAMainPage_Locators import RAMainPage_Locators
from Locators.UploadPageLocators import uploadPageLocators
from helpers.UtilFuntions import WaitAndAssert, HardWait


class UploadNewRosterPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    def uploadNewRoster(self, Market=None, LOB=None, NPI=None, TaxID=None, OrgName=None, file_path=None):
        WaitAndAssert.waitAndAssert(self.driver, RAMainPage_Locators.uploadRosterMenu, 10)
        HardWait.hard_wait(5)
        if Market is not None:
            self.driver.find_element(*RAMainPage_Locators.uploadRosterMenu).click()
            self.driver.find_element(*uploadPageLocators.MarketTextBox).click()
            self.driver.find_element(*uploadPageLocators.MarketTextBox).send_keys(Market)
            HardWait.hard_wait(5)
        if LOB is not None:
            self.driver.find_element(*uploadPageLocators.LineOfBusinessTextBox).click()
            self.driver.find_element(*uploadPageLocators.LineOfBusinessTextBox).send_keys(LOB)
            HardWait.hard_wait(5)
        if NPI is not None:
            self.driver.find_element(*uploadPageLocators.NPITextBox).click()
            self.driver.find_element(*uploadPageLocators.NPITextBox).send_keys(NPI)
            HardWait.hard_wait(5)
        if TaxID is not None:
            self.driver.find_element(*uploadPageLocators.TaxIDTextBox).click()
            self.driver.find_element(*uploadPageLocators.TaxIDTextBox).send_keys(TaxID)
            HardWait.hard_wait(5)
        if OrgName is not None:
            self.driver.find_element(*uploadPageLocators.OrgNameTextBox).click()
            self.driver.find_element(*uploadPageLocators.OrgNameTextBox).send_keys(OrgName)
        if file_path is not None:
            WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.chooseFileBtn, 5)
            self.driver.find_element(*uploadPageLocators.chooseFileBtn).send_keys(file_path)
        HardWait.hard_wait(5)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadBtn, 10)
        self.driver.find_element(*uploadPageLocators.uploadBtn).click()
        HardWait.hard_wait(10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadSuccessDescription, 10)
        WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.uploadSuccessOkBtn, 10)
        HardWait.hard_wait(10)
        # if pop-up is present
        popup_element = self.driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 popup-title css-rq20lf']")
        if popup_element.is_displayed():
            popup_text = popup_element.text
            ro_id_match = re.search(r'RO-ID:(\w+)', popup_text)
            assert ro_id_match is not None, "RO ID not found on popup"
            ro_id = ro_id_match.group(1)
            print("RO-ID:", ro_id)
            HardWait.hard_wait(2)
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB).perform()
            HardWait.hard_wait(2)
            actions.send_keys(Keys.ENTER).perform()
            WaitAndAssert.waitAndAssert(self.driver, uploadPageLocators.RosterUploadHeading, 10)
            return ro_id

