import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_guard import ensure_driver_alive


class BasePage:

    def __init__(self, driver, wait_utils):
        self.driver = driver
        self.driver = ensure_driver_alive(driver)
        self.wait = wait_utils

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def scroll_down(self):
        params = {
            "left": 100,
            "top": 400,
            "width": 800,
            "height": 1000,
            "direction": "down",
            "percent": 0.9
        }
        self.driver.execute_script("mobile: scrollGesture", params)

    def wait_for_small_delay(self, seconds=1):
        time.sleep(seconds)

    def is_loaded(self) -> bool:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement is_loaded()"
        )

    def scroll_and_click(self, text: str, max_scrolls: int = 5):

        for _ in range(max_scrolls):

            elements = self.driver.find_elements(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{text}")'
            )

            if elements:
                elements[0].click()
                return

            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 400,
                    "width": 800,
                    "height": 1000,
                    "direction": "down",
                    "percent": 0.9
                }
            )

        raise RuntimeError(
            f"Element with text '{text}' not found after scrolling"
        )
    APP_ID="com.androidsample.generalstore"
    def relaunch_app(self):
        self.driver.terminate_app(self.APP_ID)
        self.driver.activate_app(self.APP_ID)