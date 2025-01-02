from selenium.webdriver.common.by import By

class RAMainPage_Locators:
    hilabsLogo = (By.XPATH, "//img[@src='/HiLabs_logo.png']")
    mCheckProviderLogo = (By.XPATH, "//img[@src='/mcheck.png']")
    executiveSummaryMenu = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-rq20lf' and text()='Executive Summary']")
    executiveDashboardMenu = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-rq20lf' and text()='Executive Dashboard']")
    rosterTrackerMenu = (By.XPATH, "//p[normalize-space()='Roster Tracker - New']")
    rosterForManualReview = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-rq20lf' and text()='Roster For Manual Review']")
    uploadRosterMenu = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-rq20lf' and text()='Upload Roster']")
