from .translate import data, translate


def main() -> int:
    for k, v in data.items():
        r = translate(k, v)
        print(r)
    return 0
