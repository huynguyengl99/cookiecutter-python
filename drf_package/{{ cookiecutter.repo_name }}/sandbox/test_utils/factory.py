from typing import Any, TypeVar, get_args

import factory
{%- if cookiecutter.use_websocket %}
from asgiref.sync import sync_to_async
{%- endif %}
from factory.base import FactoryMetaClass

T = TypeVar("T")


class BaseFactoryMeta(FactoryMetaClass):
    def __new__(
        mcs, class_name: str, bases: tuple[type, ...], attrs: dict[str, Any]
    ) -> type["BaseModelFactory[T]"]:
        orig_bases = attrs.get("__orig_bases__", [])
        for t in orig_bases:
            if t.__name__ == "BaseModelFactory" and t.__module__ == __name__:
                type_args = get_args(t)
                if len(type_args) == 1:
                    if "Meta" not in attrs:
                        attrs["Meta"] = type("Meta", (), {})
                    attrs["Meta"].model = type_args[0]
        return super().__new__(mcs, class_name, bases, attrs)  # type: ignore


class BaseModelFactory(factory.django.DjangoModelFactory[T], metaclass=BaseFactoryMeta):
    class Meta:
        abstract = True

    @classmethod
    def create(cls, **kwargs: Any) -> T:
        return super().create(**kwargs)

    @classmethod
    def build(cls, **kwargs: Any) -> T:
        return super().build(**kwargs)

{%- if cookiecutter.use_websocket %}
    @classmethod
    async def acreate(cls, **kwargs: Any) -> T:
        return await sync_to_async(cls.create)(**kwargs)
{%- endif %}
