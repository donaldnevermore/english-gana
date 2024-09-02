import json

from pyquery import PyQuery as pq
from readmdict import MDX

data_folder = "E:/Monorepos/english-gana/src/data"


def query(s: str) -> None:
    builder = IndexBuilder()

    arr: list[str] = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            arr.append(s[i])
        else:
            word = "".join(arr)
            if word.isalpha():
                builder.lookup(word.lower())
            arr = []
        i += 1

    builder.dump_json()


class IndexBuilder:
    headwords: list = []
    dictionary: list = []
    mapping: dict[str, list[dict]] = {}

    def __init__(self) -> None:
        filename = f"{data_folder}/OALD_V14_8.mdx"
        mdxfile = MDX(filename, "utf-8")
        self.headwords = [*mdxfile]
        self.dictionary = [*mdxfile.items()]

        self.load_json()

    def lookup_many(self, queryWords: list[str]) -> None:
        for elem in queryWords:
            self.lookup(elem)

    def lookup(self, queryWord: str) -> None:
        wordIndex = self.headwords.index(queryWord.encode())
        _, val = self.dictionary[wordIndex]
        html = val.decode()
        self.find_in(html)

    def find_in(self, html: str):
        doc = pq(html)
        webtop_list = doc(
            "body > #entryContent > .entry > .top-container > .top-g > .webtop"
        )

        for elem in webtop_list.items():
            word_type = elem.find(".pos").text()
            if word_type == "verb":
                verb_table = elem.find(".collapse > .unbox > .body > .verb_forms_table")
                verb_forms = verb_table.find('tr[class="verb_form"]')
                for vf in verb_forms.items():
                    verb_form_contents = vf.find('td[class="verb_form"]').contents()
                    spelling = verb_form_contents[-1].strip()
                    phonetics_obj = vf.find(
                        ".verb_phons > .phonetics > .phons_n_am > .phon"
                    )
                    phonetics_list = [*phonetics_obj.items()]
                    sound = phonetics_list[0].text()
                    self.add_mapping(word_type, spelling, sound)
            else:
                headword_contents = elem.find(".headword").contents()
                headword = headword_contents[0]
                phonetics_obj = elem.find(".phonetics > .phons_n_am > .phon")
                phonetics_list = [*phonetics_obj.items()]
                sound = phonetics_list[0].text()
                self.add_mapping(word_type, headword, sound)

    def add_mapping(self, word_type: str, spelling: str, sound: str) -> None:
        if not word_type:
            word_type = "unknown"

        if spelling in self.mapping:
            arr = self.mapping[spelling]
            for elem in arr:
                if elem["sound"] == sound:
                    return

            arr.append(
                {
                    "type": word_type,
                    "sound": sound,
                }
            )
        else:
            self.mapping[spelling] = [
                {
                    "type": word_type,
                    "sound": sound,
                }
            ]

    def load_json(self):
        with open(f"{data_folder}/gana.json", "r", encoding="utf-8") as fp:
            self.mapping = json.load(fp)

    def dump_json(self):
        with open(f"{data_folder}/gana.json", "w", encoding="utf-8") as fp:
            json.dump(self.mapping, fp, ensure_ascii=False, indent=4)
