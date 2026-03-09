import logging

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from utils.platform_utils import get_locator

log = logging.getLogger(__name__)


class ApiDemoPage(BasePage):


    App_option = get_locator(
        (AppiumBy.ACCESSIBILITY_ID,"App"),
        (AppiumBy.ID, "not implemented")
    )

    App_Activity = get_locator(
        (AppiumBy.ACCESSIBILITY_ID, "Activity"),
        (AppiumBy.ID, "not implemented")
    )

    App_Title = get_locator(
        (AppiumBy.ACCESSIBILITY_ID, "Custom Title"),
        (AppiumBy.ID, "not implemented")
    )

    def click_App(self):
        log.info("UI ACTION: Click 'APP' option")
        self.click(self.App_option)

    def click_Activity(self):
        log.info("UI ACTION: Click 'Activity' option")
        self.click(self.App_Activity)

    def click_Title(self):
        log.info("UI ACTION: Click 'Activity' option")
        self.click(self.App_Title)

    def is_page_displayed(self, driver):
        return driver.find_element(*self.App_Title).is_displayed()


    def is_loaded_app(self) -> bool:
        """
        Verifies that the General Store home screen is loaded.
        Returns True if a key element is visible.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.App_option)
            )
            return True
        except TimeoutException:
            return False