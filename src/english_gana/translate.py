from .tokenize import tokenize_ipa
from .translate_ipa import translate_ipa

letter_to_english_gana = {
    "a": ["a", "ă", "ā", "e", "o", "ŭ", "n", "l", "é"],
    "b": ["b"],
    "c": ["k", "s", "ch", "sh"],
    "d": ["d", "t", "j"],
    "e": ["e", "i", "ï", "ā", "y", "ü", "n", "l", "é"],
    "f": ["f", "v"],
    "g": ["g", "j", "f"],
    "h": ["h"],
    "i": ["i", "ī", "ï", "y", "n", "l", "é"],
    "j": ["j"],
    "k": ["k"],
    "l": ["l"],
    "m": ["m"],
    "n": ["n", "ng"],
    "o": ["o", "a", "ō", "ŏ", "ü", "u", "ŭ", "i", "oi", "äu", "n", "l", "é"],
    "p": ["p", "f"],
    "q": ["k"],
    "r": ["r"],
    "s": ["s", "z", "sh", "zh"],
    "t": ["t", "th", "dh", "ch", "sh"],
    "u": ["u", "ŭ", "ü", "e", "y", "i", "n", "l", "é"],
    "v": ["v"],
    "w": ["w"],
    "x": ["k", "z"],
    "y": ["y", "ï", "ī"],
    "z": ["z"],
}

vowels = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú",
}


vowel_symbols = [
    "a",
    "ă",
    "ā",
    "äu",
    "e",
    "é",
    # ē
    "i",
    "ī",
    "ï",
    "o",
    "ō",
    "ŏ",
    "oi",
    "u",
    "ŭ",
    # ū
    "ü",
]

english_gana_to_respelling = {
    "ï": "ee",
    "ü": "oo",
    "u": "uu",
    "o": "aw",
    "ŏ": "o",
    "ă": "a",
    "ŭ": "u",
    "a": "ah",
    "ā": "ay",
    "oi": "oy",
    "ī": "igh",
    "ō": "oh",
    "äu": "ow",
    "á": "uh",
    "é": "uh",
    "í": "uh",
    "ó": "uh",
    "ú": "uh",
}


def english_gana_mark(ipa: str) -> list[str]:
    s = tokenize_ipa(ipa)
    return translate_ipa(s)


