import pytest

from english_gana.tokenize import remove_slash_pitch, tokenize_ipa


def test_perfect():
    a = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(a)
    assert "".join(s) == remove_slash_pitch(a)


def test_boy():
    a = "/bɔɪ/"
    s = tokenize_ipa(a)
    assert "".join(s) == remove_slash_pitch(a)


def test_egg():
    a = "/eɡ/"
    s = tokenize_ipa(a)
    assert "".join(s) == remove_slash_pitch(a)


def test_house():
    a = "/haʊs/"
    s = tokenize_ipa(a)
    assert "".join(s) == remove_slash_pitch(a)
