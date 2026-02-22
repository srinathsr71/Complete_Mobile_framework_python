import logging
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from utils.runtime_config import get_runtime_config


log = logging.getLogger(__name__)


class DriverFactory:

    @staticmethod
    def create_driver(config, android_caps, ios_caps=None):
        runtime = get_runtime_config()

        platform = runtime["platform"].lower()
        device = runtime["device"]
        environment = runtime["environment"]
        remote_server_url = runtime["remote_server_url"]

        log.info("Initializing driver")
        log.info(f"Platform    : {platform}")
        log.info(f"Device      : {device}")
        log.info(f"Environment : {environment}")

        if platform == "android":
            log.info("Creating ANDROID driver")
            return DriverFactory._create_android_driver(
                config, android_caps, environment, device, remote_server_url
            )

        if platform == "ios":
            log.info("Creating IOS driver")
            return DriverFactory._create_ios_driver(
                config, ios_caps, environment, device, remote_server_url
            )

        raise ValueError(f"Unsupported platform: {platform}")

    # ================= ANDROID ================= #

    @staticmethod
    def _create_android_driver(config, caps, environment, device, remote_url):
        log.info("Setting Android capabilities")

        options = UiAutomator2Options().load_capabilities(caps)

        options.set_capability(
            "waitForIdleTimeout",
            config["performance"]["waitForIdleTimeout"]
        )
        options.set_capability(
            "waitForSelectorTimeout",
            config["performance"]["waitForSelectorTimeout"]
        )

        if device == "emulator" and "avd" in caps:
            log.info(f"Using Android Emulator AVD: {caps['avd']}")
            options.set_capability("avd", caps["avd"])

        server_url = (
            config["appium"]["server_url"]
            if environment == "dev" or not remote_url
            else remote_url
        )

        log.info(f"Connecting to Appium server: {server_url}")

        driver = webdriver.Remote(server_url, options=options)

        log.info("Android driver created successfully")
        return driver

    # ================= iOS ================= #

    @staticmethod
    def _create_ios_driver(config, caps, environment, device, remote_url):
        if not caps:
            raise ValueError("iOS capabilities are missing")

        log.info("Setting iOS capabilities")

        options = XCUITestOptions().load_capabilities(caps)

        if device == "simulator":
            log.info("Using iOS Simulator")
            options.set_capability("useNewWDA", True)

        server_url = (
            config["appium"]["server_url"]
            if environment == "dev" or not remote_url
            else remote_url
        )

        log.info(f"Connecting to Appium server: {server_url}")

        driver = webdriver.Remote(server_url, options=options)

        log.info("iOS driver created successfully")
        return driver
