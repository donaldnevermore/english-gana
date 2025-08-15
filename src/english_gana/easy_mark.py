easy_mark = {
    "iː": "ee",
    "ɪ": "i",
    "uː": "oo",
    "ʊ": "u",
    "ɜː": "ii",
    "ə": "ii",
    "ɔː": "o",
    "ɒ": "oe", # British English
    "æ": "aa",
    "ʌ": "uu",
    "ɑː": "a",
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
    "ð": "dh",
    "ʃ": "sh",
    "ʒ": "zh",
    "j": "y",
    "ŋ": "ng",
    "ɡ": "g",
}

respelling = {
    "iː": "ee",
    "i": "ee",
    "ɪ": "i",
    "uː": "oo",
    "u": "oo",
    "ʊ": "uu",
    "ɜː": "uh", # also ur
    "ə": "uh",
    "ɔː": "aw",
    "ɒ": "o",
    "æ": "a",
    "ʌ": "u",
    "ɑː": "aa",
    # diphthong
    "eɪ": "ay",
    "ɔɪ": "oy",
    "aɪ": "y", # also igh
    "əʊ": "oh",
    "aʊ": "ow",
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


def translate_to_easy_mark(ipa: list[str]) -> list[str]:
    s: list[str] = []

    for ch in ipa:
        if ch in easy_mark:
            s.append(easy_mark[ch])
        else:
            s.append(ch)

    return s
