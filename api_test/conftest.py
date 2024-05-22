import pytest
import requests
from config import *
from .models import *


@pytest.fixture(scope="session")
def admin_auth():
    auth_data = Auth(login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    response = requests.post(f"{STAND_URL}/api/users/login", data=auth_data.model_dump())
    return {
        "x-access-token": Token(**response.json()).token,
        "content-type": "application/json",
    }


@pytest.fixture(scope="session")
def manager_auth():
    auth_data = Auth(login=MANAGER_LOGIN, password=MANAGER_PASSWORD)
    response = requests.post(f"{STAND_URL}/api/users/login", data=auth_data.model_dump())
    return {
        "x-access-token": Token(**response.json()).token,
        "content-type": "application/json",
    }


@pytest.fixture(scope="session")
def courier_auth():
    auth_data = Auth(login=COURIER_LOGIN, password=COURIER_PASSWORD)
    response = requests.post(f"{STAND_URL}/api/users/login", data=auth_data.model_dump())
    return {
        "x-access-token": Token(**response.json()).token,
        "content-type": "application/json",
    }

