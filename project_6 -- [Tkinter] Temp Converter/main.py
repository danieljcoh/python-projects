# import math?
import tkinter as tk


window = tk.Tk()
window.title("Temp converter")
window.geometry("250x150")

def get_entry_input():
    print("zombies")

def convert_to_f():
    temp = temperature_entry.get()
    print(temp)

def convert_to_c():
    temp = temperature_entry.get()
    print(temp)


temperature_label = tk.Label(window, text="Temperature")
temperature_entry = tk.Entry(window, width=15)
convert_to_f_btn = tk.Button(window, text="To Farenheit", width=10, command=convert_to_f)
convert_to_c_btn = tk.Button(window, text="To Celcius", width=10, command=convert_to_c)

temperature_label.pack()
temperature_entry.pack()
convert_to_f_btn.pack(side=tk.RIGHT)
convert_to_c_btn.pack(side=tk.LEFT)


# TODO
# - math equation for each function
# - create a new label and show the return of the function on that label - show convert result
# - pack or grid for layout?



window.mainloop()

