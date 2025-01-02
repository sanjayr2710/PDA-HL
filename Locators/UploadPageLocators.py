from selenium.webdriver.common.by import By


class uploadPageLocators:
    RosterUploadHeading = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/h3')
    MarketTextBox = (By.XPATH, "//input[@name='market']")
    LineOfBusinessTextBox = (By.XPATH, "//input[@name='lineOfBusiness']")
    NPITextBox = (By.XPATH, "//input[@name='npi']")
    TaxIDTextBox = (By.XPATH, "//input[@name='taxId']")
    OrgNameTextBox = (By.XPATH, "//input[@name='orgName']")
    chooseFileBtn = (By.XPATH, '//*[@id="root"]/div/main/div[2]/div/form/div/input')
    uploadBtn = (By.XPATH,
                 "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-1d6mz21']")
    uploadSuccessDescription = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 popup-title css-rq20lf']")
    uploadSuccessOkBtn = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[3]/div/button")
    uploadSuccessCloseBtn = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/img")
