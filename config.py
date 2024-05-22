import yaml
import os

abspath = os.path.dirname(os.path.abspath(__file__))

with open(f"{abspath}/config.yaml", "r") as config_file:
    parameters = yaml.safe_load(config_file)

ADMIN_LOGIN = parameters.get("admin", dict()).get("login", None)
ADMIN_PASSWORD = parameters.get("admin", dict()).get("password", None)

MANAGER_LOGIN = parameters.get("manager", dict()).get("login", None)
MANAGER_PASSWORD = parameters.get("manager", dict()).get("password", None)

COURIER_LOGIN = parameters.get("courier", dict()).get("login", None)
COURIER_PASSWORD = parameters.get("courier", dict()).get("password", None)

STAND_URL = parameters.get("stand", dict()).get("url", None)
