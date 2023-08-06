import yaml

from dataclasses import dataclass
from pathlib import Path

from .models.locale import Locale, LocaleConfig
from .models.value import TranslateDict, TranslateStr, TranslateList
from .lib.base_class import BaseClass


@dataclass
class I18N(BaseClass):
    path: Path
    default: str = "en"
    fallback: str = None

    def __post_init__(self):
        if self.fallback is None:
            self.fallback = self.default

        folders = list(self.path.iterdir())

        for folder in folders:
            locale = self.get_locale(folder)
            setattr(self, folder.name, locale)

    def __getattr__(self, name: str) -> TranslateStr | TranslateList | TranslateDict:
        return self[self.default][name]

    @property
    def languages(self) -> list[str]:
        """Get list of used languages"""

        return [_ for _, locale in self.__dict__.items() if isinstance(locale, Locale)]

    def get_locale(self, path: Path) -> Locale:
        """Get locale with params"""

        with (path / "__init__.yml").open() as file:
            config = yaml.safe_load(file.read())
            return Locale(LocaleConfig(lang=path.name, path=path, **config), self)

    def translate(
        self,
        path: str,
        lang: str = None,
        **kwargs
    ) -> TranslateStr | TranslateList | TranslateDict:
        """python-i18n compatible interface"""

        section, name = path.split(".")

        return self[lang or self.default][section][name](**kwargs)
