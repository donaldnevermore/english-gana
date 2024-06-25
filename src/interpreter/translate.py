data: dict[str, list[str]] = {"perfect": ["pɜːrfɪkt", "përfikt"]}

multi_sound_letters: dict[str, list[str]] = {
    "a": ["æ", "eɪ", "ɑː"],
    # b
    "c": ["k", "s"],
    # d
    "e": ["e", "iː", "ɜː"],
    # f
    "g": ["g", "dʒ"],
    # h
    "i": ["ɪ", "aɪ", "iː"],
}

sound_to_gana: dict[str, str] = {
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
    "ɔɪ": "oy",
    "aɪ": "ī",
    "əʊ": "ō",
    "aʊ": "ow",
    # consonant
    "tʃ": "ch",
    "dʒ": "j",
    "θ": "th",
    "ð": "t̂h",
    "ʃ": "sh",
    "ʒ": "ŝh",
    "j": "y",
}


def translate(word: str) -> str:
    s: list[str] = []

    ch: str
    for ch in word:
        ...

    return ""


def tokenize_ipa(sound: str) -> list[str]:
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
    s: list[str] = []

    for ch in ipa:
        if ch in sound_to_gana:
            s.append(sound_to_gana[ch])
        else:
            s.append(ch)

    return s


def tokenize_word(word: str) -> list[str]: ...
