import random
import json
from utils.word_loader import WordLoader
class KanjiType():
    KANA_DICTIONARY = str.maketrans('''
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
    KANJI = "" # The loaded kanji dictionary
    WORDS = [] # The loaded list of kanji to be used
    LOADER = None # The WordLoader for getting the known words for the kanji

    translated_readings = [] # The readings for the current kanji standardised to hiragana

    def __init__(self):
        self.KANJI = json.loads(open("data/kanji/kanjiapi_full.json", encoding="utf8").read())
        self.LOADER = WordLoader()
        self.WORDS = self.load_words()

    def load_words(self):
        file = open("data/kanji/kanji.txt", 'r', encoding="utf8")
        return [entry.strip() for entry in file.readlines()]

    def get_kanji(self):
        return random.choice(self.WORDS)

    def kanji_answer(self, answer):
        answers = answer.split(",")
        print(answers)
        output = []
        for response in answers:
            if response.translate(self.KANA_DICTIONARY) in self.translated_readings:
                output.append("True")
            else:
                output.append("False")

        return output
    
    # Rendering HTML
    def kanji_next(self):
        entry = self.kanji_reset()
        current_kanji = entry["kanji"]
        words = self.LOADER.get_entries(current_kanji)
        html = ""
        for word in words:
            html += f"<p>{word}</p>"
        return f"{current_kanji},{self.render_readings(entry["kun_readings"])},{self.render_readings(entry["on_readings"])},{html}"
    
    def render_readings(self, readings):
        html = ""
        for reading in readings:
            self.translated_readings.append(reading.replace(".", "").translate(self.KANA_DICTIONARY))
            html += f"<input id='{reading}' class='reading'/>"
        return html

    def kanji_reset(self):
        current_kanji = self.get_kanji()
        entry = self.KANJI["kanjis"][current_kanji]
        self.translated_readings.clear()
        return entry
