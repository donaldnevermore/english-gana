from english_gana.tokenize import tokenize_ipa
from english_gana.translate_ipa import translate_ipa

letter_to_english_gana = {
    "a": ["â", "ā", "ä", "e", "ö"],
    "c": ["k", "s"],
    "e": ["i", "ï", "ë"],
    "g": ["j"],
    "i": ["ī", "ï", "ë"],
    "n": ["ng"],
    "o": ["ä", "ō", "ö", "ü", "u", "û", "i", "oi", "au"],
    "s": ["z", "sh"],
    "u": ["û", "ū", "ü", "ë", "e"],
    "x": ["k"],
    "y": ["i", "ī"],
}

vowel_to_schwa = {
    "a": "á",
    "e": "é",
    "i": "í",
    "o": "ó",
    "u": "ú",
}


def english_gana_mark(ipa: str) -> list[str]:
    s = tokenize_ipa(ipa)
    return translate_ipa(s)


class EnglishGana:
    word: str = ""
    sound: list[str] = []
    result: list[str] = []
    omit: int | None = None
    i: int = 0
    j: int = 0

    def __init__(self, word: str, ipa: str) -> None:
        self.word = word
        self.sound = english_gana_mark(ipa)

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
        # Is the consonant letter after the same as the current letter?
        return (
            self.i + 1 < len(self.word)
            and self.wordi() not in vowel_to_schwa
            and self.wordi() == self.word[self.i + 1]
        )

    def handle_omit(self) -> None:
        if self.omit is None:
            return

        self.result.append(f"[{self.word[self.omit : self.i]}]{{}}")
        self.omit = None

    def wordi(self) -> str:
        if self.i >= len(self.word):
            raise IndexError()

        return self.word[self.i]

    def soundj(self) -> str:
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

    def match(self, a: str, b: str) -> bool:
        """Is a and b match word[i] and sound[j]?

        Args:
            a (str): _description_
            b (str): _description_

        Returns:
            bool: _description_
        """
        if self.wordi() == a and self.soundj() == b:
            return True
        else:
            return False

    def should_eat_two(self) -> bool:
        if self.match("e", "ï") and self.next_is("e"):
            return True
        if self.match("o", "oi") and self.next_in(["i", "y"]):
            return True
        if self.match("o", "au") and self.next_in(["u", "w"]):
            return True
        if self.match("s", "sh") and self.next_is("h"):
            return True

        return False

    def should_eat_one(self) -> bool:
        if self.match("c", "k"):
            return True
        if self.match("o", "ä"):
            return True

        return False

    def parse(self) -> None:
        self.result = []
        self.omit = None
        self.i = 0
        self.j = 0

        while True:
            if self.i >= len(self.word):
                break
            if self.j >= len(self.sound):
                self.result.append(f"[{self.word[self.i :]}]{{}}")
                break

            if self.wordi() == self.soundj():
                self.handle_omit()
                if self.is_same_consonant_after():
                    self.eat_two_letters()
                else:
                    self.eat_a_letter()
            elif self.wordi() in vowel_to_schwa and self.soundj() == "é":
                self.handle_omit()
                self.eat_a_schwa()
            elif (
                self.wordi() in letter_to_english_gana
                and self.soundj() in letter_to_english_gana[self.wordi()]
            ):
                self.handle_omit()
                if (
                    self.match("x", "k")
                    and self.j + 1 < len(self.sound)
                    and self.sound[self.j + 1] == "s"
                ):
                    self.eat_a_letter()
                    self.j += 1
                elif self.should_eat_one():
                    self.eat_a_letter()
                elif self.should_eat_two():
                    self.eat_two_letters()
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

    if len(eg.result) == 0:
        raise Exception(f"The word `{word}` is not match with the IPA {ipa}.")

    return "".join(eg.result)
