import time
import logging

log = logging.getLogger(__name__)

class WebViewUtil:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_webview(self, timeout=10):
        log.info("Switching to WebView context")

        end_time = time.time() + timeout
        while time.time() < end_time:
            contexts = self.driver.contexts
            log.info(f"Available contexts: {contexts}")

            for context in contexts:
                if "WEBVIEW" in context:
                    self.driver.switch_to.context(context)
                    log.info(f"Switched to context: {context}")
                    return

            time.sleep(1)

        raise RuntimeError("WEBVIEW context not found")

    def switch_to_native(self):
        log.info("Switching back to NATIVE_APP context")
        self.driver.switch_to.context("NATIVE_APP")