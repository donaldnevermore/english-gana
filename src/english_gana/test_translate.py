import pytest

from .tokenize import remove_pitch, remove_slash, tokenize_ipa
from .translate import (
    english_gana,
    english_gana_mark,
    tokenize_ipa,
    translate_ipa,
)


def test_english_gana_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = english_gana_mark(txt)
    assert "".join(s) == "përfikt"


def test_tokenize_ipa():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    assert "".join(s) == remove_pitch(remove_slash(txt))


def test_translate_ipa():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    x = translate_ipa(s)
    assert "".join(x) == "përfikt"


def test_english_gana():
    a = "perfect"
    b = "/ˈpɜːrfɪkt/"
    r = english_gana(a, b)
    assert r == "p[e]{ë}rf[e]{i}ct"


def test_apple():
    a = "apple"
    b = "/ˈæpl/"
    r = english_gana(a, b)
    assert r == "appl[e]{}"


def test_boy():
    a = "boy"
    b = "/bɔɪ/"
    r = english_gana(a, b)
    assert r == "boy"
