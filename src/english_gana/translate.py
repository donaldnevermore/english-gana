from english_gana.tokenize import tokenize_ipa
from english_gana.translate_ipa import translate_ipa

letter_to_english_gana = {
    "a": ["â", "ā", "ä"],
    "c": ["k", "s"],
    "e": ["i", "ï", "ë"],
    "g": ["j"],
    "i": ["ī", "ï"],
    "o": ["ä", "ō", "ö"],
    "u": ["û", "ū", "ü"],
    "y": ["i", "ī"],
}

vowels = ["a", "e", "i", "o", "u", "y"]
vowel_sounds = [
    "a",
    "â",
    "ā",
    "ä",
    "á",
    "e",
    "ë",
    "ē",
    "é",
    "i",
    "ī",
    "ï",
    "í",
    "o",
    "ō",
    "ö",
    "ó",
    "u",
    "û",
    "ū",
    "ü",
    "ú",
]


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

    def match_a_ruby(self) -> None:
        self.result.append(f"[{self.word[self.i]}]{{{self.sound[self.j]}}}")
        self.i += 1
        self.j += 1

    def match_a_letter(self) -> None:
        self.result.append(self.word[self.i])
        self.i += 1
        self.j += 1

    def match_two_letters(self) -> None:
        self.result.append(self.word[self.i : self.i + 2])
        self.i += 2
        self.j += 1

    def is_same_before(self) -> bool:
        # Is the letter before the same as the current letter?
        return self.i >= 1 and self.word[self.i] == self.word[self.i - 1]

    def handle_omit(self) -> None:
        if self.omit is None:
            return

        self.result.append(f"[{self.word[self.omit : self.i]}]{{}}")
        self.omit = None

    def word_i(self) -> str:
        return self.word[self.i]

    def sound_j(self) -> str:
        return self.sound[self.j]

    def parse(self) -> None:
        self.result = []
        self.omit = None
        self.i = 0
        self.j = 0

        while True:
            if self.i >= len(self.word):
                break
            if self.j >= len(self.sound):
                if self.is_same_before():
                    self.result.append(self.word[self.i :])
                else:
                    self.result.append(f"[{self.word[self.i :]}]{{}}")
                break

            if self.word_i() == self.sound_j():
                self.handle_omit()
                self.match_a_letter()
            elif (
                self.word_i() in letter_to_english_gana
                and self.sound_j() in letter_to_english_gana[self.word_i()]
            ):
                self.handle_omit()
                if self.word_i() == "c" and self.sound_j() == "k":
                    self.match_a_letter()
                else:
                    self.match_a_ruby()
            elif self.word_i() == "o":
                if (
                    self.sound_j() == "oi"
                    and self.i + 1 < len(self.word)
                    and self.word[self.i + 1] == "y"
                ):
                    self.match_two_letters()
                elif (
                    self.sound_j() == "au"
                    and self.i + 1 < len(self.word)
                    and self.word[self.i + 1] in ["u", "w"]
                ):
                    self.match_two_letters()
                else:
                    self.match_a_ruby()
            elif self.word_i() == "s":
                if (
                    self.sound_j() == "sh"
                    and self.i + 1 < len(self.word)
                    and self.word[self.i + 1] == "h"
                ):
                    self.match_two_letters()
                else:
                    self.match_a_ruby()
            elif self.is_same_before():
                self.result.append(self.word[self.i])
                self.i += 1
            elif self.word_i() in vowels and self.sound_j() in vowel_sounds:
                self.match_a_ruby()
            else:
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

    return "".join(eg.result)
