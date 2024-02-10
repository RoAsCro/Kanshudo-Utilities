
import pandas
import random
import re

# Class that loads a list of words from a CSV
class WordLoader():     
    data = pandas.read_csv("data/csv/all-words.csv")
    words = {x.jp:x.en for (y,x) in data.iterrows()}
    jp_words = list(words.keys())
    current_word = None
    # remove_mode = True

    # def settings(self, **remove_mode):
    #     self.remove_mode = remove_mode

    def get_word(self, remove):
        if remove and self.current_word is not None:
            self.jp_words.remove(self.current_word)
        self.current_word = random.choice(self.jp_words)
        return self.current_word
    
    def get_answer(self):
        return self.words[self.current_word]
    
    def get_readings(self):
        answer = self.get_answer()
        english_index = re.search(r"[a-zA-Z]", answer).start()
        readings = answer[answer.find("\n"): english_index].strip().split("\n")
        # print(answer)
        # print(english_index)

        return readings
