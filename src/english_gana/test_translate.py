import pytest

from .translate import english_gana, english_gana_mark


def test_english_gana_mark():
    a = "/ˈpɜːrfɪkt/"
    b = english_gana_mark(a)
    assert "".join(b) == "pérfikt"


def test_perfect():
    a = "perfect"
    b = "/ˈpɜːrfɪkt/"
    r = english_gana(a, b)
    assert r == "p[e|é]rf[e|i]ct"


def test_light():
    a = "light"
    b = "/laɪt/"
    r = english_gana(a, b)
    assert r == "l[i|ī][gh]t"


def test_car():
    a = "car"
    b = "/kɑːr/"
    r = english_gana(a, b)
    assert r == "car"


def test_ink():
    a = "ink"
    b = "/ɪŋk/"
    r = english_gana(a, b)
    assert r == "ink"


def test_juice():
    a = "juice"
    b = "/dʒuːs/"
    r = english_gana(a, b)
    assert r == "juic[e]"


def test_like():
    a = "like"
    b = "/laɪk/"
    r = english_gana(a, b)
    assert r == "l[i|ī]k[e]"


def test_rope():
    a = "rope"
    b = "/rəʊp/"
    r = english_gana(a, b)
    assert r == "r[o|ō]p[e]"


def test_sit():
    a = "sit"
    b = "/sɪt/"
    r = english_gana(a, b)
    assert r == "sit"


def test_take():
    a = "take"
    b = "/teɪk/"
    r = english_gana(a, b)
    assert r == "t[a|ā]k[e]"


def test_up():
    a = "up"
    b = "/ʌp/"
    r = english_gana(a, b)
    assert r == "[u|û]p"


def test_voice():
    a = "voice"
    b = "/vɔɪs/"
    r = english_gana(a, b)
    assert r == "voic[e]"


def test_water():
    a = "water"
    b = "/ˈwɔːtər/"
    r = english_gana(a, b)
    assert r == "w[a|o]t[e|é]r"


def test_yes():
    a = "yes"
    b = "/jes/"
    r = english_gana(a, b)
    assert r == "yes"


def test_zoo():
    a = "zoo"
    b = "/zuː/"
    r = english_gana(a, b)
    assert r == "zoo"


def test_cure():
    a = "cure"
    b = "/kjʊr/"
    r = english_gana(a, b)
    assert r == "c[u|yu]r[e]"


def test_thing():
    a = "thing"
    b = "/θɪŋ/"
    r = english_gana(a, b)
    assert r == "thing"


def test_eight():
    a = "eight"
    b = "/eɪt/"
    r = english_gana(a, b)
    assert r == "ei[gh]t"


def test_they():
    a = "they"
    b = "/ðeɪ/"
    r = english_gana(a, b)
    assert r == "[t|d]hey"


def test_judge():
    a = "judge"
    b = "/dʒʌdʒ/"
    r = english_gana(a, b)
    assert r == "j[u|û]dg[e]"


def test_sugar():
    a = "sugar"
    b = "/ˈʃʊɡər/"
    r = english_gana(a, b)
    assert r == "[s|sh]ug[a|á]r"


def test_vision():
    a = "vision"
    b = "/ˈvɪʒn/"
    r = english_gana(a, b)
    assert r == "vi[si|zh][o|ó]n"


def test_finally():
    a = "finally"
    b = "/ˈfaɪnəli/"
    r = english_gana(a, b)
    assert r == "f[i|ī]n[a|á]lly"


def test_measure():
    a = "measure"
    b = "/ˈmeʒər/"
    r = english_gana(a, b)
    assert r == "me[a][s|zh][u|ú]r[e]"


def test_phone():
    a = "phone"
    b = "/fəʊn/"
    r = english_gana(a, b)
    assert r == "ph[o|ō]n[e]"


def test_watch():
    a = "watch"
    b = "/wɑːtʃ/"
    r = english_gana(a, b)
    assert r == "watch"


def test_money():
    a = "money"
    b = "/ˈmʌni/"
    r = english_gana(a, b)
    assert r == "m[o|û]n[e]y"


def test_few():
    a = "few"
    b = "/fjuː/"
    r = english_gana(a, b)
    assert r == "f[ew|yü]"


def test_picture():
    a = "picture"
    b = "/ˈpɪktʃər/"
    r = english_gana(a, b)
    assert r == "pic[t|ch][u|ú]r[e]"


def test_mission():
    a = "mission"
    b = "/ˈmɪʃn/"
    r = english_gana(a, b)
    assert r == "mis[si|sh][o|ó]n"


def test_action():
    a = "action"
    b = "/ˈækʃn/"
    r = english_gana(a, b)
    assert r == "[a|â]c[ti|sh][o|ó]n"


def test_digestion():
    a = "digestion"
    b = "/daɪˈdʒestʃən/"
    r = english_gana(a, b)
    assert r == "d[i|ī]ˈ[g|j]es[ti|ch][o|ó]n"


def test_pencil():
    a = "pencil"
    b = "/ˈpensl/"
    r = english_gana(a, b)
    assert r == "penc[i|í]l"


def test_chef():
    a = "chef"
    b = "/ʃef/"
    r = english_gana(a, b)
    assert r == "[c|s]hef"


