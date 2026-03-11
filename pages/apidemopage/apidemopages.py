import logging

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.platform_utils import get_locator

log = logging.getLogger(__name__)


def click_Doption():
    log.info("UI ACTION: Click 'Dialog' option")


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
    Screen_view=get_locator((AppiumBy.XPATH, "//android.widget.TextView[@text='Left is best']"),(
        AppiumBy.ID, "not implemented"))

    left_text_box=get_locator((AppiumBy.ID,"io.appium.android.apis:id/left_text_edit"),
                              (AppiumBy.ID, "not implemented"))

    right_text_box=get_locator((AppiumBy.ID,"io.appium.android.apis:id/right_text_edit"),
                               (AppiumBy.ID, "not implemented"))
    click_left=get_locator((AppiumBy.ACCESSIBILITY_ID,"Change Left"),(AppiumBy.ID, "not implemented"))

    Tile_text=get_locator((AppiumBy.ID,"io.appium.android.apis:id/left_text"),(AppiumBy.ID, "not implemented"))

    click_views=get_locator((AppiumBy.ACCESSIBILITY_ID,"Views"),(AppiumBy.ID, "not implemented"))
    click_Controls=get_locator((AppiumBy.ACCESSIBILITY_ID,"Controls"),(AppiumBy.ID, "not implemented"))
    light_theme_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"1. Light Theme"),(AppiumBy.ID, "not implemented"))
    cBox=get_locator(
        (AppiumBy.ACCESSIBILITY_ID,"Checkbox 1"),(AppiumBy.ID, "not implemented") )

    dark_theme_option = get_locator((AppiumBy.ACCESSIBILITY_ID, "2. Dark Theme"), (AppiumBy.ID, "not implemented"))
    rbtn=get_locator(
        (AppiumBy.ACCESSIBILITY_ID,"RadioButton 1"),(AppiumBy.ID, "not implemented") )

    spinner=get_locator((AppiumBy.ID,"io.appium.android.apis:id/spinner1"),(AppiumBy.ID, "not implemented"))
    # select_e=get_locator((AppiumBy.XPATH, "//android.widget.TextView[@text='Earth']"),(AppiumBy.ID, "not implemented"))
    selectedText=get_locator((AppiumBy.ID,"android:id/text1"),(AppiumBy.ID,"not implemented"))

    app_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"App"),(AppiumBy.ID, "not implemented"))
    alert_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"Alert Dialogs"),(AppiumBy.ID,"not implemented"))
    dialog_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"OK Cancel dialog with a message"),(AppiumBy.ID,"not implemented"))
    dialogOkOption=get_locator((AppiumBy.ID,"android:id/button1"),(AppiumBy.ID,"not implemented"))

    datewidget=get_locator((AppiumBy.ACCESSIBILITY_ID,"Date Widgets"),(AppiumBy.ID,"not implemented"))
    Dialogoption=get_locator((AppiumBy.ACCESSIBILITY_ID,"1. Dialog"),(AppiumBy.ID, "not implemented"))
    Cdate=get_locator((AppiumBy.ACCESSIBILITY_ID,"change the date"),(AppiumBy.ID,"not implemented"))
    okoption=get_locator((AppiumBy.ID,"android:id/button1"),(AppiumBy.ID,"not implemented"))
    datedisplay=get_locator((AppiumBy.ID,"io.appium.android.apis:id/dateDisplay"),(AppiumBy.ID,"not implemented"))
    Ctime = get_locator((AppiumBy.ACCESSIBILITY_ID, "change the time"), (AppiumBy.ID, "not implemented"))
    # chour= get_locator((AppiumBy.ACCESSIBILITY_ID, "10"),(AppiumBy.ID,"not implemented"))
    # cmin = get_locator((AppiumBy.ACCESSIBILITY_ID, "30"), (AppiumBy.ID, "not implemented"))

    # wOption=get_locator((AppiumBy.ACCESSIBILITY_ID,"WebView"),(AppiumBy.ID,"not implemented"))

    dr_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"Drag and Drop"),(AppiumBy.ID, "not implemented"))
    drsource=get_locator((AppiumBy.ID,"io.appium.android.apis:id/drag_dot_1"),(AppiumBy.ID,"not implemented"))
    drtarget=get_locator((AppiumBy.ID,"io.appium.android.apis:id/drag_dot_2"),(AppiumBy.ID,"not implemented"))
    droptext=get_locator((AppiumBy.ID,"io.appium.android.apis:id/drag_result_text"),(AppiumBy.ID,"not implemented"))


    Expandable_list=get_locator((AppiumBy.ACCESSIBILITY_ID,"Expandable Lists"),(AppiumBy.ID,"not implemented"))
    Custom_adapter=get_locator((AppiumBy.ACCESSIBILITY_ID,"1. Custom Adapter"),(AppiumBy.ID,"not implemented"))
    Pname=get_locator((AppiumBy.XPATH,'//android.widget.TextView[@text="People Names"]'),(AppiumBy.ID,"not implemented"))

    sample_action=get_locator((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Sample action")'),(AppiumBy.ID,"not implemented"))

    makePopup_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"Make a Popup!"),(AppiumBy.ID,"not implemented"))
    click_option=get_locator((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Edit")'),(AppiumBy.ID,"not implemented"))

    click_link=get_locator((AppiumBy.LINK_TEXT, "i am a link"),(AppiumBy.ID,"not implemented"))
    gallery_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"Gallery"),(AppiumBy.ID,"not implemented"))
    photos_option=get_locator((AppiumBy.ACCESSIBILITY_ID,"1. Photos"),(AppiumBy.ID,"not implemented"))
    first_image_option=get_locator((AppiumBy.XPATH,'//android.widget.Gallery[@resource-id="io.appium.android.apis:id/gallery"]/android.widget.ImageView[1]'),())








    def click_App(self):
        log.info("UI ACTION: Click 'APP' option")
        self.click(self.App_option)

    def click_Activity(self):
        log.info("UI ACTION: Click 'Activity' option")
        self.click(self.App_Activity)

    def click_Title(self):
        log.info("UI ACTION: Click 'Activity' option")
        self.click(self.App_Title)

    def is_page_displayed(self):
        element = self.wait_for_presence(self.Screen_view)
        return element.is_displayed()


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


    def Click_leftText(self,ltext):
        log.info("UI ACTION: Click 'Left Text' option")
        self.type(self.left_text_box,ltext)

    def Click_rightText(self, rtext):
        log.info("UI ACTION: Click 'right Text' option")
        self.type(self.right_text_box, rtext)

    def Click_left_btn(self):
        log.info("UI ACTION: Click 'Left' option")
        self.click(self.click_left)


    def get_title_text(self):
        element = self.wait_element_visible(self.Tile_text)
        print("the left text is"+element.text)
        return element.text

    def click_view_option(self):
        log.info("UI ACTION: Click 'View' option")
        self.click(self.click_views)

    def click_controls_option(self):
        log.info("UI ACTION: Click 'Controls' option")
        self.click(self.click_Controls)

    def click_light_theme_option(self):
        log.info("UI ACTION: Click 'Light Theme' option")
        self.click(self.light_theme_option)

    def  click_cbox_option(self):
        log.info("UI ACTION: Click 'CheckBox' option")
        self.click(self.cBox)

    def checkbox_click(self):
        log.info("UI ACTION: Click 'Checkbox' option")
        element = self.wait_for_presence(self.cBox)
        return element.is_selected()

    def click_dark_theme_option(self):
        log.info("UI ACTION: Click 'Dark Theme' option")
        self.click(self.dark_theme_option)

    def click_rbtn_option(self):
        log.info("UI ACTION: Click 'RadioButton' option")
        self.click(self.rbtn)

    def rbtn_click(self):
        log.info("UI ACTION: Click 'radiobutton' option")
        element = self.wait_for_presence(self.rbtn)
        return element.get_attribute("checked") == "true"

    def click_spinner_option(self):
        log.info("UI ACTION: Click 'Spinner' option")
        self.click(self.spinner)

    def select_locator(self, selection):
        return (
            AppiumBy.XPATH,f"//android.widget.CheckedTextView[@text='{selection}']"
        )
    def select_text(self,selection):
        log.info("UI ACTION: select 'text' option")
        self.click(self.select_locator(selection))

    def get_selected_text(self):
        element = self.wait_element_visible(self.selectedText)
        print("the selected text is" + element.text)
        return element.text

    def click_app(self):
        log.info("UI ACTION: Click 'App' option")
        self.click(self.app_option)

    def click_alert(self):
        log.info("UI ACTION: Click 'Activity' option")
        self.click(self.alert_option)

    def click_dialog(self):
        log.info("UI ACTION: Click 'Dialog' option")
        self.click(self.dialog_option)

    def click_okOption(self):
        log.info("UI ACTION: Click 'OK' option")
        self.click(self.dialogOkOption)

    def is_dialog_closed(self):
        try:
            self.Invisible_element(self.dialogOkOption)
            return True
        except TimeoutException:
            return False



    def click_widget(self):
        log.info("UI ACTION: Click 'Widget' option")
        self.click(self.datewidget)

    def click_doption(self):
        log.info("UI ACTION: Click 'Doption' option")
        self.click(self.Dialogoption)

    def click_cdate(self):
        log.info("UI ACTION: Click 'Cdate' option")
        self.click(self.Cdate)


    def select_date(self, date):
        return (
            AppiumBy.XPATH,f"//android.view.View[@text='{date}']"
        )

    def select_date_text(self, date):
        log.info("UI ACTION: select 'text' option")
        self.click(self.select_date(date))
        self.click(self.okoption)


    def get_date_text(self):
        element = self.wait_element_visible(self.datedisplay)
        print("the date is" + element.text)
        return element.text

    def click_ctime(self):
        log.info("UI ACTION: Click 'Ctime' option")
        self.click(self.Ctime)

    def select_hour(self, hour):
        return (
            AppiumBy.XPATH, f"//*[@class='android.widget.RadialTimePickerView$RadialPickerTouchHelper' and @content-desc='{hour}']"
        )

    def select_min(self,minute):
        return (
            AppiumBy.XPATH,
            f"//*[@class='android.widget.RadialTimePickerView$RadialPickerTouchHelper' and @content-desc='{minute}']"
        )



    def click_hourmin(self,hour,minute):
        log.info("UI ACTION: Click 'Hourmin' option")
        self.click(self.select_hour(hour))
        self.click(self.select_min(minute))
        self.click(self.okoption)

    def scroll_text(self):
        log.info("UI ACTION: Scroll 'text' option")
        self.scroll_and_click("WebView",5)
        print(self.driver.contexts)



    def is_sandbox_title_displayed(self):
        contexts = self.driver.contexts
        self.driver.switch_to.context(contexts[1])

        element = self.find(
            (AppiumBy.XPATH, "//*[text()='This page is a Selenium sandbox']")
        )
        return element.is_displayed()

    def click_Drag_drop(self):
        log.info("UI ACTION: Click 'Drag' option")
        self.click(self.dr_option)


    def drag_drop(self):
        print(self.drsource)
        source = self.wait_for_presence(self.drsource)
        target = self.wait_for_presence(self.drtarget)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).pause(1).move_to_element(target).release().perform()

    def get_drop_text(self):
        element = self.wait_for_presence(
                (AppiumBy.ID, "io.appium.android.apis:id/drag_result_text")
            )
        return element.is_displayed()

    def click_expandable_list(self):
        log.info("UI ACTION: Click 'Expandable List' option")
        self.click(self.Expandable_list)

    def click_custom_adapter(self):
        log.info("UI ACTION: Click 'Custom Adapter' option")
        self.click(self.Custom_adapter)

    def click_long_press(self):
        log.info("UI ACTION: Click 'Long Press' option")
        element = self.find(self.Pname)
        finger = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to(element)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(2)  # hold for 2 seconds
        actions.pointer_action.pointer_up()

        actions.perform()
        self.click(self.sample_action)

    def Is_toast_message_displayed(self):
        element = self.wait_for_presence(
                (AppiumBy.XPATH, "//android.widget.Toast")
            )
        return element.text

    def scroll_Popmenu(self):
        log.info("UI ACTION: Scroll 'text' option")
        self.scroll_and_click("Popup Menu",5)



    def click_makepopup(self):
        log.info("UI ACTION: Click 'Make Popup' option")
        self.click(self.makePopup_option)

    def click_edit_option(self):
        log.info("UI ACTION: Click 'Edit Option' option")
        self.click(self.click_option)

    def click_link_option(self):
        log.info("UI ACTION: Click 'Link Option' option")
        contexts = self.driver.contexts
        self.driver.switch_to.context(contexts[1])
        linkoption=self.find(self.click_link)
        self.click(linkoption)


    def is_text_visible(self):
        log.info("UI ACTION: Is Text Visible")
        element = self.find(
            (By.XPATH, "//*[contains(text(),'I am some other page content')]")
        )
        return element.is_displayed()


    def rotate_to_landscape(self):
        self.driver.orientation = "LANDSCAPE"

    def get_orientation(self):
        return self.driver.orientation


    def click_gallery(self):
        log.info("UI ACTION: Click 'Gallery' option")
        self.click(self.gallery_option)

    def click_photos(self):
        log.info("UI ACTION: Click 'Photos' option")
        self.click(self.photos_option)

    def open_first_image(self):
        image = self.find(self.first_image_option)
        image.click()

    def pinch_image(self):
        element = self.find(self.first_image_option)

        self.driver.execute_script(
            "mobile: pinchCloseGesture",
            {
                "elementId": element.id,
                "percent": 0.75,
                "speed": 200
            }
        )

    def is_image_displayed(self):
        element = self.find(self.first_image_option)
        return element.is_displayed()







