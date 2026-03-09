import logging
import allure
from pytest_bdd import given, when, then, parsers
from pages.storepage.E2Eplaceorderpage import PlaceOrderPage
from utils.assertions import assert_true


# Logger at top (once)
log = logging.getLogger(__name__)


@given("user is on General Store home", target_fixture="home")
def user_is_on_home(driver, wait_utils):
    home = PlaceOrderPage(driver, wait_utils)
    assert_true(home.is_loaded(), "Home screen not loaded")
    return home


@when(parsers.parse('user selects country "{country}"'))
def select_country(home, country):
    with allure.step(f"User selects country: {country}"):
        log.info(f"STEP: User selects country -> {country}")
        home.select_country(country)

@when(parsers.parse('user selects different country "{country}"'))
def select_diff_country(home, country):
    with allure.step(f"User selects different country -> {country}"):
        log.info(f"STEP: User selects different country -> {country}")
        home.select_country_diff(country)
        home.scroll_and_click("India",15)


@when(parsers.parse('user enters name "{name}"'))
def enter_name(home, name):
    with allure.step(f"User enters name: {name}"):
        log.info(f"STEP: User enters name -> {name}")
        home.enter_name(name)


@when(parsers.parse('user selects gender "{gender}"'))
def select_gender(home, gender):
    with allure.step(f"User selects gender: {gender}"):
        log.info(f"STEP: User selects gender -> {gender}")
        home.select_gender(gender)


@then("user proceeds to shop")
def proceed(home):
    with allure.step("User proceeds to shop"):
        log.info("STEP: User proceeds to shop")
        home.click_lets_shop()

@then("user added product to the cart")
def add_Product_to_cart(home):
    print("user added product to the cart")
    home.scroll_and_add_product_by_name("Converse All Star", 5)
    home.scroll_and_add_product_by_name("Air Jordan 9 Retro", 5)

@then("user click on add to cart")
def click_on_add_to_cart(home):
    print("user click on add to cart")
    home.click_cart()

@then("user verify the cart total amount")
def Cart_total(home):
    print("user verify the cart total amount")
    log.info("STEP: Validating added product total price")

    prices = home.get_cart_price_elements()
    log.info(f"Cart price elements found = {len(prices)}")

    expected_sum = home.get_calculated_cart_total()
    actual_total = home.get_displayed_cart_total()

    assert abs(actual_total - expected_sum) < 0.01, \
        f"Total price mismatch: expected {expected_sum}, got {actual_total}"



@then("user click on proceed button")
def click_proceed_button(home):
    print("user click on proceed button")
    home.click_proceed()

@then("user navigating to web view")
def navigate_to_web(home):
    print("user navigating to web view")
    home.switch_to_webview()


@then("user verifies the title of the page")
def title_page(home):
    print("user verifies the title of the page")
    print("the title of the page is"+home.get_web_page_title())

@then("user return to native app")
def return_native_app(home):
    print("user return to native app")
    home.switch_to_native_app()