class EnglishGana:
    # the sound symbols of English Gana
    sound: list[str] = []
    # for silent letters
    omit: int | None = None
    word: str = ""
    result: list[str] = []
    i: int = 0
    j: int = 0
    unresolved_j: int | None = None
    is_respelling: bool = False

    def __init__(self, word: str, ipa: str, is_respelling: bool = False) -> None:
        self.word = word
        self.is_respelling = is_respelling
        self.sound = english_gana_mark(ipa)

    def sound_repr(self, gana: str) -> str:
        if self.is_respelling and gana in english_gana_to_respelling:
            return english_gana_to_respelling[gana]
        else:
            return gana

    def eat_a_ruby(self) -> None:
        s = self.sound_repr(self.soundj())
        if s == self.wordi():
            self.result.append(self.wordi())
        else:
            self.result.append(f"[{self.wordi()}|{s}]")

        self.i += 1
        self.j += 1

    def eat_a_letter(self) -> None:
        self.result.append(self.wordi())
        self.i += 1
        self.j += 1

    def eat_two_letters(self) -> None:
        self.result.append(self.word[self.i : self.i + 2])
        self.i += 2
        self.j += 1

    def same_next_consonant(self) -> bool:
        # Is the consonant letter that comes next the same as the current letter?
        letter = self.wordi()
        return letter not in vowels and self.next_is(letter)

    def handle_omit(self) -> None:
        """Handle silent letters in the middle of the word."""
        if self.omit is None:
            return

        self.result.append(f"[{self.word[self.omit : self.i]}]")
        self.omit = None

    def wordi(self) -> str:
        # the current letter
        if self.i >= len(self.word):
            raise IndexError()

        return self.word[self.i]

    def soundj(self) -> str:
        # the current sound symbol
        if self.j >= len(self.sound):
            raise IndexError()

        return self.sound[self.j]

    def next_is(self, letter: str) -> bool:
        if self.i + 1 < len(self.word) and self.word[self.i + 1] == letter:
            return True
        else:
            return False

    def next_in(self, symbols: list[str]) -> bool:
        if self.i + 1 < len(self.word) and self.word[self.i + 1] in symbols:
            return True
        else:
            return False

    def next_sound_is(self, letter: str) -> bool:
        if self.j + 1 < len(self.sound) and self.sound[self.j + 1] == letter:
            return True
        else:
            return False

    def next_sound_in(self, symbols: list[str]) -> bool:
        if self.j + 1 < len(self.sound) and self.sound[self.j + 1] in symbols:
            return True
        else:
            return False

    def match_is(self, l: str, r: str) -> bool:
        """Is l and r match word[i] and sound[j]?

        Args:
            l (str): _description_
            r (str): _description_

        Returns:
            bool: _description_
        """
        if self.wordi() == l and self.soundj() == r:
            return True
        else:
            return False

    def match_in(self, l: str, r: list[str]) -> bool:
        if self.wordi() == l and self.soundj() in r:
            return True
        else:
            return False

    def should_eat_two(self) -> bool:
        if self.match_is("a", "ā") and self.next_in(["i", "y"]):
            return True
        if self.match_is("a", "o") and self.next_in(["w", "u"]):
            return True
        if self.match_is("e", "ï") and self.next_in(["e", "a"]):
            return True
        if self.match_is("e", "ā") and self.next_in(["i", "y"]):
            return True
        if self.match_is("o", "ü") and self.next_is("o"):
            return True
        if (
            self.match_is("o", "ō")
            and self.next_in(["a", "e"])
            and not self.next_sound_in(vowel_symbols)
        ):
            return True
        if self.match_is("o", "oi") and self.next_in(["i", "y"]):
            return True
        if self.match_is("o", "äu") and self.next_in(["u", "w"]):
            return True
        if (
            self.match_is("u", "ü")
            and self.next_in(["i", "e"])
            and not self.next_sound_in(vowel_symbols)
        ):
            return True
        if self.match_is("d", "j") and self.next_is("g"):
            return True
        if self.match_is("t", "th") and self.next_is("h"):
            return True
        if self.match_is("s", "sh") and self.next_is("h"):
            return True
        if self.match_is("c", "ch") and self.next_is("h"):
            return True
        if self.match_is("p", "f") and self.next_is("h"):
            return True
        if self.match_is("c", "k") and self.next_is("k"):
            return True
        if (
            self.match_is("n", "ng")
            and self.next_in(["k", "g"])
            and not self.next_sound_is("g")
        ):
            return True

        return False

    def should_eat_one(self) -> bool:
        if self.match_is("c", "k"):
            return True
        if self.match_is("c", "s") and self.next_in(["i", "e", "y"]):
            return True
        if self.match_is("n", "ng") and self.next_is("x") and self.next_sound_is("k"):
            return True
        if self.match_is("y", "ï"):
            return True

        return False

    def handle_in_table(self) -> None:
        if self.same_next_consonant():
            self.result.append(self.wordi())
            self.i += 1
            return

        # greedy algorithm: eat the longest letters first
        if (
            self.match_is("o", "é")
            and self.word[self.i + 1 : self.i + 3] == "us"
            and self.next_sound_is("s")
        ):
            s = self.sound_repr("ú")
            self.result.append(f"[o][u|{s}]s")
            self.i += 3
            self.j += 2
        elif self.match_is("t", "ch") and self.word[self.i + 1 : self.i + 3] == "ch":
            self.result.append("tch")
            self.i += 3
            self.j += 1
        elif self.match_is("q", "k") and self.next_is("u") and self.next_sound_is("w"):
            self.result.append("qu")
            self.i += 2
            self.j += 2
        elif (
            self.match_is("e", "y") and self.next_in(["w"]) and self.next_sound_is("ü")
        ):
            s = self.sound_repr("ü")
            self.result.append(f"[ew|y{s}]")
            self.i += 2
            self.j += 2
        elif self.match_is("x", "k") and self.next_is("i") and self.next_sound_is("sh"):
            self.result.append("[xi|ksh]")
            self.i += 2
            self.j += 2
        elif (
            self.wordi() in vowels
            and self.soundj() in ["n", "l"]
            and self.next_in(["n", "l"])
        ):
            schwa = vowels[self.wordi()]
            s = self.sound_repr(schwa)
            self.result.append(f"[{self.wordi()}|{s}]{self.word[self.i+1]}")
            self.i += 2
            self.j += 1
        elif self.match_in("o", ["ŭ", "ü", "u"]) and self.next_is("u"):
            s = self.sound_repr(self.soundj())
            self.result.append(f"[o][u|{s}]")
            self.i += 2
            self.j += 1
        elif self.match_in("s", ["sh", "zh"]) and self.next_is("i"):
            s = self.sound_repr(self.soundj())
            self.result.append(f"[si|{s}]")
            self.i += 2
            self.j += 1
        elif self.match_in("t", ["sh", "ch"]) and self.next_is("i"):
            s = self.sound_repr(self.soundj())
            self.result.append(f"[ti|{s}]")
            self.i += 2
            self.j += 1
        elif self.match_is("t", "dh") and self.next_is("h"):
            self.result.append("[t|d]h")
            self.i += 2
            self.j += 1
        elif self.match_is("c", "sh") and self.next_is("h"):
            self.result.append("[c|s]h")
            self.i += 2
            self.j += 1
        elif self.match_is("c", "sh") and self.next_in(["i", "e"]):
            letters = self.word[self.i : self.i + 2]
            self.result.append(f"[{letters}|sh]")
            self.i += 2
            self.j += 1
        elif self.match_is("e", "ï") and self.next_is("y"):
            self.result.append("[e]y")
            self.i += 2
            self.j += 1
        elif self.should_eat_two():
            self.eat_two_letters()
        elif self.match_is("x", "k") and self.next_sound_is("s"):
            self.result.append("x")
            self.i += 1
            self.j += 2
        elif self.match_is("u", "y") and self.next_sound_is("ü"):
            s = self.sound_repr("ū")
            self.result.append(f"[u|{s}]")
            self.i += 1
            self.j += 2
        elif self.match_is("u", "y") and self.next_sound_is("u"):
            s = self.sound_repr("u")
            self.result.append(f"[u|y{s}]")
            self.i += 1
            self.j += 2
        elif self.match_is("e", "ï"):
            s = self.sound_repr("ē")
            self.result.append(f"[e|{s}]")
            self.i += 1
            self.j += 1
        elif self.match_is("o", "a"):
            s = self.sound_repr("ŏ")
            self.result.append(f"[o|{s}]")
            self.i += 1
            self.j += 1
        elif self.wordi() in vowels and self.soundj() == "é":
            schwa = vowels[self.wordi()]
            s = self.sound_repr(schwa)
            self.result.append(f"[{self.wordi()}|{s}]")
            self.i += 1
            self.j += 1
        elif self.should_eat_one():
            self.eat_a_letter()
        else:
            self.eat_a_ruby()

    def parse(self) -> None:
        self.result = []
        self.omit = None
        self.i = 0
        self.j = 0

        while True:
            if self.i >= len(self.word):
                if self.j < len(self.sound):
                    self.unresolved_j = self.j
                break
            if self.j >= len(self.sound):
                remain_letters = self.word[self.i :]
                if len(remain_letters) > 0:
                    self.result.append(f"[{remain_letters}]")
                break

            if self.soundj() in ["ˌ", "ˈ"]:
                self.result.append(self.soundj())
                self.j += 1
            elif (
                self.wordi() in letter_to_english_gana
                and self.soundj() in letter_to_english_gana[self.wordi()]
            ):
                self.handle_omit()
                self.handle_in_table()
            else:
                # not match
                if self.omit is None:
                    self.omit = self.i
                self.i += 1


def english_gana(word: str, ipa: str) -> str:
    """translate to English Gana

    Args:
        word (str): _description_
        ipa (str): _description_

    Returns:
        str: _description_
    """
    eg = EnglishGana(word, ipa)
    eg.parse()

    if eg.unresolved_j is not None:
        print(f"`{word}` doesn't match with {eg.sound} at index {eg.unresolved_j}.")

    return "".join(eg.result)
