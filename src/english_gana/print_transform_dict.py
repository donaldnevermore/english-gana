from english_gana.translate_ipa import ipa_to_english_gana

letter_to_ipa = {
    "a": ["a", "æ", "eɪ", "ɑː"],
    # b
    "c": ["k", "s"],
    # d
    "e": ["ɪ", "e", "iː", "ɜː"],
    # f
    "g": ["ɡ", "dʒ"],
    # h
    "i": ["ɪ", "aɪ", "iː"],
    # j, k, l, m
    "n": ["n", "ŋ"],
    "o": ["ɒ", "ɑː", "əʊ", "ɔː"],
    # p, q, r, s, t
    "u": ["ʌ", "ʊ", "uː"],  # "juː", "jʊ"
    # v, w, x
    "y": ["j", "ɪ", "i", "aɪ"],
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


print_transform_dict()
