import pytest

from .translate import english_gana, english_gana_mark


def test_english_gana_mark():
    txt = "/ˈpɜːrfɪkt/"
    s = english_gana_mark(txt)
    assert "".join(s) == "përfikt"


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
