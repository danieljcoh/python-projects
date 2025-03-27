from tkinter import *


window = Tk()
window.title("Test!")
window.geometry("400x400")


def first_button_clicked():
    text = input.get()
    my_label["text"] = text

def second_button_clicked():
    my_label["text"] = "2nd BTN"


# Label
my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label["text"] = "NEW TEXT!"
my_label.config(text="new text...")
my_label.grid(column=0, row=0)

# Button 1
btn = Button(text="Click me!", command=first_button_clicked)
btn.grid(column=1, row=1)

# Button 2
btn_2 = Button(text="Second button!", command=second_button_clicked)
btn_2.grid(column=2, row=0)

# entry
ent = Entry()
ent.grid(column=3, row=3)


window.mainloop()