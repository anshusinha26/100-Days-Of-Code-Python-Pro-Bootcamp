# """imported smtplib module"""
# import smtplib
#
# """variable to store email address and password"""
# myEmail = "gpython72@gmail.com"
# password = "blxfzquksftguoxk"
#
# """variable to store receiver's address"""
# receiver = "anshujuly26@yahoo.com"
#
# with smtplib.SMTP(
#     "smtp.gmail.com",
#     port=587,
#     timeout=25
# ) as connection:
#
#     """securing our connection"""
#     connection.starttls()
#
#     """login"""
#     connection.login(
#         user=myEmail,
#         password= password
#     )
#
#     """send mail"""
#     connection.sendmail(
#         from_addr=myEmail,
#         to_addrs=receiver,
#         msg="Subject:Hi!\n\nThis is the new body of the message."
#     )

# ------------------------------------------------------------

## working with the datetime module

# """imported datetime module as dt"""
# import datetime as dt
#
# """created now object"""
# now = dt.datetime.now()
#
# year = now.year
# month = now.month
# day = now.day
#
# date = now.date()
#
# dayOfTheWeek = now.weekday()
# print(dayOfTheWeek)
#
# dateOfBirth = dt.datetime(year=2003, month=7, day=26)
# print(dateOfBirth.date())

# ------------------------------------------------------------

## challenge 1: send motivational quotes on wednesday via email

# """imported smtplib module"""
# import smtplib
#
# """imported datetime module as dt"""
# import datetime as dt
#
# """imported random module"""
# import random
#
# """created the now object"""
# now = dt.datetime.now()
# dayOfTheWeek = now.weekday()
#
# """variable to store email address and password"""
# myEmail = "gpython72@gmail.com"
# password = "blxfzquksftguoxk"
#
# """variable to store receiver's address"""
# receiver = "anshujuly26@yahoo.com"
#
# """reading text file"""
# with open("quotes.txt") as file:
#     quotesList = file.readlines()
#
# """send email when it's wednesday"""
# if dayOfTheWeek == 2:
#     with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
#         connection.starttls()
#         connection.login(
#             user=myEmail,
#             password=password,
#         )
#         connection.sendmail(
#             from_addr=myEmail,
#             to_addrs=receiver,
#             msg=f"Subject:Wednesday motivational quote!\n\n{random.choice(quotesList)}",
#         )

# ------------------------------------------------------------

## day32: automated birthday wisher

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


# -------------------- MODULES --------------------
"""imported smtplib module"""
import smtplib

"""imported pandas module"""
import pandas

"""imported datetime module as dt"""
import datetime as dt

"""imported random module"""
import random

from dotenv import load_dotenv
import os
load_dotenv()


# -------------------- GETTING DATA --------------------
"""variable to store the csv data"""
data = pandas.read_csv("birthdays.csv")

"""dictionary to store data"""
birthdayDict = {(dataRow.month, dataRow.day): dataRow for (index, dataRow) in data.iterrows()}


# -------------------- WORKING WITH DATES --------------------
now = dt.datetime.today()

"""variable to store month"""
t_month = now.month

"""variable to store year"""
t_day = now.day

"""tuple to store month and day"""
t_tuple = (t_month, t_day)


# -------------------- WORKING WITH EMAILS --------------------
"""variable to store email address and password"""
myEmail = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
    connection.starttls()
    connection.login(
        user=myEmail, password=password
    )

    for birthday in birthdayDict.values():
        if (birthday["month"], birthday["day"]) == (t_month, t_day):
            birthdayPerson = birthday["name"]
            birthdayPersonEmail = birthday["email"]
            randomNum = random.randint(1, 3)
            with open(f"letter_templates/letter_{randomNum}.txt") as file:
                letter = file.read()
                birthdayLetter = letter.replace("[NAME]", birthdayPerson)

            connection.sendmail(
                from_addr=myEmail,
                to_addrs=birthdayPersonEmail,
                msg=f"Subject:Happy birthday {birthdayPerson}!\n\n{birthdayLetter}"
            )


