from tkinter import *
from utils.word_loader import WordLoader

BACKGROUND_COLOR = "#151824"
TEXT_COLOUR = "#ebebeb"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
JP_FONT = 90



# Initialise UI
window = Tk()
window.title("Answer Type")

window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
word_loader = WordLoader()

word = Label(canvas, text=word_loader.get_word(False), font=("arial", JP_FONT), bg=BACKGROUND_COLOR, fg=TEXT_COLOUR)
word.grid(column=2, row=0, )

text_box = Text(canvas, height=1, width=30, font=("arial", 24))
text_box.grid(column=2, row=1)

def enter_answer(answer):
    print("test")
    answer = text_box.get(1.0, END)
    if answer in word_loader.get_readings():
        print("correct")
    
window.bind('<Return>', enter_answer)



window.mainloop()
