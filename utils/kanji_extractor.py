import pandas
import re


def extract():
    data = pandas.read_csv("data/csv/all-words.csv")
    entries = list({x.jp:x.en for (y,x) in data.iterrows()}.keys())
    kanji = re.compile(r"[\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A]", re.U)

    # print("Yes" if kanji.match("外") else "No")

    kanji_list = []

    for entry in entries:
        for char in entry:
            if kanji.match(char):
                if char not in kanji_list:
                    kanji_list.append(char)

    with open("data/kanji/kanji.txt", "w", encoding="utf-8") as text:
        output = ""
        for 漢字 in kanji_list:
            output += "\n" + 漢字
        text.write(output)

