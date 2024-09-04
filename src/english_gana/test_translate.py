import pytest

from .translate import english_gana, english_gana_mark


def test_english_gana_mark():
    a = "/ˈpɜːrfɪkt/"
    b = english_gana_mark(a)
    assert "".join(b) == "përfikt"


def test_perfect():
    a = "perfect"
    b = "/ˈpɜːrfɪkt/"
    r = english_gana(a, b)
    assert r == "p[e]{ë}rf[e]{i}ct"


def test_light():
    a = "light"
    b = "/laɪt/"
    r = english_gana(a, b)
    assert r == "l[i]{ī}[gh]{}t"


def test_car():
    a = "car"
    b = "/kɑːr/"
    r = english_gana(a, b)
    assert r == "c[a]{ä}r"


def test_ink():
    a = "ink"
    b = "/ɪŋk/"
    r = english_gana(a, b)
    assert r == "i[n]{ng}k"


def test_juice():
    a = "juice"
    b = "/dʒuːs/"
    r = english_gana(a, b)
    assert r == "j[u]{ü}[i]{}[c]{s}[e]{}"


def test_like():
    a = "like"
    b = "/laɪk/"
    r = english_gana(a, b)
    assert r == "l[i]{ī}k[e]{}"


def test_rope():
    a = "rope"
    b = "/rəʊp/"
    r = english_gana(a, b)
    assert r == "r[o]{ō}p[e]{}"


def test_sit():
    a = "sit"
    b = "/sɪt/"
    r = english_gana(a, b)
    assert r == "sit"


def test_take():
    a = "take"
    b = "/teɪk/"
    r = english_gana(a, b)
    assert r == "t[a]{ā}k[e]{}"


def test_up():
    a = "up"
    b = "/ʌp/"
    r = english_gana(a, b)
    assert r == "[u]{û}p"


def test_voice():
    a = "voice"
    b = "/vɔɪs/"
    r = english_gana(a, b)
    assert r == "voi[c]{s}[e]{}"


def test_water():
    a = "water"
    b = "/ˈwɔːtər/"
    r = english_gana(a, b)
    assert r == "w[a]{ö}t[e]{é}r"


def test_yes():
    a = "yes"
    b = "/jes/"
    r = english_gana(a, b)
    assert r == "yes"


def test_zoo():
    a = "zoo"
    b = "/zuː/"
    r = english_gana(a, b)
    assert r == "z[oo]{ü}"


def test_cure():
    a = "cure"
    b = "/kjʊr/"
    r = english_gana(a, b)
    assert r == "c[u]{yu}r[e]{}"


def test_thing():
    a = "thing"
    b = "/θɪŋ/"
    r = english_gana(a, b)
    assert r == "thing"


def test_eight():
    a = "eight"
    b = "/eɪt/"
    r = english_gana(a, b)
    assert r == "ei[gh]{}t"


def test_they():
    a = "they"
    b = "/ðeɪ/"
    r = english_gana(a, b)
    assert r == "[t]{d}hey"


def test_judge():
    a = "judge"
    b = "/dʒʌdʒ/"
    r = english_gana(a, b)
    assert r == "j[u]{û}[dg]{j}[e]{}"


def test_sugar():
    a = "sugar"
    b = "/ˈʃʊɡər/"
    r = english_gana(a, b)
    assert r == "[s]{sh}ug[a]{á}r"


def test_vision():
    a = "vision"
    b = "/ˈvɪʒn/"
    r = english_gana(a, b)
    assert r == "vi[si]{zh}[o]{ó}n"


def test_finally():
    a = "finally"
    b = "/ˈfaɪnəli/"
    r = english_gana(a, b)
    assert r == "f[i]{ī}n[a]{á}lly"


def test_measure():
    a = "measure"
    b = "/ˈmeʒər/"
    r = english_gana(a, b)
    assert r == "me[a]{}[s]{zh}[u]{ú}r[e]{}"


def test_phone():
    a = "phone"
    b = "/fəʊn/"
    r = english_gana(a, b)
    assert r == "[ph]{f}[o]{ō}n[e]{}"


def test_tough():
    a = "tough"
    b = "/tʌf/"
    r = english_gana(a, b)
    assert r == "t[o]{}[u]{û}[gh]{f}"


# starts with alphabet order


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


def test_cat():
    a = "cat"
    b = "/kæt/"
    r = english_gana(a, b)
    assert r == "c[a]{â}t"


def test_dog():
    a = "dog"
    b = "/dɔːɡ/"
    r = english_gana(a, b)
    assert r == "d[o]{ö}g"


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


def test_input():
    a = "input"
    b = "/ˈɪnpʊt/"
    r = english_gana(a, b)
    assert r == "input"


def test_join():
    a = "join"
    b = "/dʒɔɪn/"
    r = english_gana(a, b)
    assert r == "join"


def test_kite():
    a = "kite"
    b = "/kaɪt/"
    r = english_gana(a, b)
    assert r == "k[i]{ī}t[e]{}"


def test_lunch():
    a = "lunch"
    b = "/lʌntʃ/"
    r = english_gana(a, b)
    assert r == "l[u]{û}nch"


def test_music():
    a = "music"
    b = "/ˈmjuːzɪk/"
    r = english_gana(a, b)
    assert r == "m[u]{ū}[s]{z}ic"


def test_need():
    a = "need"
    b = "/niːd/"
    r = english_gana(a, b)
    assert r == "n[e]{ē}[e]{}d"


def test_ox():
    a = "ox"
    b = "/ɑːks/"
    r = english_gana(a, b)
    assert r == "ox"


def test_person():
    a = "person"
    b = "/ˈpɜːrsn/"
    r = english_gana(a, b)
    assert r == "p[e]{ë}rs[o]{ó}n"


def test_quick():
    a = "quick"
    b = "/kwɪk/"
    r = english_gana(a, b)
    assert r == "quick"


def test_ruby():
    a = "ruby"
    b = "/ˈruːbi/"
    r = english_gana(a, b)
    assert r == "r[u]{ü}by"


def test_ski():
    a = "ski"
    b = "/skiː/"
    r = english_gana(a, b)
    assert r == "sk[i]{ï}"


def test_tooth():
    a = "tooth"
    b = "/tuːθ/"
    r = english_gana(a, b)
    assert r == "t[oo]{ü}th"


def test_update():
    a = "update"
    b = "/ˌʌpˈdeɪt/"
    r = english_gana(a, b)
    assert r == "[u]{û}pd[a]{ā}t[e]{}"


def test_vowel():
    a = "vowel"
    b = "/ˈvaʊəl/"
    r = english_gana(a, b)
    assert r == "vow[e]{é}l"


def test_weather():
    a = "weather"
    b = "/ˈweðər/"
    r = english_gana(a, b)
    assert r == "we[a]{}[t]{d}h[e]{é}r"


def test_xenon():
    a = "xenon"
    b = "/ˈzenɑːn/"
    r = english_gana(a, b)
    assert r == "[x]{z}enon"


def test_yard():
    a = "yard"
    b = "/jɑːrd/"
    r = english_gana(a, b)
    assert r == "y[a]{ä}rd"


def test_zero():
    a = "zero"
    b = "/ˈzɪrəʊ/"
    r = english_gana(a, b)
    assert r == "z[e]{i}r[o]{ō}"
