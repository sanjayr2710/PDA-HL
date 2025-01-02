import logging
import datetime
import os

from selenium.webdriver.support.events import AbstractEventListener


class WebDriverListener(AbstractEventListener):
    def __init__(self, testcase_name, base_directory='C:/Users/sanjay.r/PycharmProjects/Roster Automation/Results'):
        self.base_directory = base_directory
        self.setup_logger(testcase_name)

    def setup_logger(self, testcase_name):
        # Create a new directory with today's date
        today = datetime.datetime.now()
        folder_name = today.strftime('%Y-%m-%d')
        folder_path = os.path.join(self.base_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Define the log file path with the testcase name
        log_filename = f"{testcase_name}.log"
        log_file = os.path.join(folder_path, log_filename)

        # Set up the logger
        logging.basicConfig(
            filename=log_file,
            format="%(asctime)s: %(levelname)s: %(message)s",
            level=logging.INFO
        )
        self.logger = logging.getLogger(testcase_name)

    def before_navigate_to(self, url, driver):
        if self.logger:
            self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        if self.logger:
            self.logger.info(f"{url} opened")

    def before_find(self, by, value, driver):
        if self.logger:
            self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        if self.logger:
            self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if self.logger:
            text = element.get_attribute("text")
            if text:
                self.logger.info(f"Clicking on {text}")
            else:
                self.logger.info(f"Clicking on {element.get_attribute('class')}")

    def after_click(self, element, driver):
        if self.logger:
            text = element.get_attribute("text")
            if text:
                self.logger.info(f"{text} clicked")
            else:
                self.logger.info(f"{element.get_attribute('class')} clicked")

    def before_change_value_of(self, element, driver):
        if self.logger:
            self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        if self.logger:
            self.logger.info("Driver quitting")

    def after_quit(self, driver):
        if self.logger:
            self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        if self.logger:
            self.logger.info(exception)
