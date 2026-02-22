from utils.runtime_config import get_runtime_config

def get_locator(android_locator, ios_locator):
    platform = get_runtime_config()["platform"]
    return android_locator if platform == "android" else ios_locator
