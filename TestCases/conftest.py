import pytest
import allure
from allure_commons.types import AttachmentType
from Utilities.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    """
    this fixture is for initialize the driver basis of user params
    :param request: browser_name
    :return: driver for all classes
    """
    browser_name = request.config.getoption("browser_name")
    driver = DriverFactory.get_driver(browser_name)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    driver.implicitly_wait(3)
    yield
    try:
        if request.session.testsfailed != before_failed:
            allure.attach(driver.get_screenshot_as_png(), name="Test_failed", attachment_type=AttachmentType.PNG)
    except Exception as e:
        print(e)
    finally:
        driver.quit()
