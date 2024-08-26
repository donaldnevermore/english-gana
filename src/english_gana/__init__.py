from english_gana.translate import english_gana

data = {"perfect": "pɜːrfɪkt"}


def main() -> int:
    for k, v in data.items():
        res = english_gana(k, v)
        print(res)
    return 0
