ipa_to_easy_mark: dict[str, str] = {
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


# different symbol, same sound.
# just for reference
special = {
    "c": ["c", "c̄"],
    "g": ["g", "ḡ"],
    "o": ["o", "ō", "ö"],
    "y": ["y", "ȳ"],
}


def translate_to_easy_mark(ipa: list[str]) -> list[str]:
    s: list[str] = []

    for ch in ipa:
        if ch in ipa_to_easy_mark:
            s.append(ipa_to_easy_mark[ch])
        else:
            s.append(ch)

    return s
