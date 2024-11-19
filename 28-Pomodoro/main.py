"""imported every class from the tkinter module"""
from tkinter import *

"""imported math module"""
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
"""function to stop the timer"""
def stopTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    labelTimer.config(text="Timer", fg=GREEN)
    labelCheck.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
"""function to start the timer"""
def startTimer():
    global reps
    reps += 1

    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        labelTimer.config(text="Break", fg=RED)
        countDown(longBreakSec)
    elif reps % 2 == 0:
        labelTimer.config(text="Break", fg=PINK)
        countDown(shortBreakSec)
    elif reps % 2 != 0:
        labelTimer.config(text="Work", fg=GREEN)
        countDown(workSec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
"""function to count down time"""
def countDown(time):
    minutes = time // 60
    seconds = time % 60

    """improved the UI of time display"""
    if len(str(seconds)) == 1:
        canvas.itemconfig(timerText, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(timerText, text=f"{minutes}:{seconds}")

    if time > 0:
        global timer
        timer = window.after(1000, countDown, time - 1)
    else:
        startTimer()
        marks = ""
        workSessions = math.floor(reps/2)
        for _ in range(workSessions):
            marks += "✔"
        labelCheck.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
"""created the window object"""
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

"""created the canvas widget"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timerText = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

"""created the labelTimer object"""
labelTimer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
labelTimer.grid(row=1, column=2)
labelTimer.config(padx=20, pady=20)

"""created the labelCheck object"""
labelCheck = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
labelCheck.grid(row=4, column=2)
labelCheck.config(padx=20, pady=20)

"""created the buttonStart object"""
buttonStart = Button(text="Start", command=startTimer)
buttonStart.grid(row=3, column=1)
buttonStart.config(padx=20, pady=20)

"""created the buttonReset object"""
buttonReset = Button(text="Reset", command=stopTimer)
buttonReset.grid(row=3, column=3)
buttonReset.config(padx=20, pady=20)


"""loop to keep the window running"""
window.mainloop()