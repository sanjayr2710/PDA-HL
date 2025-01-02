import re
import openpyxl
import requests
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os, datetime


class WaitAndAssert:
    @staticmethod
    def waitAndAssert(driver, locator, timeout=10):
        try:
            # Ensure locator is a tuple
            if not isinstance(locator, tuple) or len(locator) != 2:
                raise ValueError(f"Locator must be a tuple with 2 elements (By, value), got {locator}")

            # Debugging statement to print the locator
            print(f"Waiting for element with locator: {locator}")

            element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
            assert element is not None, "Element not found"
            print("Element found")
        except TimeoutException:
            print("Element not found")
            raise AssertionError("Element not found within the given timeout")
        except ValueError as ve:
            print(f"Invalid locator: {ve}")
            raise


class HardWait:
    @staticmethod
    def hard_wait(seconds):
        time.sleep(seconds)


class GetRosterDetailsXlsx:
    def __init__(self, columns, *args):
        for index, value in enumerate(args):
            setattr(self, columns[index], value)


class XlsReader:
    @staticmethod
    def get_data_from_xlsx(file_path, sheet_name, columns):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name]
        roster_details = []

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header row
            details = GetRosterDetailsXlsx(columns, *row[:len(columns)])
            roster_details.append(details)

        return roster_details


class helpersUtil:
    @staticmethod
    def replaceXpathAtRuntime(xpath_replace, text_to_replace):
        # Access the XPath string from the tuple
        xpath_string = xpath_replace[1]

        # Use the format method on the string
        formatted_xpath = xpath_string.format(text_to_replace)

        return 'xpath', formatted_xpath

    @staticmethod
    def readTextFromWebElement(driver, locator):
        try:
            by, value = locator
            if not isinstance(value, str):
                raise ValueError("Locator value must be a string.")

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by, value))
            )
            return element.text
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class RosterAPIUtility:

    @staticmethod
    def get_roster_id_from_api(url):
        try:
            response = requests.post(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

            # Parse the JSON response and extract the rosterId
            data = response.json()
            return data.get('data', {}).get('rosterId')

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def trigger_upload_button_and_get_response(driver, onClickButtonName, response_variable_name):
        HardWait.hard_wait(10)
        print("UtilFunction - trigger_upload_button_and_get_response")
        onClickButtonName.click()
        HardWait.hard_wait(10)

        response_exists = driver.execute_script(f"return typeof {response_variable_name} !== 'undefined';")
        if not response_exists:
            raise Exception(f"JavaScript variable '{response_variable_name}' is not defined.")

        # Execute JavaScript to get the response
        api_response = driver.execute_script(f"return {response_variable_name};")
        return api_response


class Capture_Screenshot:
    @staticmethod
    def capture_screenshot(driver, testcase_name,
                           base_directory='C:/Users/sanjay.r/PycharmProjects/Roster Automation/Results'):
        # Create the base directory if it doesn't exist
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)

        # Create a new directory with today's date
        today = datetime.datetime.now()
        folder_name = today.strftime('%Y-%m-%d')  # Use only the date for the folder name
        folder_path = os.path.join(base_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        # Define the screenshot file path with the testcase name
        screenshot_file = os.path.join(folder_path, f'{testcase_name}.png')

        # Capture and save the screenshot
        driver.get_screenshot_as_file(screenshot_file)

        print(f"Screenshot saved to {screenshot_file}")
