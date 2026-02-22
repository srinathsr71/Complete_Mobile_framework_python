from selenium.webdriver.support.ui import WebDriverWait

class WaitUtils:

    def __init__(self, driver, timeout, poll_frequency):
        self.wait = WebDriverWait(
            driver,
            timeout=timeout,
            poll_frequency=poll_frequency
        )

    def until(self, condition):
        return self.wait.until(condition)
