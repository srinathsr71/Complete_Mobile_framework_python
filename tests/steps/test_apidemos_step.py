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
    assert apidemo.is_page_displayed()

@then(parsers.parse('the user enters "{lefttextbox}" in Left Text Box'))
def user_click_on_left_text_box(apidemo, lefttextbox):
    log.info(f"user_click_on_left_text_box: {lefttextbox}")
    apidemo.Click_leftText(lefttextbox)


@then(parsers.parse('the user enters "{righttextbox}" in Right Text Box'))
def user_click_on_right_text_box(apidemo, righttextbox):
    log.info(f"user_click_on_right_text_box: {righttextbox}")
    apidemo.Click_rightText(righttextbox)



@then("the user clicks on Change Left Title")
def user_click_on_left_btn(apidemo):
    log.info(f"user_click_on_left_btn:")
    apidemo.Click_left_btn()

@then(parsers.parse('the left title should display as "{lefttextbox}"'))
def user_displayed_text(apidemo, lefttextbox):
    actual = apidemo.get_title_text()
    assert actual == lefttextbox

@when("the user clicks on Views")
def user_click_on_views(apidemo):
    log.info(f"user_click_on_views:")
    apidemo.click_view_option()

@then("user clicks on Controls")
def user_click_on_controls(apidemo):
    log.info(f"user_click_on_controls:")
    apidemo.click_controls_option()

@then("user clicks on Light Theme")
def user_click_on_light_theme(apidemo):
    log.info(f"user_click_on_light_theme:")
    apidemo.click_light_theme_option()

@then("the user selects the Checkbox")
def user_click_on_checkbox(apidemo):
    log.info(f"user_click_on_checkbox:")
    apidemo.click_cbox_option()

@then("the checkbox should be checked")
def checkbox_is_checked(apidemo):
    log.info(f"checkbox_is_checked:")
    apidemo.checkbox_click()

@then("user clicks on Dark Theme")
def user_click_on_light_theme(apidemo):
    log.info(f"user_click_on_dark_theme:")
    apidemo.click_dark_theme_option()

@then("the user selects RadioButton2")
def user_click_on_radio_button2(apidemo):
    log.info(f"user_click_on_radio_button2:")
    apidemo.click_rbtn_option()

@then("RadioButton2 should be selected")
def radio_button2_is_selected(apidemo):
   status= apidemo.rbtn_click()
   assert status is True


@then("the user clicks the Spinner dropdown")
def user_click_on_spinner(apidemo):
    log.info(f"user_click_on_spinner:")
    apidemo.click_spinner_option()

@then(parsers.parse('the user selects "{selection}"'))
def user_select(apidemo, selection):
    log.info(f"user_select text: {selection}:")
    print("the method is working")
    apidemo.select_text(selection)


@then(parsers.parse('"{selection}" should be displayed as selected option'))
def user_selected_option_displayed(apidemo, selection):
    log.info(f"user_selected_option_displayed: {selection}")
    actual=apidemo.get_selected_text()
    assert actual == selection



@when(parsers.parse("user clicks on App"))
def user_click_on_app(apidemo):
    log.info(f"user_click_on_app:")
    apidemo.click_app()

@then(parsers.parse("user clicks on alert dialogs"))
def user_click_on_alert_dialogs(apidemo):
    log.info(f"user_click_on_alert_dialogs:")
    apidemo.click_alert()

@then(parsers.parse("the user clicks OK Cancel dialog with a message"))
def user_click_on_ok_cancel_dialog(apidemo):
    log.info(f"user_click_on_ok_cancel_dialog:")
    apidemo.click_dialog()



@then(parsers.parse("the user clicks OK"))
def user_click_on_ok(apidemo):
    log.info(f"user_click_on_ok:")
    apidemo.click_okOption()

@then(parsers.parse("the dialog should close successfully"))
def user_click_on_dialog(apidemo):
    log.info(f"user_click_on_dialog:")
    assert apidemo.is_dialog_closed()

@then(parsers.parse("user clicks on Date Widgets"))
def user_click_on_date_widgets(apidemo):
    log.info(f"user_click_on_date_widgets:")
    apidemo.click_widget()

@then(parsers.parse("user clicks on Dialog"))
def user_click_on_dialog(apidemo):
    log.info(f"user_click_on_dialog:")
    apidemo.click_doption()


@then(parsers.parse("the user clicks CHANGE THE DATE"))
def user_click_on_dialog(apidemo):
    log.info(f"user_click_on_dialog:")
    apidemo.click_cdate()

@then(parsers.parse('the user selects date "{date}"'))
def user_click_on_dialog(apidemo, date):
    log.info(f"user_click_on_dialog:")
    apidemo.select_date_text(date)

@then(parsers.parse('the selected "{date}" should be displayed'))
def user_confirms_selection(apidemo,date):
    log.info(f"user_click_on_dialog:")
    print("Step reached")
    actual=apidemo.get_date_text()
    print("Actual date displayed:", actual)
    assert date in actual




















