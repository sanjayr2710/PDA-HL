import json
import os
from Base.page_base import PageBase
from Locators.BCBSMA.Login_Locators import LoginPageLocators
from helpers.UtilFuntions import WaitAndAssert, HardWait


class LoginPage(PageBase):
    def __init__(self, driver, config_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))):
        super().__init__(driver)
        self.base_url = self.get_url_from_config(config_path)

    def get_url_from_config(self, config_path):
        try:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            client = config.get("client")

            if client == "Elixir":
                return config.get("ElixirURL", "Elixir URL not found")
            elif client == "BCBSMA":
                return config.get("BCBSMAURL", "BCBSMA URL not found")
            elif client == "Molina":
                return config.get("MolinaURL", "Molina URL not found")
            elif client == "CareSource":
                return config.get("CareSourceURL", "CareSource URl Not found")
            elif client == "Scan":
                return config.get("Scan URL", "Scan URL not found")
            elif client == "Horizon":
                return config.get("Horizon URL not found")
            else:
                raise ValueError("Invalid client specified in config.json")
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the config file: {e}")

    def open(self):
        super().open(self.base_url)

    def Login_to_RA(self, username=None, password=None):
        self.open()
        WaitAndAssert.waitAndAssert(self.driver, LoginPageLocators.HilabsLOGO, 10)
        self.driver.find_element(*LoginPageLocators.user_id_textbox).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password_textbox).send_keys(password)
        HardWait.hard_wait(5)
        self.driver.find_element(*LoginPageLocators.loginBtn).click()
