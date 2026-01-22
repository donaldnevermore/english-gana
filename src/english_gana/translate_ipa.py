ipa_to_english_gana = {
    "iː": "ï",
    "i": "ï",
    "ɪ": "i",
    "uː": "ü",
    "u": "ü",
    "ʊ": "u",
    "ɜː": "é", # is equal to ə
    "ɜ": "é",
    "ə": "é",
    "ɔː": "o",
    "ɔ": "o",
    "ɒ": "ŏ",
    "æ": "ă",
    "ʌ": "ŭ",
    "ɑː": "a",
    "ɑ": "a",
    # e
    # diphthong
    "eɪ": "ā", # ei
    "ɔɪ": "oi",
    "aɪ": "ī", # äi
    "əʊ": "ō", # öu
    "aʊ": "äu",
    # ir, ur, er
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
    # The letters below are the same as in English Gana symbols.
    # b, d, f, h, k, l, m, n, p, r, s, t, v, w, z
    # tr, dr, ts, dz
}

easy_mark = {
    "iː": "ee",
    "i": "ee",
    "ɪ": "i",
    "uː": "oo",
    "u": "oo",
    "ʊ": "u",
    "ɜː": "ii",
    "ɜ": "ii",
    "ə": "ii",
    "ɔː": "o",
    "ɔ": "o",
    "ɒ": "oe", # British English
    "æ": "aa",
    "ʌ": "uu",
    "ɑː": "a",
    "ɑ": "a",
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


def translate_ipa(ipa: list[str]) -> list[str]:
    """translate IPA to English Gana symbols

    Args:
        ipa (list[str]): _description_

    Returns:
        list[str]: _description_
    """
    s: list[str] = []

    for ch in ipa:
        if ch in ipa_to_english_gana:
            s.append(ipa_to_english_gana[ch])
        else:
            s.append(ch)

    return s
