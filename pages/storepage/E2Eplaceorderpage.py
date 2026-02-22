import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.platform_utils import get_locator
from utils.webview_util import WebViewUtil

log = logging.getLogger(__name__)


class PlaceOrderPage(BasePage):


    COUNTRY_SPINNER = get_locator(
        (AppiumBy.ID,"com.androidsample.generalstore:id/spinnerCountry"),
        (AppiumBy.ID, "not implemented")
    )
    NAME_FIELD = get_locator(
        (AppiumBy.ID,"com.androidsample.generalstore:id/nameField"),
        (AppiumBy.ID, "not implemented")
    )
    GENDER_FEMALE =get_locator (
        (AppiumBy.ID,"com.androidsample.generalstore:id/radioFemale"),
        (AppiumBy.ID,"not implemented")
    )
    LETS_SHOP =get_locator(
        (AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop"),  # ANDROID
        (AppiumBy.ACCESSIBILITY_ID, "LetsShopButton")
    )
    PRODUCT_NAMES =get_locator ((AppiumBy.ID, "com.androidsample.generalstore:id/productName"),
                                (AppiumBy.ID, "not implemented")
    )
    ADD_TO_CART =get_locator((AppiumBy.ID,"com.androidsample.generalstore:id/productAddCart")
                             ,(AppiumBy.ID, "not implemented")
    )
    PRODUCT_PRICES =get_locator ((AppiumBy.ID, "com.androidsample.generalstore:id/productPrice")
                                 , (AppiumBy.ID, "not implemented")
    )

    TOTAL_AMOUNT =get_locator ((AppiumBy.ID, "com.androidsample.generalstore:id/totalAmountLbl")
                               ,(AppiumBy.ID, "not implemented")
    )
    CART_BUTTON = get_locator((AppiumBy.ID, "com.androidsample.generalstore:id/appbar_btn_cart")
                              ,(AppiumBy.ID, "not implemented")
    )

    PROCEED_BTN=get_locator((AppiumBy.ID, "com.androidsample.generalstore:id/btnProceed"),
                            (AppiumBy.ID, "not implemented")
    )

    def is_loaded(self) -> bool:
        """
        Verifies that the General Store home screen is loaded.
        Returns True if a key element is visible.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.COUNTRY_SPINNER)
            )
            return True
        except TimeoutException:
            return False


    def select_country(self, country):
        log.info("UI ACTION: Open country dropdown")
        self.click(self.COUNTRY_SPINNER)

        log.info(f"UI ACTION: Select country -> {country}")
        self.click(
            (AppiumBy.ANDROID_UIAUTOMATOR,
             f'new UiSelector().text("{country}")')
        )

    def select_country_diff(self, country):
        log.info("UI ACTION: Open country dropdown")
        self.click(self.COUNTRY_SPINNER)
        log.info(f"UI ACTION: Select country -> {country}")

    def enter_name(self, name):
        log.info(f"UI ACTION: Enter name -> {name}")
        self.type(self.NAME_FIELD, name)

    def select_gender(self, gender):
        log.info(f"UI ACTION: Select gender -> {gender}")
        self.click(self.GENDER_FEMALE)

    def click_lets_shop(self):
        log.info("UI ACTION: Click 'Let's Shop' button")
        self.click(self.LETS_SHOP)


 # ---------- CART ACTIONS ----------


    def scroll_and_add_product_by_name(self, product_name, max_scrolls=5):

        for _ in range(max_scrolls):

            products = self.driver.find_elements(*self.PRODUCT_NAMES)
            add_buttons = self.driver.find_elements(*self.ADD_TO_CART)

            for i in range(len(products)):
                name_on_screen = products[i].text.strip()

                if name_on_screen.lower() == product_name.strip().lower():
                    add_buttons[i].click()

                    # small wait to allow RecyclerView to refresh
                    self.wait_for_small_delay()
                    return

            self.scroll_down()

        raise RuntimeError(
            f"Product '{product_name}' not found after scrolling"
        )




    def click_cart(self):
        log.info("UI ACTION: Click 'cart' button")
        self.click(self.CART_BUTTON)

    def get_cart_price_elements(self):
        log.info("UI ACTION: get_cart_price_elements")

        self.wait.until(
            lambda d: len(d.find_elements(*self.PRODUCT_PRICES)) > 0
        )

        return self.driver.find_elements(*self.PRODUCT_PRICES)

    def get_calculated_cart_total(self):
        log.info("UI ACTION: get_calculated_cart_total")

        total = 0.0
        prices = self.get_cart_price_elements()

        for price in prices:
            total += float(
                price.text.replace("$", "").strip()
            )

        return total

    def get_displayed_cart_total(self):
        log.info("UI ACTION: get_displayed_cart_total")

        total_text = self.wait.until(
            lambda d: d.find_element(*self.TOTAL_AMOUNT).text
        )

        return float(total_text.replace("$", "").strip())

    def click_proceed(self):
        log.info("UI ACTION: Click 'proceed' button")
        self.click(self.PROCEED_BTN)

    def switch_to_webview(self):
        WebViewUtil(self.driver).switch_to_webview()

    def switch_to_native_app(self):
        # 1️⃣ Switch context
        WebViewUtil(self.driver).switch_to_native()

        # 2️⃣Relaunch app cleanly
        self.relaunch_app()

        # 3️⃣ VERIFY context
        log.info(f"Current context after relaunch: {self.driver.current_context}")
        assert self.driver.current_context == "NATIVE_APP"

    def get_web_page_title(self):
        return self.driver.title





