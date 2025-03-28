from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        reps += 1
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        reps += 1
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        reps += 1
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps 
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec >= 10:
        count_sec = f"{count_sec}"
    elif count_sec < 10 and count_sec > 0:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"
    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "√"
        work_session = math.floor(reps % 2)
        for _ in range(work_session):
            marks += "√"
        check_mark_label.config(text=marks)
        


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
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_btn = Button(text="Start", width=10, bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", width=10, bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

# Checkmark Label
check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(column=1, row=3)


window.mainloop()