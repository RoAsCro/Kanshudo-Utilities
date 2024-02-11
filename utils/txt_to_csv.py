# Class for converting Kanshudo's flashcard .txt output to .csv
import pandas
import os
import re


BACK = []
FRONT = []

# Converts the .txt file at the given path to a 
def convert_file(file):
    
    with open(file, "r", encoding="utf-8") as entries:
        for entry in entries:
            front_back = entry.split("\t")
            back = front_back[1]
            if back[0] == '(':
                continue

            english_index = re.search(r"[a-zA-Z]|[(]", back).start() # Index of start of English definition

            jp = back[back.find(" "): english_index]
            
            readings = jp.strip().replace("  ", "\n")
            
            english = back[english_index: ] # String containing English definition
            eng_entries = english.replace("; ", "\n")
            front = front_back[0]
            BACK.append(front + "\n" + readings + "\n\n" + eng_entries)
            FRONT.append(front)


            

def convert_all():
    DIRECTORY = "./data/text"
    os.chdir(DIRECTORY)
    text_files = os.listdir()
    print()
    for file in text_files:
        convert_file(file)
    pandas.DataFrame({"jp": FRONT, "en": BACK}).to_csv("../csv/all-words.csv")
