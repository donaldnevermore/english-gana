from .translate import english_gana

data: dict[str, str] = {"perfect": "pɜːrfɪkt"}


def main() -> int:
    for k, v in data.items():
        r = english_gana(k, v)
        print(r)
    return 0
