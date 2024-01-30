from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.config(bg='#D9D8D7')
ws.geometry('400x300')

tb = Text(
    ws,
    width=25, 
    height=8,
    font=('Times', 20),
    wrap='word',
    fg='#4A7A8C'
)
tb.pack(expand=True)

ws.mainloop()