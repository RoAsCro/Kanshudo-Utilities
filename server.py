from flask import Flask, render_template
import json
import random
from utils.kanji_extractor import extract
from utils.kanshudo_scraper import scrape_web
from utils.txt_to_csv import convert_all
from utils.word_loader import WordLoader

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract/")
def extract_kanji():
    # ToDo - catch exceptions
    extract()
    return "Kanji extracted"

@app.route("/scrape<confirm>/")
def scrape(confirm):
    if confirm == "false":
        return "<div>Are you sure?<button value='scrapetrue'>Yes</button><button value='scrapeend'>No</button></div>"
    elif confirm == "true":
        scrape_web()
        convert_all()
        return "Flashcards acquired"
    else:
        return ""


# Kanji type
kana_dictionary = str.maketrans('''
    ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじす
    ずせぜそぞただちぢっつづてでとどなにぬねのはばぱひ
    びぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりる
    れろゎわゐゑをんゔゕゖ
    ''',
    '''
    ァアィイゥウェエォオカガキギクグケゲコゴサザシジス
    ズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒ
    ビピフブプヘベペホボポマミムメモャヤュユョヨラリル
    レロヮワヰヱヲンヴヵヶ
    '''
)

KANJI = ""

file = open("data/kanji/kanji.txt", 'r', encoding="utf8")
WORDS = [entry.strip() for entry in file.readlines()]
translated_readings = []
current_readings = []
loader = None

def get_kanji():
    return random.choice(WORDS)

    # with open(file, "r", encoding="utf-8") as entries:

def render_readings(readings):
    html = ""
    for reading in readings:
        current_readings.append(reading)
        translated_readings.append(reading.replace(".", "").translate(kana_dictionary))
        html += f"<input id='{reading}' class='reading'/>"
    print(current_readings)
    return html

@app.route("/kanji_type/")
def kanji_type():
    global KANJI
    global loader
    KANJI = json.loads(open("data/kanji/kanjiapi_full.json", encoding="utf8").read())
    loader = WordLoader()
    entry = kanji_reset()
    current_kanji = entry["kanji"]
    kun_readings = entry["kun_readings"]
    on_readings = entry["on_readings"]
    words = loader.get_entries(current_kanji)
    html = ""
    for word in words:
        html += f"<p>{word}</p>"

    return render_template("kanji_type.html")

@app.route("/kanji_type/kanji_answer/<answer>")
def kanji_answer(answer):
    answers = answer.split(",")
    print(answers)
    output = []
    for response in answers:
        print(response.translate(kana_dictionary))
        print(current_readings)

        if response.translate(kana_dictionary) in translated_readings:
            output.append("True")
        else:
            output.append("False")

    return output

@app.route("/kanji_type/kanji_next/")
def kanji_next():
    entry = kanji_reset()
    current_kanji = entry["kanji"]
    words = loader.get_entries(current_kanji)
    html = ""
    for word in words:
        html += f"<p>{word}</p>"
    return f"{current_kanji},{render_readings(entry["kun_readings"])},{render_readings(entry["on_readings"])},{html}"

def kanji_reset():
    current_kanji = get_kanji()
    print(loader.get_entries(current_kanji))
    entry = KANJI["kanjis"][current_kanji]
    translated_readings.clear()
    current_readings.clear()
    return entry

if __name__ == '__main__':
    app.run(debug=True)

  
