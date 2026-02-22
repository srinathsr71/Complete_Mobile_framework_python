import os


def get_runtime_config():
    return {
        "platform_type": os.getenv("PLATFORM_TYPE", "mobile"),
        "platform": os.getenv("PLATFORM", "android"),
        "device": os.getenv("DEVICE", "mobile"),
        "environment": os.getenv("ENV", "dev"),
        "remote_server_url": os.getenv("REMOTE_SERVER_URL"),
    }