import pytest

from .tokenize import remove_slash_pitch, tokenize_ipa


def test_tokenize_perfect():
    txt = "/ˈpɜːrfɪkt/"
    s = tokenize_ipa(txt)
    assert "".join(s) == remove_slash_pitch(txt)


def test_tokenize_boy():
    b = "/bɔɪ/"
    s = tokenize_ipa(b)
    assert "".join(s) == remove_slash_pitch(b)


def test_tokenize_egg():
    b = "/eɡ/"
    s = tokenize_ipa(b)
    assert "".join(s) == remove_slash_pitch(b)
