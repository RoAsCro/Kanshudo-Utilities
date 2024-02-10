from flask import Flask, render_template
from flask import request
from utils.kanji_extractor import extract
from utils.kanshudo_scraper import scrape_web

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
        return "Flashcards acquired"
    else:
        return ""

if __name__ == '__main__':
    app.run(debug=True)

  
