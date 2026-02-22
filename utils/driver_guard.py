from selenium.common.exceptions import WebDriverException
import logging

log = logging.getLogger(__name__)

def ensure_driver_alive(driver):
    try:
        driver.current_activity
        return driver
    except WebDriverException:
        log.warning("Driver session lost. Relaunching app.")
        driver.launch_app()
        return driver
