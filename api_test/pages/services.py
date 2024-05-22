import requests
from config import *


def get_services(headers: dict, params: dict = None):
    response = requests.get(
        f"{STAND_URL}/api/services/",
        headers=headers,
        params=params
    )
    return response
