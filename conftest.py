import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_name = f"{item.name}_{timestamp}.png"

            screenshot_path = os.path.join("screenshots", screenshot_name)

            driver.save_screenshot(screenshot_path)
