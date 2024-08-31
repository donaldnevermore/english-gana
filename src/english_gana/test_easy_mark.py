from english_gana.easy_mark import translate_to_easy_mark
from english_gana.tokenize import tokenize_ipa


def test_easy_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    i = translate_to_easy_mark(s)
    assert "".join(i) == "pe_rfikt"
