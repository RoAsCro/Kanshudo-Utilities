from flask import Flask, render_template
import json
import random
from utils.kanji_extractor import extract
from utils.kanshudo_scraper import scrape_web
from utils.txt_to_csv import convert_all
from utils.word_loader import WordLoader
from kanji_type import KanjiType

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
@app.route("/kanji_type/")
def kanji_type():
    print("cals")
    global kanji_app
    kanji_app = KanjiType()
    return render_template("kanji_type.html")

@app.route("/kanji_type/kanji_answer/<answer>")
def kanji_answer(answer):
    return kanji_app.kanji_answer(answer)

@app.route("/kanji_type/kanji_next/")
def kanji_next():
    return kanji_app.kanji_next()

if __name__ == '__main__':
    app.run(debug=True)

  
