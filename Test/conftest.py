import json
import os
import allure
import pytest
import zipfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from allure_commons.types import AttachmentType
from Drivers.driver_factory import DriverFactory

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = ""

SMTP_SERVER = "smtp.office365.com"  # Replace it with your SMTP server
SMTP_PORT = 587
SENDER_EMAIL = "sanjay.r@hilabs.com"
SENDER_PASSWORD = "Mahadeva@27"
RECIPIENT_EMAILS = ["ashwini.py@hilabs.com", "ishwar.navale@hilabs.com"]

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
    # Attach screenshot at the end of the test for both passed and failed cases
    if report.when == "call" and driver:
        # Capture screenshot
        screenshot = driver.get_screenshot_as_png()
        # Attach to Allure
        allure.attach(
            screenshot,
            name=f"Screenshot ({report.outcome.upper()}) - {item.name}",
            attachment_type=AttachmentType.PNG
        )

def zip_allure_report(report_dir, output_zip):
    """
    Compress the Allure report folder into a ZIP file.
    """
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(report_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=report_dir)
                zipf.write(file_path, arcname)

def send_email_with_attachment(subject, body, attachment_path):
    """
    Send an email with an attachment.
    """
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECIPIENT_EMAILS)
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(attachment_path)}",
        )
        msg.attach(part)

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAILS, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Generate the Allure report and send it via email after all test cases are executed.
    """
    allure_results_dir = "allure-results"
    allure_report_dir = "allure-report"
    zip_file_path = "allure-report.zip"

    # Generate Allure report
    os.system(f"allure generate {allure_results_dir} --clean -o {allure_report_dir}")

    # Compress the Allure report
    zip_allure_report(allure_report_dir, zip_file_path)

    # Send the report via email
    send_email_with_attachment(
        subject="Allure Test Report",
        body="Attached is the Allure Test Report. Please review the test results.",
        attachment_path=zip_file_path
    )

    # Clean up the zip file
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
