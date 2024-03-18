import random
import json
import math
from utils.word_loader import WordLoader
class KanjiType():
    # A dictionary for translating katakana to hiragana in order to standardise text
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
    REVISION_WORDS = []
    LOADER = None # The WordLoader for getting the known words for the kanji

    translated_readings = [] # The readings for the current kanji standardised to hiragana

    def __init__(self):
        self.KANJI = json.loads(open("data/kanji/kanjiapi_full.json", encoding="utf8").read())["kanjis"]
        self.LOADER = WordLoader()
        self.WORDS = self.load_words()

    def load_words(self):
        file = open("data/kanji/kanji.txt", 'r', encoding="utf8")
        return [entry.strip() for entry in file.readlines()]

    def get_kanji(self):
        if len(self.WORDS) == 0:
            self.WORDS = self.load_words()
        revise = math.floor(random.randint(0, 9) / ((10 - len(self.REVISION_WORDS)) if len(self.REVISION_WORDS) < 10 else 9))
        # revise = 0
        current = ""
        # Ignore blank lines
        while current == "":
            current = self.REVISION_WORDS.pop() if revise else random.choice(self.WORDS)
        if not revise:
            self.REVISION_WORDS.insert(0, current)
        return current

    def kanji_answer(self, answer):
        answers = answer.split(",")
        output = []
        for response in answers:
            if response.translate(self.KANA_DICTIONARY) in self.translated_readings:
                output.append("True")
            else:
                output.append("False")

        return output
    
    def kanji_reset(self):
        current_kanji = self.get_kanji()
        entry = self.KANJI[current_kanji]
        self.translated_readings.clear()
        return entry
    
    # Rendering HTML
    def kanji_next(self):
        entry = self.kanji_reset()
        current_kanji = entry["kanji"]
        words = self.LOADER.get_entries(current_kanji)
        html = f"<p>{"; ".join(entry["meanings"])}</p>"
        for word in words:
            html += f"<p>{word}</p>"
        return f"{current_kanji},,{self.render_readings(entry["kun_readings"])},,{self.render_readings(entry["on_readings"])},,{html}"
    
    def render_readings(self, readings):
        html = ""
        for reading in readings:
            self.translated_readings.append(reading.replace(".", "").translate(self.KANA_DICTIONARY))
            html += f"<input id='{reading}' class='reading'/>"
        return html
