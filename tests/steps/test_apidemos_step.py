import logging
import allure
from pytest_bdd import given, when, then, parsers

from pages.apidemopage.apidemopages import ApiDemoPage
from pages.storepage.E2Eplaceorderpage import PlaceOrderPage
from utils.assertions import assert_true

# Logger at top (once)
log = logging.getLogger(__name__)


@given("the API Demos app is launched", target_fixture="apidemo")
def user_is_APIdemo(driver, wait_utils):
    apidemo = ApiDemoPage(driver, wait_utils)
    assert_true(apidemo.is_loaded_app(), "Home screen not loaded")
    return apidemo

@when("the user clicks on App")
def user_click_on_app(apidemo):
    apidemo.click_App()

@then("the user clicks on Activity")
def user_click_on_activity(apidemo):
    apidemo.click_Activity()

@then("the user clicks on Custom Title")
def user_click_on_custom_title(apidemo):
    apidemo.click_Title()

@then("the Custom Title screen should be displayed")
def user_click_on_screen(apidemo):
    assert apidemo.is_page_displayed(apidemo.driver)

