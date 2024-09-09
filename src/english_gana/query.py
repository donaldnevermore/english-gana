import json
from typing import Any

from pyquery import PyQuery
from readmdict import MDX

from .translate import english_gana

data_folder = "E:/Monorepos/english-gana/src/data"


def go() -> None:
    ganaData = GanaData()
    mapping: dict[str, list[dict[str, str]]] = {}
    for key, val in ganaData.mapping.items():
        arr: list[dict[str, str]] = []
        for elem in val:
            arr.append(
                {"type": elem["type"], "sound": english_gana(key, elem["sound"])}
            )
        mapping[key] = arr

    with open(f"{data_folder}/output.json", "w", encoding="utf-8") as fp:
        json.dump(mapping, fp, ensure_ascii=False, indent=4, sort_keys=True)


def run() -> None:
    s = ""
    with open(f"{data_folder}/input.md", "r", encoding="utf-8") as fp:
        s = fp.read()

    mapping: dict[str, list[dict[str, str]]] = {}
    with open(f"{data_folder}/output.json", "r", encoding="utf-8") as fp:
        mapping = json.load(fp)

    article: list[str] = []
    arr: list[str] = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            arr.append(s[i])
        else:
            word = "".join(arr)
            lower = word.lower()
            if lower in mapping:
                sound = mapping[lower][0]["sound"]
                article.append(sound)
            else:
                article.append(word)
            article.append(s[i])
            arr = []
        i += 1

    with open(f"{data_folder}/article.md", "w", encoding="utf-8") as fp:
        fp.write("".join(article))


def query() -> None:
    s = ""
    with open(f"{data_folder}/input.md", "r", encoding="utf-8") as fp:
        s = fp.read()

    ganaData = GanaData()
    builder = IndexBuilder(ganaData)

    arr: list[str] = []
    i = 0
    while i < len(s):
        if s[i].isalpha():
            arr.append(s[i])
        else:
            word = "".join(arr)
            builder.lookup(word.lower())
            arr = []
        i += 1

    ganaData.dump_json()


class GanaData:
    mapping: dict[str, list[dict[str, str]]] = {}

    def __init__(self) -> None:
        self.load_json()

    def load_json(self) -> None:
        with open(f"{data_folder}/gana.json", "r", encoding="utf-8") as fp:
            self.mapping = json.load(fp)

    def dump_json(self) -> None:
        with open(f"{data_folder}/gana.json", "w", encoding="utf-8") as fp:
            json.dump(self.mapping, fp, ensure_ascii=False, indent=4, sort_keys=True)

    def add_mapping(self, word_type: str, spelling: str, sound: str) -> None:
        if not word_type:
            word_type = "unknown"

        s = spelling.lower()
        if s in self.mapping:
            arr = self.mapping[s]
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
            self.mapping[s] = [
                {
                    "type": word_type,
                    "sound": sound,
                }
            ]


class IndexBuilder:
    headwords: list[Any] = []
    dictionary: list[Any] = []
    ganaData: GanaData

    def __init__(self, ganaData: GanaData) -> None:
        filename = f"{data_folder}/OALD_V14_8.mdx"
        mdxfile = MDX(filename, "utf-8")
        self.headwords = [*mdxfile]
        self.dictionary = [*mdxfile.items()]
        self.ganaData = ganaData

    def lookup_many(self, queryWords: list[str]) -> None:
        for elem in queryWords:
            self.lookup(elem)

    def lookup(self, queryWord: str) -> None:
        try:
            wordIndex = self.headwords.index(queryWord.encode())
        except ValueError:
            return

        _, val = self.dictionary[wordIndex]
        html = val.decode()
        self.find_in(html)

    def find_in(self, html: str) -> None:
        doc = PyQuery(html)
        webtop_list = doc(
            "body > #entryContent > .entry > .top-container > .top-g > .webtop"
        )

        for elem in webtop_list.items():
            word_type = elem.find(".pos").text()
            headword_contents = elem.find(".headword").contents()
            headword = headword_contents[0]
            if headword.isupper():
                continue

            phons_n_am_list = elem.find(".phonetics > .phons_n_am")
            for n_am in phons_n_am_list.items():
                spelling = n_am.attr("wd")
                phon_obj = n_am.find(".phon")
                phon_list = [*phon_obj.items()]
                phon = phon_list[0].text()
                self.ganaData.add_mapping(word_type, spelling, phon)
