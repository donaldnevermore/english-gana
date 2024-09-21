from .tokenize import tokenize_ipa
from .translate_ipa import translate_ipa

letter_to_english_gana = {
    "a": ["â", "ā", "ä", "e", "ö", "û", "n", "l", "ó"],
    "c": ["k", "s", "ch", "sh"],
    "d": ["t", "j"],
    "e": ["i", "ï", "ë", "ā", "y", "ü", "n", "l", "ó"],
    "f": ["v"],
    "g": ["j", "f"],
    "i": ["ī", "ï", "ë", "y", "n", "l", "ó"],
    "n": ["ng"],
    "o": ["ä", "ō", "ö", "ü", "u", "û", "ë", "i", "oi", "au", "n", "l", "ó"],
    "p": ["f"],
    "q": ["k"],
    "s": ["z", "sh", "zh"],
    "t": ["th", "dh", "ch", "sh"],
    "u": ["û", "ü", "ë", "e", "y", "i", "n", "l", "ó"],
    "x": ["k", "z"],
    "y": ["i", "ī"],
}

vowels = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú",
}


vowel_symbols = [
    # a
    "â",
    "ā",
    "ä",
    "au",
    "e",
    # ē
    "ë",
    "i",
    "ī",
    "ï",
    "o",
    "ō",
    "ö",
    "ó",
    "oi",
    "u",
    "û",
    # ū
    "ü",
]


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

    def __init__(self, word: str, ipa: str) -> None:
        self.word = word
        self.sound = english_gana_mark(ipa)

    def eat_a_ruby(self) -> None:
        self.result.append(f"[{self.wordi()}|{self.soundj()}]")
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
        if self.match_is("o", "ü") and self.next_is("o"):
            return True
        if self.match_is("e", "ï") and self.next_is("e"):
            return True
        if self.match_is("a", "ö") and self.next_in(["w", "u"]):
            return True
        if self.match_is("d", "j") and self.next_is("g"):
            return True
        if self.match_is("t", "th") and self.next_is("h"):
            return True
        if self.match_is("o", "oi") and self.next_in(["i", "y"]):
            return True
        if self.match_is("e", "ā") and self.next_in(["i", "y"]):
            return True
        if self.match_is("o", "au") and self.next_in(["u", "w"]):
            return True
        if self.match_is("s", "sh") and self.next_is("h"):
            return True
        if self.match_is("c", "ch") and self.next_is("h"):
            return True
        if self.match_is("c", "k") and self.next_is("k"):
            return True
        if (
            self.match_is("n", "ng")
            and self.next_is("g")
            and not self.next_sound_is("g")
        ):
            return True

        return False

    def should_eat_one(self) -> bool:
        if self.match_is("c", "k"):
            return True
        if self.match_is("c", "s") and self.next_in(["i", "e", "y"]):
            return True
        if self.match_is("n", "ng"):
            return True
        if self.match_is("o", "ä"):
            return True
        if self.match_is("y", "i"):
            return True
        if self.match_is("x", "z"):
            return True

        return False

    def handle_in_table(self) -> None:
        if self.same_next_consonant():
            self.result.append(self.wordi())
            self.i += 1
            return

        # greedy algorithm: eat the longest letters first
        if (
            self.match_is("o", "ó")
            and self.word[self.i + 1 : self.i + 3] == "us"
            and self.next_sound_is("s")
        ):
            self.result.append("[o][u|ú]s")
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
            self.match_is("e", "y")
            and self.next_in(["w", "u"])
            and self.next_sound_is("ü")
        ):
            self.result.append(self.word[self.i : self.i + 2])
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
            self.result.append(f"[{self.wordi()}|{schwa}]{self.word[self.i+1]}")
            self.i += 2
            self.j += 1
        elif self.match_in("o", ["û", "ü", "u"]) and self.next_is("u"):
            self.result.append(f"[o][u|{self.soundj()}]")
            self.i += 2
            self.j += 1
        elif self.match_in("s", ["sh", "zh"]) and self.next_is("i"):
            self.result.append(f"[si|{self.soundj()}]")
            self.i += 2
            self.j += 1
        elif self.match_in("t", ["sh", "ch"]) and self.next_is("i"):
            self.result.append(f"[ti|{self.soundj()}]")
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
        elif self.match_is("e", "i") and self.next_is("y"):
            self.result.append("[e]y")
            self.i += 2
            self.j += 1
        elif self.should_eat_two():
            self.eat_two_letters()
        elif self.match_is("x", "k") and self.next_sound_is("s"):
            self.result.append("[x|ks]")
            self.i += 1
            self.j += 2
        elif self.match_is("u", "y") and self.next_sound_is("ü"):
            self.result.append("[u|ū]")
            self.i += 1
            self.j += 2
        elif self.match_is("u", "y") and self.next_sound_is("u"):
            self.result.append("[u|yu]")
            self.i += 1
            self.j += 2
        elif self.match_is("e", "ï"):
            self.result.append("[e|ē]")
            self.i += 1
            self.j += 1
        elif self.wordi() in vowels and self.soundj() == "ó":
            schwa = vowels[self.wordi()]
            self.result.append(f"[{self.wordi()}|{schwa}]")
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

            if self.wordi() == self.soundj():
                self.handle_omit()
                if self.same_next_consonant():
                    self.eat_two_letters()
                else:
                    self.eat_a_letter()
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
