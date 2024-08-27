ipa_to_easy_mark = {
    "iː": "ii",
    "ɪ": "i",
    "uː": "uu",
    "ʊ": "u",
    "ɜː": "i_",
    "ə": "e_",
    "ɔː": "oo",
    "ɒ": "o",
    "æ": "a_",
    "ʌ": "u_",
    "ɑː": "aa",
    # diphthong
    "eɪ": "ei",
    "ɔɪ": "oi",
    "aɪ": "ai",
    "əʊ": "ou",
    "aʊ": "au",
    "juː": "yuu",
    # consonant
    "tʃ": "ch",
    "dʒ": "j",
    "θ": "th",
    "ð": "dh",
    "ʃ": "sh",
    "ʒ": "zh",
    "j": "y",
    "ŋ": "ng",
    "ɡ": "g",
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
