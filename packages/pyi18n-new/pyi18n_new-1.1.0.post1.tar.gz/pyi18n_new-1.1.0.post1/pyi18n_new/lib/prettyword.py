def prettyword(n: int, forms: list | tuple | str) -> str:
    if isinstance(forms, str):
        return forms

    if n == 0:
        return forms[0]
    elif n % 100 in [11, 12, 13, 14]:
        return forms[3]
    elif n % 10 == 1:
        return forms[1]
    elif n % 10 in [2, 3, 4]:
        return forms[2]
    else:
        return forms[3]


def prettyword_en(n: int, forms: list | tuple) -> str:
    if n == 1:
        return forms[0]
    else:
        return forms[1]
