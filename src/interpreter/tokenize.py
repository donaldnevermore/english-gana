def tokenize_ipa(txt: str) -> list[str]:
    """divide into IPA symbols

    Args:
        sound (str): _description_

    Returns:
        list[str]: _description_
    """
    arr: list[str] = []
    sound = remove_slash(txt)

    i: int = 0
    while i < len(sound):
        ch: str = sound[i]
        if ch in ["ˈ", "ˌ"]:
            i += 1
            continue

        if ch == "ɜ" and sound[i + 1] == "ː":
            arr.append(sound[i : i + 2])
            i += 1
        else:
            arr.append(ch)
        i += 1

    return arr


def remove_slash(s: str) -> str:
    return s.replace("/", "")


def remove_pitch(s: str) -> str:
    r = s.replace("ˈ", "")
    return r.replace("ˌ", "")
