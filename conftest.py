import logging
import os

import allure
import pytest

from core.appium_service import AppiumService
from utils.config_reader import load_config, load_android_caps, load_ios_caps
from core.driver_factory import DriverFactory
from utils.runtime_config import get_runtime_config
from utils.wait_utils import WaitUtils

pytest.driver_instance = None

appium_service = AppiumService()


@pytest.fixture(scope="session", autouse=True)
def start_appium():
    if os.getenv("EXEC_MODE") == "local":
        appium_service.start()
        yield
        try:
            appium_service.stop()
        except Exception:
            pass


# @pytest.fixture(scope="function")
# def driver():
#     config = load_config()
#     android_caps = load_android_caps()
#     ios_caps = load_ios_caps()
#
#     driver = DriverFactory.create_driver(
#         config,
#         android_caps,
#         ios_caps,
#     )
#
#     pytest.driver_instance = driver
#     yield driver
#
#     driver.quit()

@pytest.fixture(scope="function")
def driver():

    config = load_config()

    app = os.getenv("APP", "app2")

    print(f"Launching app capability profile: {app}")

    android_caps = load_android_caps(app)
    ios_caps = load_ios_caps()

    driver = DriverFactory.create_driver(
        config,
        android_caps,
        ios_caps,
    )

    pytest.driver_instance = driver
    yield driver

    driver.quit()


@pytest.fixture
def wait_utils(driver):
    config = load_config()
    return WaitUtils(
        driver,
        config["timeouts"]["explicitWait"],
        config["timeouts"]["pollFrequency"]
    )
log = logging.getLogger(__name__)
def pytest_sessionstart():
    runtime = get_runtime_config()
    log.info("=== TEST SESSION STARTED ===")
    log.info(f"Environment : {runtime['environment']}")
    log.info(f"Platform    : {runtime['platform']}")
    log.info(f"Device      : {runtime['device']}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        driver = getattr(pytest, "driver_instance", None)

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{rep.when}.png"
            )

            try:
                driver.save_screenshot(file_path)

                allure.attach.file(
                    file_path,
                    name=f"Screenshot ({rep.when})",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                log.warning(f"Screenshot capture failed: {e}")

            allure.attach.file(
                file_path,
                name=f"Screenshot ({rep.when})",
                attachment_type=allure.attachment_type.PNG
            )


# @pytest.fixture(autouse=True)
# def reset_app_state(driver):
#     yield
#     try:
#         if driver.session_id:
#             driver.reset()
#     except Exception:
#         try:
#             driver.launch_app()
#         except Exception:
#             pass
