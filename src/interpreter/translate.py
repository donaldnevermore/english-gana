data: dict[str, str] = {"perfect": "pɜːrfɪkt"}

letter_to_ipa: dict[str, list[str]] = {
    "a": ["æ", "eɪ", "ɑː"],
    # b
    "c": ["k", "s"],
    # d
    "e": ["e", "iː", "ɜː"],
    # f
    "g": ["g", "dʒ"],
    # h
    "i": ["ɪ", "aɪ", "iː"],
    # j, k, l, m, n
    "o": ["ɑː", "əʊ", "ɔː"],
    # p, q, r, s, t
    "u": ["ʌ", "juː", "ʊ", "uː"],
    # v, w, x, y, z
}

letter_to_engana = {
    "a": ["a", "ā", "ä"],
    "c": ["k", "s"],
    "e": ["e", "ï", "ë"],
    "g": ["g", "j"],
    "i": ["i", "ī", "ï"],
    "o": ["ä", "ō", "ö"],
    "u": ["u", "ū", "û", "ü"],
}

sound_to_engana: dict[str, str] = {
    "iː": "ï",
    "ɪ": "i",
    "ʊ": "û",
    "uː": "ü",
    "ə": "é",
    "ɜː": "ë",
    "ɔː": "ö",
    "æ": "a",
    "ʌ": "u",
    "ɑː": "ä",
    # diphthong
    "eɪ": "ā",
    "ɔɪ": "oi",
    "aɪ": "ī",
    "əʊ": "ō",
    "aʊ": "ou",
    "juː": "ū",
    # consonant
    "tʃ": "ch",
    "dʒ": "j",
    "θ": "th",
    "ð": "t̂h",
    "ʃ": "sh",
    "ʒ": "ŝh",
    "j": "y",
    "ŋ": "ng",
}

sound_to_easy_ipa: dict[str, str] = {
    "iː": "ii",
    "ɪ": "i",
    "ʊ": "u",
    "uː": "uu",
    "ə": "_e",
    "ɜː": "_i",
    "ɔː": "oo",
    "æ": "_a",
    "ʌ": "_u",
    "ɑː": "aa",
    "ɒ": "o",
    # diphthong
    "eɪ": "ei",
    "ɔɪ": "oi",
    "aɪ": "ai",
    "əʊ": "ou",
    "aʊ": "au",
    # consonant
    "tʃ": "ch",
    "dʒ": "j",
    "θ": "th",
    "ð": "_th",
    "ʃ": "sh",
    "ʒ": "_sh",
    "j": "y",
    "ŋ": "ng",
}


def translate(word: str, sound: str) -> str:
    token = engana_word(sound)
    s: list[str] = []

    i, j = 0, 0
    while i < len(word) and j < len(token):
        if word[i] == token[j]:
            s.append(word[i])
        elif word[i] in letter_to_engana and token[j] in letter_to_engana[word[i]]:
            s.append(token[j])
        else:
            s.append(f"[{word[i]}]{{{token[j]}}}")

        i += 1
        j += 1

    return "".join(s)


def print_transform() -> None:
    x: dict[str, list[str]] = {}

    for k, v in letter_to_ipa.items():
        y: list[str] = []
        for i in v:
            if i in sound_to_engana:
                y.append(sound_to_engana[i])
            else:
                y.append(i)
        x[k] = y

    print(x)


def tokenize_ipa(sound: str) -> list[str]:
    """divide into IPA symbols

    Args:
        sound (str): _description_

    Returns:
        list[str]: _description_
    """
    s: list[str] = []

    i: int = 0
    while i < len(sound):
        ch: str = sound[i]
        if ch in ["ˈ", "ˌ", "/"]:
            i += 1
            continue
        if ch == "ɜ" and sound[i + 1] == "ː":
            s.append(sound[i : i + 2])
            i += 1
        else:
            s.append(ch)
        i += 1

    return s


def translate_ipa(ipa: list[str]) -> list[str]:
    """translate IPA to Engana symbols

    Args:
        ipa (list[str]): _description_

    Returns:
        list[str]: _description_
    """
    s: list[str] = []

    for ch in ipa:
        if ch in sound_to_engana:
            s.append(sound_to_engana[ch])
        else:
            s.append(ch)

    return s


def translate_to_easy_ipa(ipa: list[str]) -> list[str]:
    s: list[str] = []

    for ch in ipa:
        if ch in sound_to_easy_ipa:
            s.append(sound_to_easy_ipa[ch])
        else:
            s.append(ch)

    return s


def engana_word(ipa: str) -> list[str]:
    s = tokenize_ipa(ipa)
    return translate_ipa(s)
