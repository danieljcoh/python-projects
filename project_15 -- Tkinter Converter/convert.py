from tkinter import *

window = Tk()

window.title("Converter!")
window.geometry("300x300")
window.config(padx=50, pady=50)

# Functions
def convert():
    miles = int(input_1.get())
    km = miles * 1.609344
    label_3["text"] = str(round(km, 2))

# Input
input_1 = Entry(width=10)
input_1.grid(column=1, row=0)

# label 1
label_1 = Label(text="miles", font=("Arial", 14))
label_1.grid(column=2, row=0)

# label 2
label_2 = Label(text="is equal to", font=("Arial", 14))
label_2.grid(column=0, row=1)

# label 3
label_3 = Label(text="0", font=("Arial", 14))
label_3.grid(column=1, row=1)

# label 4
label_4 = Label(text="Km", font=("Arial", 14))
label_4.grid(column=2, row=1)

# Button
calc_btn = Button(text="Calculate", command=convert)
calc_btn.grid(column=1, row=2)


window.mainloop()