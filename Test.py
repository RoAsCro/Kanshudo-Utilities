from tkinter import *
import gzip
import csv
from utils.kanji_extractor import KANJI
import json

def run():

    ws = Tk()
    ws.title('PythonGuides')
    ws.config(bg='#D9D8D7')
    ws.geometry('400x300')

    tb = Text(
        ws,
        width=25, 
        height=8,
        font=('Times', 20),
        wrap='word',
        fg='#4A7A8C'
    )
    tb.pack(expand=True)

    ws.mainloop()


kanji = json.loads(open("data/kanji/kanjiapi_full.json", encoding="utf8").read())
print(kanji["kanjis"]["外"])
print(len(kanji["readings"]))
print(len(kanji["words"]))
# for k in kanji[0]:
    # print(k)

# readFile = gzip.open("utils/JMdict_e.gz", mode="rt", encoding="utf8")
# reader = csv.reader(readFile)
# number = 0
# for row in reader:
#     number += 1
#     # if (number > 1000):
#     #     break
#     # print(number)
#     if len(row) > 0:
#         if "<keb>" in row[0]:
#             # print(row)
#             count = 0
#             word = ""
#             # print(row[0][4:])
#             for character in row[0][5:]:
#                 # print(character)
#                 if character == "<":
#                     break
#                 if KANJI.match(character):
#                     # print(row)
#                     word += character
#                 count += 1
#             # print(count)
#             if len(word) == 1 and count == 1:
#                 print(row)

# 521
# file = gzip.GzipFile("utils/JMdict_e.gz", mode="r")
# print(file.readine())