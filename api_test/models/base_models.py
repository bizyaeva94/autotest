import json

from typing import Any, Type, TypeVar
from pydantic import BaseModel


Model = TypeVar('Model', bound='BaseModel')


class CustomBaseModel(BaseModel):
    """
    Модель используется для наследования во всех последующих моделях вместо BaseModel.
    Переопределяется метод model_dump_json, в котором происходит кодирование в utf-8,
    чтобы можно было передавать в json в теле запроса текст на кириллице.
    Переопределяется метод model_validate, в котором включается параметр strict=True,
    чтобы всегда была строгая валидация типов данных.
    """

    def model_dump_json(self, exclude_none: bool = False, *args, **kwargs):
        if exclude_none:
            data = {}
            for key, value in self.model_dump(by_alias=True).items():
                if value is not None:
                    data.update({key: value})
            return json.dumps(data).encode("utf-8")
        return json.dumps(self.model_dump(by_alias=True)).encode("utf-8")

    @classmethod
    def model_validate(
        cls: Type[Model],
        obj: Any,
        *,
        strict: bool | None = True,
        from_attributes: bool | None = None,
        context: dict[str, Any] | None = None,
    ) -> Model:
        return super().model_validate(obj=obj, strict=strict, from_attributes=from_attributes, context=context)


class Auth(CustomBaseModel):
    """Авторизация с логином и паролем, используется в фикстурах"""

    login: str
    password: str


class Token(CustomBaseModel):
    """Токен, который получается в результате авторизации и прокидывается в header во всех последующих запросах"""

    token: str
    type: str
