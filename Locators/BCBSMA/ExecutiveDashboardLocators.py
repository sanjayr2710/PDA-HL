from selenium.webdriver.common.by import By


class ExecutiveDashboardPageLocators:
    executiveDashboardHeading = (By.XPATH, "//div[@class='MuiStack-root css-knpqyr']//*[name()='svg']")
    executiveDashboardBtn = (By.XPATH, "//div[@title='Executive']//*[name()='svg']")
    EDHeading = (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5 css-1dg2jyp']")
