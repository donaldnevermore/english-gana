respelling = {
    "iː": "ee",
    "i": "ee",
    "ɪ": "i",
    "uː": "oo",
    "u": "oo",
    "ʊ": "uu",
    "ɜː": "uh", # also ur
    "ɜ": "uh",
    "ə": "uh",
    "ɔː": "aw",
    "ɔ": "aw",
    "ɒ": "o",
    "æ": "a",
    "ʌ": "u",
    "ɑː": "ah",
    "ɑ": "ah",
    # diphthong
    "eɪ": "ay",
    "ɔɪ": "oy",
    "aɪ": "igh",
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


def translate_to_respelling(ipa: list[str]) -> list[str]:
    s: list[str] = []

    for ch in ipa:
        if ch in respelling:
            s.append(respelling[ch])
        else:
            s.append(ch)

    return s
