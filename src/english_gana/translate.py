from .tokenize import tokenize_ipa

letter_to_english_gana = {
    "a": ["a", "ā", "ä"],
    "c": ["k", "s"],
    "e": ["e", "ï", "ë"],
    "g": ["g", "j"],
    "i": ["i", "ī", "ï"],
    "o": ["ä", "ō", "ö"],
    "u": ["u", "ū", "û", "ü"],
    "y": ["y", "ī"],
}

# different symbol, same sound.
# just for reference
special = {
    "c": ["c", "c̄"],
    "g": ["g", "ḡ"],
    "o": ["o", "ō", "ö"],
    "y": ["y", "ȳ"],
}

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


def english_gana(word: str, ipa: str) -> str:
    """translate to Engana

    Args:
        word (str): _description_
        sound (str): _description_

    Returns:
        str: _description_
    """
    sound = english_gana_mark(ipa)
    arr: list[str] = []

    i, j = 0, 0
    while i < len(word) and j < len(sound):
        if word[i] == sound[j]:
            arr.append(word[i])
            i += 1
            j += 1
        elif (
            word[i] in letter_to_english_gana
            and sound[j] in letter_to_english_gana[word[i]]
        ):
            if word[i] == "c":
                if sound[j] == "k":
                    arr.append(word[i])
                else:
                    arr.append(f"[{word[i]}]{{c̄}}")
            else:
                arr.append(f"[{word[i]}]{{{sound[j]}}}")
            i += 1
            j += 1
        else:
            # raise Exception(f"{word[i]} : {sound[j]}, not matched")
            arr.append(f"[{word[i]}]{{{sound[j]}}}")
            i += 1
            j += 1

    return "".join(arr)


def translate_ipa(ipa: list[str]) -> list[str]:
    """translate IPA to Engana symbols

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


def english_gana_mark(ipa: str) -> list[str]:
    s = tokenize_ipa(ipa)
    return translate_ipa(s)
