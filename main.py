from tkinter import *
from utils.word_loader import WordLoader

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
FRONT_FONT = 40
BACK_FONT = 19

# Load WordLoader
word_loader = WordLoader()


# UI

window = Tk()
window.title("Flash Cards")
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=3)
# Front
current_img = canvas.create_image(450, 300, image=card_front, tag="front")
word = canvas.create_text(450, 263, text=word_loader.get_word(False), font=("arial", FRONT_FONT, "bold"))


right_button = Button(image=right, highlightthickness=0, command=lambda: new_word(True))
right_button.grid(column=1, row=2)

wrong_button = Button(image=wrong, highlightthickness=0, command=lambda: new_word(False))
wrong_button.grid(column=3, row=2)



# Next word
def new_word(yes_no):

    r_jp_word = word_loader.get_word(yes_no)
    global word

    canvas.delete(word)
    canvas.itemconfig(current_img, image=card_front, tag="front")

    word = canvas.create_text(450, 263, text=r_jp_word, font=("arial", FRONT_FONT, "bold"))

def click(event):
    x_bound = (CANVAS_WIDTH - card_front.width()) / 2
    y_bound = (CANVAS_HEIGHT - card_front.height()) / 2
    
    if x_bound < event.x < CANVAS_WIDTH - x_bound and y_bound < event.y < CANVAS_HEIGHT - y_bound:
        swap()
        

window.bind("<Button>", click)

def swap():
    front_back = "front" in canvas.itemcget(current_img, "tag")

    new_image = card_back if front_back else card_front
    new_tag = "back" if front_back else "front"
    new_text = word_loader.get_answer() if front_back else word_loader.current_word

    canvas.itemconfig(current_img, image=new_image, tag=new_tag)
    canvas.itemconfig(word, text=new_text, font=("arial", BACK_FONT if front_back else FRONT_FONT, "bold"))
    window.bind("<Button>", click)

window.mainloop()
