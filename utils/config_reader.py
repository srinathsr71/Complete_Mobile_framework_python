# import yaml
# import json
# import os
#
#
# def get_project_root():
#     """
#     Returns absolute path of project root directory
#     """
#     return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#
#
# def load_config():
#
#     project_root = get_project_root()
#
#     config_path = os.path.join(project_root, "config", "config.yml")
#
#     print("Loading config from:", config_path)   # DEBUG LINE
#
#     if not os.path.exists(config_path):
#         raise FileNotFoundError(f"config.yml NOT FOUND at {config_path}")
#
#     with open(config_path, "r") as file:
#         return yaml.safe_load(file)
#
#
#
# def load_android_caps():
#
#     project_root = get_project_root()
#
#     caps_path = os.path.join(project_root, "config", "android_caps.json")
#
#     print("Loading caps from:", caps_path)   # DEBUG LINE
#
#     if not os.path.exists(caps_path):
#         raise FileNotFoundError(f"android_caps.json NOT FOUND at {caps_path}")
#
#     with open(caps_path, "r") as file:
#         return json.load(file)
#
# def load_ios_caps():
#
#     project_root = get_project_root()
#
#     caps_path = os.path.join(project_root, "config", "ios_caps.json")
#
#     print("Loading caps from:", caps_path)   # DEBUG LINE
#
#     if not os.path.exists(caps_path):
#         raise FileNotFoundError(f"android_caps.json NOT FOUND at {caps_path}")
#
#     with open(caps_path, "r") as file:
#         return json.load(file)


import os
import yaml
import json


def load_config():
    env = os.getenv("ENV", "dev")
    with open(f"config/{env}/config.yml", "r") as f:
        return yaml.safe_load(f)


def load_android_caps():
    env = os.getenv("ENV", "dev")
    with open(f"config/{env}/android_caps.json", "r") as f:
        return json.load(f)


def load_ios_caps():
    env = os.getenv("ENV", "dev")
    with open(f"config/{env}/ios_caps.json", "r") as f:
        return json.load(f)
