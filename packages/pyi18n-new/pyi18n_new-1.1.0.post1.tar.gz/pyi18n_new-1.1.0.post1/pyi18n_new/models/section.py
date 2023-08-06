import contextlib
from ..lib.base_class import BaseClass

from ..models.value import TranslateList, TranslateStr, TranslateDict


def to_pyi18n_type(value: str | list | dict) -> TranslateStr | TranslateList | TranslateDict:
    if isinstance(value, str):
        return TranslateStr(value)
    elif isinstance(value, list):
        return TranslateList(value)
    elif isinstance(value, dict):
        return TranslateDict(value)


class Section(BaseClass):
    def __init__(self, name: str, entries: dict, pyi18n):
        self.__pyi18n = pyi18n
        self.__name = name

        for key, value in entries.items():
            setattr(self, key, to_pyi18n_type(value))

    def __getattr__(self, name: str) -> TranslateStr | TranslateList | TranslateDict:
        with contextlib.suppress(AttributeError):
            return self.__getattribute__(name)
        with contextlib.suppress(AttributeError):
            return self.__pyi18n[self.__pyi18n.fallback][self.__name].__getattribute__(name)
        return f"{self.__name}.{name}"
