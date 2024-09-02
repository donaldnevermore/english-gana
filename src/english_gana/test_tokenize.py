import pytest

from .tokenize import remove_slash_pitch, tokenize_ipa


def test_perfect():
    a = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(a)
    assert s == ["p", "ɜː"] + list("rfɪkt")


def test_boy():
    a = "/bɔɪ/"
    s = tokenize_ipa(a)
    assert s == ["b", "ɔɪ"]


def test_egg():
    a = "/eɡ/"
    s = tokenize_ipa(a)
    assert "".join(s) == remove_slash_pitch(a)


def test_house():
    a = "/haʊs/"
    s = tokenize_ipa(a)
    assert s == ["h", "aʊ", "s"]
