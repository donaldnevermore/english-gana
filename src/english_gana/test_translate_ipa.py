import pytest

from english_gana.tokenize import tokenize_ipa
from english_gana.translate_ipa import translate_ipa


def test_perfect():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "përfikt"


def test_apple():
    txt = "/ˈæpl/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "apl"


def test_boy():
    txt = "/bɔɪ/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "boi"


def test_egg():
    txt = "/eɡ/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "eg"
