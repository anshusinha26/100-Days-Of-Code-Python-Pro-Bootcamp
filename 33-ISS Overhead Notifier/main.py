## challenge: kanye quotes app
# """imported every class from the tkinter module"""
# from tkinter import *
#
# """imported requests module"""
# import requests
#
# """function to get quotes"""
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#
#     data = response.json()
#     quote = data["quote"]
#
#     canvas.itemconfig(quote_text, text=quote)
#
#
# """created the window object"""
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# """created the canvas object"""
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# """created the kanye_button object"""
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
# """loop to keep the window open"""
# window.mainloop()

# --------------------------------------------------------------------

## day33: iss overhead notifier project

# -------------------- MODULES --------------------

"""imported requests module"""
import requests

"""imported datetime module as dt"""
import datetime as dt

"""imported smptlib module"""
import smtplib

"""imported random module"""
import random

"""imported time module"""
import time

from dotenv import load_dotenv
import os
load_dotenv()


# -------------------- MY DATA --------------------
"""constants"""
MY_LAT = 21.860285
MY_LNG = 84.034145

"""email details"""
MY_EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

receiver = "anshujuly2@gmail.com"


# -------------------- ISS DATA --------------------
"""variable to store the response"""
responseIss = requests.get(url="http://api.open-notify.org/iss-now.json")
responseIss.raise_for_status()

"""variable to store the data"""
dataIss = responseIss.json()

"""iss' latitude and longitude"""
issLat = float(dataIss["iss_position"]["latitude"])
issLng = float(dataIss["iss_position"]["longitude"])


# -------------------- SUN DATA --------------------
"""dictionary to hold the parameters"""
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

"""variable to store the response for the sun"""
responseSun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
responseSun.raise_for_status()

"""variable to hold the data for the sun"""
dataSun = responseSun.json()

"""variables to hold the sunrise and sunset"""
sunrise = int(dataSun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(dataSun["results"]["sunset"].split("T")[1].split(":")[0])

timeNow = dt.datetime.now().hour


# -------------------- FACTS ABOUT ISS --------------------
with open("facts.txt") as file:
    issFactsList = file.readlines()


# # -------------------- NOTIFIER --------------------
# """function to check if iss is overhead"""
# def isIssOverhead():
#     if MY_LAT - 5 <= issLat <= MY_LAT + 5 and MY_LNG - 5 <= issLng <= MY_LNG + 5:
#         return True
#
# """function to check if it's night"""
# def isNight():
#     if sunset <= timeNow <= sunrise:
#         return True
#
# while True:
#     time.sleep(60)
#     if isIssOverhead() and isNight():
#         with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
#             connection.starttls()
#             connection.login(
#                 user=MY_EMAIL,
#                 password=PASSWORD
#             )
#             connection.sendmail(
#                 from_addr=MY_EMAIL,
#                 to_addrs=receiver,
#                 msg=f"Subject:Look up, ISS is overhead 🛰️\n\n{random.choice(issFactsList)}".encode("utf-8")
#             )

# -------------------- TEST NOTIFIER --------------------
def isIssOverhead():
    return True  # Override to always return True for testing

def isNight():
    return True  # Override to always return True for testing

# Test the notification logic directly
if isIssOverhead() and isNight():
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=receiver,
            msg=f"Subject:Look up, ISS is overhead 🛰️\n\n{random.choice(issFactsList)}".encode("utf-8")
        )
    print("Test email sent successfully!")