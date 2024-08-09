from .translate import ipa_to_english_gana

letter_to_ipa: dict[str, list[str]] = {
    "a": ["æ", "eɪ", "ɑː"],
    # b
    "c": ["k", "s"],
    # d
    "e": ["e", "iː", "ɜː"],
    # f
    "g": ["g", "dʒ"],
    # h
    "i": ["ɪ", "aɪ", "iː"],
    # j, k, l, m, n
    "o": ["ɑː", "əʊ", "ɔː"],
    # p, q, r, s, t
    "u": ["ʌ", "juː", "ʊ", "uː"],
    # v, w, x
    "y": ["j", "ī"],
    # z
}


# generates the letter_to_english_gana dict
def print_transform() -> None:
    x: dict[str, list[str]] = {}

    for k, v in letter_to_ipa.items():
        y: list[str] = []
        for i in v:
            if i in ipa_to_english_gana:
                y.append(ipa_to_english_gana[i])
            else:
                y.append(i)
        x[k] = y

    print(x)
