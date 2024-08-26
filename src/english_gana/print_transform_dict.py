from english_gana.translate_ipa import ipa_to_english_gana

letter_to_ipa = {
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
    "y": ["j", "aɪ"],
    # z
}


# A script to generate the letter_to_english_gana dict.
def print_transform_dict() -> None:
    d: dict[str, list[str]] = {}

    for key, vals in letter_to_ipa.items():
        arr: list[str] = []
        for i in vals:
            if i in ipa_to_english_gana:
                arr.append(ipa_to_english_gana[i])
            else:
                arr.append(i)
        d[key] = arr

    print(d)
