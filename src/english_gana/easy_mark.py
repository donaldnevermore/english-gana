easy_mark = {
    "iː": "ii",
    "ɪ": "i",
    "uː": "uu",
    "ʊ": "u",
    "ɜː": "e_",
    "ə": "o_",
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
    "ɜː": "ur",
    "ə": "uh",
    "ɔː": "aw",
    "ɒ": "o",
    "æ": "a",
    "ʌ": "u",
    "ɑː": "ah",
    # diphthong
    "eɪ": "ay",
    "ɔɪ": "oy",
    "aɪ": "y",
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
