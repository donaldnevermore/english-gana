from english_gana.tokenize import tokenize_ipa
from english_gana.translate_ipa import translate_ipa

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


def english_gana(word: str, ipa: str) -> str:
    """translate to English Gana

    Args:
        word (str): _description_
        ipa (str): _description_

    Returns:
        str: _description_
    """

    sound = english_gana_mark(ipa)
    result: list[str] = []

    i, j = 0, 0

    while True:
        if i >= len(word):
            break
        if j >= len(sound):
            if i >= 1 and word[i] == word[i - 1]:
                result.append(word[i:])
            else:
                result.append(f"[{word[i:]}]{{}}")
            break

        if word[i] == sound[j]:
            result.append(word[i])
            i += 1
            j += 1
        elif (
            word[i] in letter_to_english_gana
            and sound[j] in letter_to_english_gana[word[i]]
        ):
            if word[i] == "c":
                if sound[j] == "k":
                    result.append(word[i])
                else:
                    result.append(f"[{word[i]}]{{c̄}}")
                i += 1
                j += 1
            else:
                result.append(f"[{word[i]}]{{{sound[j]}}}")
                i += 1
                j += 1
        elif word[i] == "o":
            if sound[j] == "oi" and i + 1 < len(word) and word[i + 1] == "y":
                result.append(word[i : i + 2])
                i += 2
                j += 2
        elif word[i] == "s":
            if sound[j] == "sh" and i + 1 < len(word) and word[i + 1] == "h":
                result.append(word[i : i + 2])
                i += 2
                j += 2
        elif i >= 1 and word[i] == word[i - 1]:
            result.append(word[i])
            i += 1
        else:
            result.append(f"[{word[i]}]{{{sound[j]}}}")
            i += 1
            j += 1

    return "".join(result)


def english_gana_mark(ipa: str) -> list[str]:
    s = tokenize_ipa(ipa)
    return translate_ipa(s)
