from .respelling import translate_to_respelling
from .tokenize import tokenize_ipa, remove_pitch


def test_easy_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    r = remove_pitch("".join(x))
    assert r == "puhrfikt"

def test_apple():
    txt = "/ˈæpl/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    r = remove_pitch("".join(x))
    assert r == "apl"


def test_boy():
    txt = "/bɔɪ/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    assert "".join(x) == "boy"


def test_egg():
    txt = "/eɡ/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    assert "".join(x) == "eg"


def test_girl():
    txt = "/ɡɜːrl/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    assert "".join(x) == "guhrl"


def test_house():
    txt = "/haʊs/"
    s = tokenize_ipa(txt)
    x = translate_to_respelling(s)
    assert "".join(x) == "hows"
