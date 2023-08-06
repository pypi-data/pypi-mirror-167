import re
import random

from pyi18n_new.lib.prettyword import prettyword, prettyword_en


class TranslateList(list):
    def _(self, **kwargs):
        if kwargs.get("went_random", False):
            return TranslateStr(random.choice(self))(**kwargs)

        return self

    __call__ = _


class TranslateDict(dict):
    def _(self, **kwargs):
        return self

    __call__ = _


class TranslateStr(str):
    def _(self, **kwargs):
        return re.sub(r"{.+?}", lambda x: self._format(x.group()[1:-1], **kwargs), self)

    def _format(self, text: str, **kwargs) -> str:
        if "|" in text:
            cases = re.split(r"\s\|\s", text)

            VAR_TYPE_2 = r"\$\w{1,}"
            first_var = re.findall(VAR_TYPE_2, text)[0][1:]

            count = kwargs[first_var]

            if len(cases) == 2:
                text = cases[0] if count == (0, 1) else cases[1]

            text = prettyword(count, cases) if len(cases) > 2 else prettyword_en(count, cases)
            return re.sub(VAR_TYPE_2, lambda x: str(kwargs[x.group()[1:]]), text)

        elif "::" in text:
            try:
                section, var = text.split("::")
            except:
                section, var = "current", text

            return self._[section][var](**kwargs)

        else:
            return str(kwargs.get(text))

    __call__ = _
