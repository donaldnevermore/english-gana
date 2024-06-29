import pytest

from .translate import tokenize_ipa, translate_ipa, translate_to_easy_ipa


def test_translate():
    s = tokenize_ipa("/ˈpɜːrfɪkt/")
    print(s)
    a = translate_ipa(s)
    print(a)
    i = translate_to_easy_ipa(s)
    print(i)

    assert False
