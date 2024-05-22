from pydantic import Field
from typing import List, Optional
from .base_models import CustomBaseModel


class WorkTime(CustomBaseModel):
    """Режим работы ПВЗ"""

    dayTo: int
    timeTo: str
    dayFrom: int
    timeFrom: str


class PointsGet(CustomBaseModel):
    """Модель одного ПВЗ при запросе списка всех ПВЗ"""

    id: int
    owner_type: str
    name: str
    city_id: int
    city: str
    region: str
    region_id: int
    address: str
    lat: float
    lon: float
    work_time: Optional[List[WorkTime]]
    cash: bool
    card: bool
    service_id: str
    service_type: Optional[str] = None
    active: bool
    restaurant_id: str | None
    sklad: str | None
    shop_id: str | None
    tariffs: str | None


class PointGet(PointsGet):
    """Модель одного ПВЗ при запросе конкретного ПВЗ по id, дополняет предыдущую модель"""

    code: str
    metro: str | None
    postcode: str
    phone: str | None
    delivery_period: str | None
    trip_description: str | None
    return_: bool = Field(alias="return")
    max_size: str | None
    max_weight: str | None
    owner: str
    country: str
    type: Optional[str] = None


class PointChange(CustomBaseModel):
    """Изменение ПВЗ"""

    active: Optional[bool] = None
    card: Optional[bool] = None
    cash: Optional[bool] = None
    restaurant_id: Optional[str] = None
    sklad: Optional[str] = None


class PointsPagination(CustomBaseModel):
    """Пагинация"""

    count: int
    limit: int
    page: int
    total_pages: int
