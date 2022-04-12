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
tick_change = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global tick_change
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    tick_change = ""
    tick_label.config(text=tick_change, bg=YELLOW)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        title_label.config(text="Timer")
    if reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        title_label.config(text="Short break")
    if reps == 8:
        count_down(short_break_sec)
        reps = 0
        title_label.config(text="Long break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
def count_down(count):
    global reps
    global tick_change
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    count_min_str = str(count_min)
    if len(count_min_str) < 2:
        count_min_str = "0" + count_min_str

    count_sec_str = str(count_sec)
    if len(count_sec_str) < 2:
        count_sec_str = "0" + count_sec_str

    canvas.itemconfig(timer_text, text=f"{count_min_str}:{count_sec_str}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_change += "✅"
        tick_label.config(text=tick_change, bg=YELLOW)




window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
title_label.config(font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)



start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

tick_label = Label(text="", bg=YELLOW)
tick_label.grid(column=1, row=3)



window.mainloop()
