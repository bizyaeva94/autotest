import requests
from config import *


def get_restaurants(headers: dict):
    response = requests.get(
        f"{STAND_URL}/api/restaurants/",
        headers=headers
    )
    return response

