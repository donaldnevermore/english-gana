from readmdict import MDX


def lookup() -> None:
    filename = "D:/Shared/OALD_V14_8.mdx"
    mdxfile = MDX(filename)
    headwords = [*mdxfile]
    items = [*mdxfile.items()]

    queryWord = "come"
    wordIndex = headwords.index(queryWord.encode())
    key, val = items[wordIndex]
    word, html = key.decode(), val.decode()

    print(word)


lookup()
