
from selenium.webdriver.common.by import By


class LoginPageLocators:
    HilabsLOGO = (By.XPATH, "//img[@src='/bcbsma/logo.svg']")
    user_id_textbox = (By.XPATH, "//input[@name='username']")
    password_textbox = (By.XPATH, "//input[@name='password']")
    loginBtn = (By.XPATH, "//button[@type='submit']")
