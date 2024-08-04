from .easy_mark import translate_to_easy_mark
from .tokenize import tokenize_ipa


def test_easy_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    i = translate_to_easy_mark(s)
    assert "".join(i) == "p_irfikt"
