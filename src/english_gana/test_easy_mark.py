from .easy_mark import translate_to_easy_mark
from .tokenize import tokenize_ipa


def test_easy_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "piirfikt"

def test_apple():
    txt = "/ˈæpl/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "aapl"


def test_boy():
    txt = "/bɔɪ/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "boi"


def test_egg():
    txt = "/eɡ/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "eg"


def test_girl():
    txt = "/ɡɜːrl/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "giirl"


def test_house():
    txt = "/haʊs/"
    s = tokenize_ipa(txt)
    x = translate_to_easy_mark(s)
    assert "".join(x) == "haus"
