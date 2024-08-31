two_parts = [
    "iː",
    "uː",
    "ɜː",
    "ɔː",
    "ɑː",
    "eɪ",
    "ɔɪ",
    "aɪ",
    "əʊ",
    "aʊ",
    "tʃ",
    "dʒ",
]


def is_two_parts(i: int, sound: str) -> bool:
    if i + 1 >= len(sound):
        return False

    for elem in two_parts:
        if sound[i : i + 2] == elem:
            return True

    return False


def tokenize_ipa(txt: str) -> list[str]:
    """divide into IPA symbols

    Args:
        sound (str): _description_

    Returns:
        list[str]: _description_
    """
    result: list[str] = []
    sound = remove_slash(txt)

    i = 0
    while i < len(sound):
        if sound[i] in ["ˈ", "ˌ"]:
            i += 1
            continue

        if is_two_parts(i, sound):
            result.append(sound[i : i + 2])
            i += 2
        else:
            result.append(sound[i])
            i += 1

    return result


def remove_slash(s: str) -> str:
    return s.replace("/", "")


def remove_pitch(s: str) -> str:
    r = s.replace("ˈ", "")
    return r.replace("ˌ", "")


def remove_slash_pitch(s: str) -> str:
    return remove_pitch(remove_slash(s))
