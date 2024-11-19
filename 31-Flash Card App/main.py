"""imported every class from the tkinter module"""
from tkinter import *

"""imported pandas module"""
import pandas

"""imported random module"""
import random


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
timer = None
randomNum = None
unknownCards = {}


# ---------------------------- CHANGING FLASH CARDS ------------------------------- #
"""function to change to front card"""
def changeToFront():
    canvas.itemconfig(cardImage, image=cardFront)
    canvas.itemconfig(langText, text="French", fill="black")
    canvas.itemconfig(wordText, text=randomFrench(), fill="black")

    global timer
    timer = window.after(3000, changeToBack)



"""function to change to back card"""
def changeToBack():
    canvas.itemconfig(cardImage, image=cardBack)
    canvas.itemconfig(langText, text="English", fill="white")
    canvas.itemconfig(wordText, text=randomEnglish(), fill="white")

    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
"""function to start the timer"""
def startTimer():
    global timer
    timer = window.after(3000, changeToBack)


# ---------------------------- GENERATING RANDOM WORDS ------------------------------- #
"""variable to store the csv data"""
data = pandas.read_csv("data/french_words.csv")

"""converted to list of dictionaries"""
dataList = data.to_dict(orient="records")

"""variable to store the length of the dataList"""
dataListLength = len(dataList)

"""function to return random french word"""
def randomFrench():
    global randomNum
    """variable to store random number"""
    randomNum = random.randint(0, dataListLength - 1)

    wordFrench = dataList[randomNum]["French"]
    return wordFrench

"""function to return random english word"""
def randomEnglish():
    wordEnglish = dataList[randomNum]["English"]
    return wordEnglish


# ---------------------------- SAVE PROGRESS ------------------------------- #
if dataListLength > 1:
    """function to remove card which is known"""
    def knownCard():
        global dataListLength
        print(dataListLength)
        dataList.remove(dataList[randomNum])
        dataListLength = len(dataList)

        changeToFront()

else:
    print("Done")

if dataListLength > 1:
    """function to remove card which is unknown and store it in unknownCards dictionary"""
    def unknownCard():
        global dataListLength
        print(dataListLength)
        unknownCard = dataList.pop(randomNum)
        unknownCards.update(unknownCard)
        dataListLength = len(dataList)

        changeToFront()

else:
    print("Done")


# ---------------------------- UI SETUP ------------------------------- #

# window

"""created the window object"""
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas

"""created the canvas object"""
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
cardImage = canvas.create_image(400, 263, image=cardFront)
langText = canvas.create_text(400, 150, text="French", font=FONT_LANG, fill="black")
wordText = canvas.create_text(400, 263, text=randomFrench(), font=FONT_WORD, fill="black")
canvas.grid(row=1, column=1, columnspan=2)

# button

"""created the buttonWrong object"""
wrongImage = PhotoImage(file="images/wrong.png")
buttonWrong = Button(image=wrongImage, bd=0, highlightthickness=0, command=unknownCard)
buttonWrong.grid(row=2, column=1)

"""created the buttonRight object"""
rightImage = PhotoImage(file="images/right.png")
buttonRight = Button(image=rightImage, bd=0, highlightthickness=0, command=knownCard)
buttonRight.grid(row=2, column=2)

"""initial start timer"""
startTimer()

"""loop to keep the window open"""
window.mainloop()
