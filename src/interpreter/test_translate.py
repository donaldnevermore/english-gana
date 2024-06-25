import pytest

from .translate import tokenize_ipa, translate_ipa


def test_translate():
    s = tokenize_ipa("/ˈpɜːrfɪkt/")
    print(s)
    a = translate_ipa(s)
    print(a)

    assert False
