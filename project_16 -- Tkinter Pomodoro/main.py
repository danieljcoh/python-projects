from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

window.after()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_label = Label(text="Title", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
title_label.config(pady=10)
title_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # the data type canvas expects for images
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_btn = Button(text="Start", width=10, bg=YELLOW, highlightbackground=YELLOW)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", width=10, bg=YELLOW, highlightbackground=YELLOW)
reset_btn.grid(column=2, row=2)

# Checkmark Label
check_mark_label = Label(text="√", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=1, row=3)


window.mainloop()