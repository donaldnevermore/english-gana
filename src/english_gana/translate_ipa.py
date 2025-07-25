ipa_to_english_gana = {
    "iː": "ï",
    "ɪ": "i",
    "uː": "ü",
    "ʊ": "u",
    "ɜː": "é", # is equal to ə
    "ə": "é", # also ê
    "ɔː": "o",
    "ɒ": "ô",
    "æ": "â",
    "ʌ": "û",
    "ɑː": "a",
    # e
    # diphthong
    "eɪ": "ā", # ei or ëi
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
