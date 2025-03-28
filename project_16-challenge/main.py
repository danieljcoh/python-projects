from tkinter import *
import json

FONT_NAME = 'Courier'
FONT_SIZE = 16

# FUNCTIONS

def save_entry():
    entry_text = entry_title.get()
    input_text = text_box.get("1.0", END)

    with open("data.json", "w+") as file:
        d = {}
        d[entry_text] = input_text
        json.dump(d, file)

    exit()

def retrieve_text():
    with open("data.json", "r+") as file:
        d = json.load(file)
        return d

### ###

window = Tk()
window.title("Project 16: Challenge")
window.geometry("400x400")
window.config(pady=10)

label_1 = Label(text="Project 16 Challenge", font=(FONT_NAME, FONT_SIZE, "bold"))
label_1.pack()

entry_title = Entry(text="Title")
entry_title.pack()

text_box = Text(width=40, height=10)
text_box.pack()

btn = Button(text="Save", command=save_entry)
btn.pack()

try:
    data = retrieve_text()
    k = ""
    v = ""
    for key,value in data.items():
        k = key
        v = value
    label_2 = Label(text=key, font=(FONT_NAME, FONT_SIZE, "bold"))
    label_2.pack()

    label_3 = Label(text=value, font=(FONT_NAME, FONT_SIZE, "bold"))
    label_3.pack()
except:
    pass


window.mainloop()