def test_cetacean():
    a = "cetacean"
    b = "/sɪˈteɪʃn/"
    r = english_gana(a, b)
    assert r == "c[e|i]ˈt[a|ā][ce|sh][a|á]n"


def test_social():
    a = "social"
    b = "/ˈsəʊʃl/"
    r = english_gana(a, b)
    assert r == "s[o|ō][ci|sh][a|á]l"


def test_obvious():
    a = "obvious"
    b = "/ˈɑːbviəs/"
    r = english_gana(a, b)
    assert r == "[o|ô]bv[i|ï][o][u|ú]s"


def test_though():
    a = "though"
    b = "/ðəʊ/"
    r = english_gana(a, b)
    assert r == "[t|d]h[o|ō][ugh]"


def test_tough():
    a = "tough"
    b = "/tʌf/"
    r = english_gana(a, b)
    assert r == "t[o][u|û][g|f][h]"


def test_cough():
    a = "cough"
    b = "/kɔːf/"
    r = english_gana(a, b)
    assert r == "co[u][g|f][h]"


def test_through():
    a = "through"
    b = "/θruː/"
    r = english_gana(a, b)
    assert r == "thr[o][u|ü][gh]"


def test_anxious():
    a = "anxious"
    b = "/ˈæŋkʃəs/"
    r = english_gana(a, b)
    assert r == "[a|â]n[xi|ksh][o][u|ú]s"


def test_anxiety():
    a = "anxiety"
    b = "/æŋˈzaɪəti/"
    r = english_gana(a, b)
    assert r == "[a|â][n|ng]ˈ[x|z][i|ī][e|é]ty"


def test_naughty():
    a = "naughty"
    b = "/ˈnɔːti/"
    r = english_gana(a, b)
    assert r == "nau[gh]ty"


def test_singer():
    a = "singer"
    b = "/ˈsɪŋər/"
    r = english_gana(a, b)
    assert r == "sing[e|é]r"


def test_finger():
    a = "finger"
    b = "/ˈfɪŋɡər/"
    r = english_gana(a, b)
    assert r == "fi[n|ng]g[e|é]r"


# starts with alphabet order


def test_apple():
    a = "apple"
    b = "/ˈæpl/"
    r = english_gana(a, b)
    assert r == "[a|â]ppl[e]"


def test_boy():
    a = "boy"
    b = "/bɔɪ/"
    r = english_gana(a, b)
    assert r == "boy"


def test_cat():
    a = "cat"
    b = "/kæt/"
    r = english_gana(a, b)
    assert r == "c[a|â]t"


def test_dog():
    a = "dog"
    b = "/dɔːɡ/"
    r = english_gana(a, b)
    assert r == "dog"


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
    assert r == "g[i|í]rl"


def test_house():
    a = "house"
    b = "/haʊs/"
    r = english_gana(a, b)
    assert r == "hous[e]"


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
    assert r == "k[i|ī]t[e]"


def test_lunch():
    a = "lunch"
    b = "/lʌntʃ/"
    r = english_gana(a, b)
    assert r == "l[u|û]nch"


def test_music():
    a = "music"
    b = "/ˈmjuːzɪk/"
    r = english_gana(a, b)
    assert r == "m[u|ū][s|z]ic"


def test_need():
    a = "need"
    b = "/niːd/"
    r = english_gana(a, b)
    assert r == "need"


def test_ox():
    a = "ox"
    b = "/ɑːks/"
    r = english_gana(a, b)
    assert r == "[o|ô]x"


def test_person():
    a = "person"
    b = "/ˈpɜːrsn/"
    r = english_gana(a, b)
    assert r == "p[e|é]rs[o|ó]n"


def test_quick():
    a = "quick"
    b = "/kwɪk/"
    r = english_gana(a, b)
    assert r == "quick"


def test_ruby():
    a = "ruby"
    b = "/ˈruːbi/"
    r = english_gana(a, b)
    assert r == "r[u|ü]by"


def test_ski():
    a = "ski"
    b = "/skiː/"
    r = english_gana(a, b)
    assert r == "sk[i|ï]"


def test_tooth():
    a = "tooth"
    b = "/tuːθ/"
    r = english_gana(a, b)
    assert r == "tooth"


def test_update():
    a = "update"
    b = "/ˌʌpˈdeɪt/"
    r = english_gana(a, b)
    assert r == "ˌ[u|û]pˈd[a|ā]t[e]"


def test_vowel():
    a = "vowel"
    b = "/ˈvaʊəl/"
    r = english_gana(a, b)
    assert r == "vow[e|é]l"


def test_weather():
    a = "weather"
    b = "/ˈweðər/"
    r = english_gana(a, b)
    assert r == "we[a][t|d]h[e|é]r"


def test_xenon():
    a = "xenon"
    b = "/ˈzenɑːn/"
    r = english_gana(a, b)
    assert r == "[x|z]en[o|ô]n"


def test_yard():
    a = "yard"
    b = "/jɑːrd/"
    r = english_gana(a, b)
    assert r == "yard"


def test_zero():
    a = "zero"
    b = "/ˈzɪrəʊ/"
    r = english_gana(a, b)
    assert r == "z[e|i]r[o|ō]"
