import pytest

from english_gana.translate import english_gana, english_gana_mark


def test_english_gana_mark():
    a = "/ˈpɜːrfɪkt/"
    b = english_gana_mark(a)
    assert "".join(b) == "përfikt"


def test_english_gana():
    a = "perfect"
    b = "/ˈpɜːrfɪkt/"
    r = english_gana(a, b)
    assert r == "p[e]{ë}rf[e]{i}ct"


def test_apple():
    a = "apple"
    b = "/ˈæpl/"
    r = english_gana(a, b)
    assert r == "[a]{â}ppl[e]{}"


def test_boy():
    a = "boy"
    b = "/bɔɪ/"
    r = english_gana(a, b)
    assert r == "boy"


def test_car():
    a = "car"
    b = "/kɑːr/"
    r = english_gana(a, b)
    assert r == "c[a]{ä}r"


def test_egg():
    a = "egg"
    b = "/eɡ/"
    r = english_gana(a, b)
    assert r == "egg"


def test_fish():
    a = "fish"
    b = "/fɪʃ/"
    r = english_gana(a, b)
    assert r == "fish"


def test_girl():
    a = "girl"
    b = "/ɡɜːrl/"
    r = english_gana(a, b)
    assert r == "g[i]{ë}rl"


def test_house():
    a = "house"
    b = "/haʊs/"
    r = english_gana(a, b)
    assert r == "hous[e]{}"
