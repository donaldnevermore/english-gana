ipa_to_english_gana: dict[str, str] = {
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


def translate_ipa(ipa: list[str]) -> list[str]:
    """translate IPA to English gana symbols

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
