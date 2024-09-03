from .tokenize import tokenize_ipa
from .translate_ipa import translate_ipa

letter_to_english_gana = {
    "a": ["â", "ā", "ä", "e", "ö"],
    "c": ["k", "s", "ch"],
    "e": ["i", "ï", "ë", "ā"],
    "g": ["j"],
    "i": ["ī", "ï", "ë", "y"],
    "n": ["ng"],
    "o": ["ä", "ō", "ö", "ü", "u", "û", "i", "oi", "au"],
    "q": ["k"],
    "s": ["z", "sh"],
    "t": ["th", "dh"],
    "u": ["û", "ü", "ë", "e", "y"],  # ū
    "x": ["k", "z"],
    "y": ["i", "ī"],
}

vowel_to_schwa = {
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
        symbols = english_gana_mark(ipa)

        # special cases like person, button, and final, etc.
        if (
            len(word) >= 2
            and word[-1] in ["n", "l"]
            and word[-2] in vowel_to_schwa
            and len(symbols) >= 2
            and symbols[-1] in ["n", "l"]
            and symbols[-2] not in vowel_symbols
        ):
            changed = symbols.copy()
            changed.insert(-1, "ó")
            self.sound = changed
        else:
            self.sound = symbols

    def eat_a_ruby(self) -> None:
        self.result.append(f"[{self.wordi()}]{{{self.soundj()}}}")
        self.i += 1
        self.j += 1

    def eat_a_letter(self) -> None:
        self.result.append(self.wordi())
        self.i += 1
        self.j += 1

    def eat_a_schwa(self) -> None:
        schwa = vowel_to_schwa[self.wordi()]
        self.result.append(f"[{self.wordi()}]{{{schwa}}}")
        self.i += 1
        self.j += 1

    def eat_two_letters(self) -> None:
        self.result.append(self.word[self.i : self.i + 2])
        self.i += 2
        self.j += 1

    def is_same_consonant_after(self) -> bool:
        # Is the consonant letter that comes after the same as the current letter?
        letter = self.wordi()
        return letter not in vowel_to_schwa and self.next_is(letter)

    def handle_omit(self) -> None:
        """Handle silent letters in the middle of the word."""
        if self.omit is None:
            return

        self.result.append(f"[{self.word[self.omit : self.i]}]{{}}")
        self.omit = None

    def wordi(self) -> str:
        """the current letter

        Raises:
            IndexError: _description_

        Returns:
            str: _description_
        """
        if self.i >= len(self.word):
            raise IndexError()

        return self.word[self.i]

    def soundj(self) -> str:
        """the current sound symbol

        Raises:
            IndexError: _description_

        Returns:
            str: _description_
        """
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
        if self.match_is("n", "ng") and self.next_is("g"):
            return True

        return False

    def is_vowel_combo(self) -> bool:
        if self.match_in("o", ["ü", "u"]) and self.next_is("o"):
            return True
        if self.match_is("e", "ü") and self.next_is("w"):
            return True
        if self.match_is("a", "ö") and self.next_in(["w", "u"]):
            return True

        return False

    def should_eat_one(self) -> bool:
        if self.match_is("c", "k"):
            return True
        if self.match_is("o", "ä"):
            return True

        return False

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
                    self.result.append(f"[{remain_letters}]{{}}")
                break

            if self.wordi() == self.soundj():
                self.handle_omit()
                if self.is_same_consonant_after():
                    self.eat_two_letters()
                else:
                    self.eat_a_letter()
            elif self.wordi() in vowel_to_schwa and self.soundj() == "ó":
                self.handle_omit()
                self.eat_a_schwa()
            elif (
                self.wordi() in letter_to_english_gana
                and self.soundj() in letter_to_english_gana[self.wordi()]
            ):
                self.handle_omit()

                # greedy algorithm: eat the longest letters first
                if (
                    self.match_is("q", "k")
                    and self.next_is("u")
                    and self.next_sound_is("w")
                ):
                    self.result.append("qu")
                    self.i += 2
                    self.j += 2
                elif self.is_vowel_combo():
                    letters = self.word[self.i : self.i + 2]
                    self.result.append(f"[{letters}]{{{self.soundj()}}}")
                    self.i += 2
                    self.j += 1
                elif self.should_eat_two():
                    self.eat_two_letters()
                elif self.match_is("t", "dh") and self.next_is("h"):
                    self.result.append("[t]{d}h")
                    self.i += 2
                    self.j += 1
                elif self.match_is("u", "y") and self.next_sound_is("ü"):
                    self.result.append("[u]{ū}")
                    self.i += 1
                    self.j += 2
                elif self.match_is("u", "y") and self.next_sound_is("u"):
                    self.result.append("[u]{yu}")
                    self.i += 1
                    self.j += 2
                elif self.match_is("x", "k") and self.next_sound_is("s"):
                    self.result.append("x")
                    self.i += 1
                    self.j += 2
                elif self.match_is("e", "ï"):
                    self.result.append("[e]{ē}")
                    self.i += 1
                    self.j += 1
                elif self.should_eat_one():
                    self.eat_a_letter()
                else:
                    self.eat_a_ruby()
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
        raise Exception(
            f"`{word}` is not match with {eg.sound} at index {eg.unresolved_j}."
        )

    return "".join(eg.result)
