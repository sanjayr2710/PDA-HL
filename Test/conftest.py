import json
import os
import allure
import pytest
from allure_commons.types import AttachmentType
from Drivers.driver_factory import DriverFactory

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = ""


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        return json.load(config_file)


@pytest.fixture(scope='session')
def driver(config):
    """
    Session-scoped WebDriver fixture to ensure a single browser instance for all test cases in a session.
    """
    driver = DriverFactory.get_driver(config, "session")
    driver.implicitly_wait(config.get("timeout", 20))
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function', autouse=True)
def test_setup(request, driver):
    """
    Function-scoped fixture to attach the WebDriver instance to each test case and handle failures.
    """
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed > before_failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Test failed", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and attach screenshots for both passed and failed test cases.
    """
    outcome = yield
    report = outcome.get_result()
    driver = getattr(item.instance, 'driver', None)

    # Attach screenshot for both passed and failed tests
    if report.when == "call" and driver:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Screenshot ({report.outcome.upper()}) - {item.name}",
            attachment_type=AttachmentType.PNG
        )