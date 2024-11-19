"""imported every class from the tkinter module"""
from tkinter import *

"""imported messagebox class from the tkinter module"""
from tkinter import messagebox

"""imported random module"""
import random

"""imported pyperclip module"""
import pyperclip

"""imported json module"""
import json

"""constant"""
FONT = ("Courier", 20, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
"""function to generate password"""
def genPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nrLetters = random.randint(8, 10)
    nrSymbols = random.randint(2, 4)
    nrNumbers = random.randint(2, 4)

    passwordLetters = [random.choice(letters) for char in range(nrLetters)]
    passwordSymbols = [random.choice(symbols) for sym in range(nrSymbols)]
    passwordNumbers = [random.choice(numbers) for num in range(nrNumbers)]

    passwordList = passwordLetters + passwordSymbols + passwordNumbers

    random.shuffle(passwordList)

    password = "".join(passwordList)

    entryPassword.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
"""function to store the data in a file"""
def addData():
    website = entryWebsite.get()
    emailUsername = entryEmailUsername.get()
    password = entryPassword.get()
    newData = {
        website: {
            "email": emailUsername,
            "password": password
        }
    }

    if len(website) == 0 or len(emailUsername) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please don't leave any fields empty!")
    else:

        try:
            with open("data.json", mode="r") as file:
                """reading the old data"""
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                """creating the json file if it doesn't exist"""
                json.dump(newData, file, indent=4)

        else:
            """updating the old data with new data"""
            data.update(newData)

            with open("data.json", mode="w") as file:
                """writing the new data"""
                json.dump(data, file, indent=4)

        finally:
            entryWebsite.delete(0, END)
            entryPassword.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
"""function to show the data of the website"""
def showData():
    website = entryWebsite.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(message="No data file exists!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(message=f"No data for {website} exists!")


# ---------------------------- UI SETUP ------------------------------- #

# window

"""created the window object"""
window = Tk()
window.title("Password manager")
window.config(padx=100, pady=100)

# canvas

"""created the canvas object"""
canvas = Canvas(width=200, height=200)
logoImage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImage)
canvas.grid(row=1, column=2)

# label

"""created the labelWebsite object"""
labelWebsite = Label(text="Website:", font=FONT)
labelWebsite.grid(row=2, column=1)

"""created the labelEmailUsername object"""
labelEmailUsername = Label(text="Email/Username:", font=FONT)
labelEmailUsername.grid(row=3, column=1)

"""created the labelPassword object"""
labelPassword = Label(text="Password:", font=FONT)
labelPassword.grid(row=4, column=1)

# entry

"""created the entryWebsite object"""
entryWebsite = Entry(width=35)
entryWebsite.focus()
entryWebsite.grid(row=2, column=2, columnspan=2)

"""created the entryEmailUsername object"""
entryEmailUsername = Entry(width=35)
entryEmailUsername.insert(0, "anshujuly2@gmail.com")
entryEmailUsername.grid(row=3, column=2, columnspan=2)

"""created the entryPassword object"""
entryPassword = Entry(width=20)
entryPassword.grid(row=4, column=2)

# button

"""created the buttonSearch object"""
buttonSearch = Button(text="Search", width=11, command=showData)
buttonSearch.grid(row=2, column=3)

"""created the buttonPassword object"""
buttonPassword = Button(text="Generate Password", width=11, command=genPassword)
buttonPassword.grid(row=4, column=3)

"""created the buttonAdd object"""
buttonAdd = Button(text="Add", width=32, command=addData)
buttonAdd.grid(row=5, column=2, columnspan=2)


"""loop to keep the window open"""
window.mainloop()
