
from selenium.webdriver.common.by import By


class LoginPageLocators:
    HilabsLOGO = (By.XPATH, "//img[@src='/HiLabs_Primary_RGB.svg']")
    user_id_textbox = (By.XPATH, "//input[@name='email']")
    password_textbox = (By.XPATH, "//input[@name='password']")
    loginBtn = (By.XPATH, "//button[@type='submit']")

