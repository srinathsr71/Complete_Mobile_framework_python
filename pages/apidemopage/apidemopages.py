import logging

from selenium.common import TimeoutException
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
