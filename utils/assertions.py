import allure
import logging

log = logging.getLogger(__name__)

def assert_true(condition, message):
    if not condition:
        log.error(message)
        allure.attach(message, name="Assertion Failure")
        raise AssertionError(message)
