import requests
from config import *
from api_test.models.points_models import *


def get_points_by_param(headers: dict, params: dict = None):
    """
    Получить все пункты самовывоза, отфильтрованные по квери-параметру
    :param headers: токен
    :param params: service_id / region_id / city_id / restaurant_id / search / owner_type / country_id / active
    """

    response = requests.get(
        f"{STAND_URL}/api/courier_services/points/",
        headers=headers,
        params=params
    )
    return response


def get_point(headers: dict, point_id: int):
    """
    Получить ПВЗ по его id
    :param headers: токен
    :param point_id: id пункта самовывоза
    """

    response = requests.get(
        f"{STAND_URL}/api/courier_services/points/{point_id}",
        headers=headers
    )
    return response


def change_point(headers: dict, point_id: int, data: PointChange):
    """
    Отключить ПВЗ, изменить способы оплаты, изменить склад
    :param data: тело запроса
    :param headers: токен
    :param point_id: id пункта самовывоза
    """

    response = requests.put(
        f"{STAND_URL}/api/courier_services/points/company/{point_id}",
        headers=headers,
        data=data.model_dump_json(exclude_none=True)
    )
    return response


def change_many_points(headers: dict, data: PointChange, params: dict = None):
    """
    Множественное редактирование ПВЗ, отфильтрованных по квери-параметру - отключить, изменить способы оплаты и склад
    :param data: тело запроса
    :param params: region / region_id / city_id / service_id / service / restaurant_id
    :param headers: токен
    """

    response = requests.post(
        f"{STAND_URL}/api/courier_services/points/many",
        headers=headers,
        params=params,
        data=data.model_dump_json()
    )
    return response
