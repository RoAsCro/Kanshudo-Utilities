from tkinter import *
from utils.word_loader import WordLoader
from utils.kanji_extractor import KANJI

BACKGROUND_COLOR = "#151824"
TEXT_COLOUR = "#ebebeb"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
JP_FONT = 90

def load_word(delete):
    current_word = word_loader.get_word(delete)
    while not KANJI.search(current_word):
        current_word = word_loader.get_word(True)
    return current_word


# Initialise UI
window = Tk()
window.title("Answer Type")

window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
word_loader = WordLoader()

word = Label(canvas, text=load_word(False), font=("arial", JP_FONT), bg=BACKGROUND_COLOR, fg=TEXT_COLOUR)
word.grid(column=2, row=0, )

text_box = Text(canvas, height=1, width=30, font=("arial", 24))
text_box.grid(column=2, row=1)
questions = 0
correct = 0
def enter_answer(answer):
    global questions
    global correct
    answer = text_box.get(1.0, END)
    readings = word_loader.get_readings()
    if answer.strip() in readings:
        correct += 1
        print("correct")
    else:
        print("incorrect")
    print(f"Your answer = {answer.strip()}")
    print(word_loader.current_word.strip())
    # print(readings)
    print(word_loader.get_answer().strip())
    print(readings)
    
    questions += 1
    print()
    print(f"{correct}/{questions}")
    text_box.delete(1.0, END)

    
    global word
    word.config(text=load_word(True))
    
window.bind('<Return>', enter_answer)



window.mainloop()
