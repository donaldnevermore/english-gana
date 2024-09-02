import pytest

from .tokenize import tokenize_ipa
from .translate_ipa import translate_ipa


def test_perfect():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "përfikt"


def test_apple():
    txt = "/ˈæpl/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "âpl"


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


def test_girl():
    txt = "/ɡɜːrl/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "gërl"


def test_house():
    txt = "/haʊs/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "haus"
