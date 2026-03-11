import logging
import allure
from cffi.cparser import Parser
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


@then(parsers.parse("the user clicks CHANGE THE TIME"))
def user_clicks_on_Ctime(apidemo):
    log.info(f"user_clicks_on_Ctime:")
    apidemo.click_ctime()


@then(parsers.parse('the user selects hour "{hour}" and "{minute}"'))
def user_clicks_on_chour_cmin(apidemo,hour,minute):
    log.info(f"user_clicks_on_chour_cmin:")
    apidemo.selected_time = f"{hour}:{minute}"
    print("the selected time displayed:", apidemo.selected_time)
    apidemo.click_hourmin(hour,minute)

@then(parsers.parse("the selected time should be displayed"))
def user_shows_time(apidemo):
    log.info(f"user_shows_time:")
    actual = apidemo.get_date_text()
    print("Actual date displayed:", actual)
    actual_time = actual.split(" ")[1]  # gets HH:MM
    assert actual_time == apidemo.selected_time

@then(parsers.parse("the user scrolls down the screen and click webview option"))
def user_scrolls_down(apidemo):
    log.info(f"user_scrolls_down:")
    apidemo.scroll_text()



@then(parsers.parse("verify the title of the page"))
def verify_title(apidemo):
    log.info(f"verify_title:")
    assert apidemo.is_sandbox_title_displayed()


@then(parsers.parse(("user clicks on Drag and Drop")))
def user_clicks_on_drag_and_drop(apidemo):
    log.info(f"user_clicks_on_drag_and_drop:")
    apidemo.click_Drag_drop()


@then(parsers.parse("the user drags the first dot to the second dot"))
def user_clicks_on_drag_and_drop(apidemo):
    log.info(f"user_clicks_on_drag_and_drop:")
    apidemo.drag_drop()


@then(parsers.parse("verify the dropped text is visible"))
def verify_dropped_text(apidemo):
    log.info(f"verify_dropped_text:")
    assert apidemo.get_drop_text()


@then(parsers.parse("user clicks on Expandable Lists"))
def user_clicks_on_expandable_list(apidemo):
    log.info(f"user_clicks_on_expandable_list:")
    apidemo.click_expandable_list()


@then(parsers.parse("user clicks on custom adapter"))
def user_clicks_on_adapter(apidemo):
    log.info(f"user_clicks_on_adapter:")
    apidemo.click_custom_adapter()

@then(parsers.parse("the user long presses on People Names"))
def user_clicks_on_long_presses(apidemo):
    log.info(f"user_clicks_on_long_presses:")
    apidemo.click_long_press()

@then(parsers.parse("verify the toast message by clicking sample action"))
def toast_message_displayed(apidemo):
    log.info(f"toast_message_displayed:")
    assert apidemo.Is_toast_message_displayed() == "People Names: Group 0 clicked"

@then(parsers.parse("user clicks on Popupmenu"))
def user_clicks_on_popupmenu(apidemo):
    log.info(f"user_clicks_on_popupmenu:")
    apidemo.scroll_Popmenu()

@then(parsers.parse("the user clicks Make a Popup!"))
def user_clicks_on_make_popup(apidemo):
    log.info(f"user_clicks_on_make_popup:")
    apidemo.click_makepopup()

@then(parsers.parse("the user selects an option"))
def user_clicks_on_select_option(apidemo):
    log.info(f"user_clicks_on_select_option:")
    apidemo.click_edit_option()

@then(parsers.parse("a toast message should appear"))
def toast_message_displayed(apidemo):
    log.info(f"toast_message_displayed:")
    assert apidemo.Is_toast_message_displayed() == "Clicked popup menu item Edit"

@then(parsers.parse("user click on link in the webview"))
def user_link_in_webview(apidemo):
    log.info(f"user_link_in_webview:")
    apidemo.click_link_option()




@then(parsers.parse("the text should be displayed"))
def text_displayed(apidemo):
    log.info(f"text_displayed:")
    assert apidemo.is_text_visible()


@when("the device orientation changes to landscape")
def rotate_device(apidemo):
    apidemo.rotate_to_landscape()

@then("the application should adjust to landscape mode")
def verify_landscape(apidemo):
    assert apidemo.get_orientation() == "LANDSCAPE"


@then(parsers.parse("user clicks on Gallery"))
def user_clicks_on_gallery(apidemo):
    log.info(f"user_clicks_on_gallery:")
    apidemo.click_gallery()
    apidemo.click_photos()

@then(parsers.parse("the user performs a pinch gesture on the image"))
def user_clicks_on_gesture(apidemo):
    log.info(f"user_clicks_on_gesture:")
    apidemo.open_first_image()
    apidemo.pinch_image()

@then(parsers.parse("the image should zoom out"))
def zoom_out(apidemo):
    log.info(f"zoom_out:")
    assert  apidemo.is_image_displayed()


















