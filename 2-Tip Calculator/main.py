# print("hello"[4])
# len(112343)

# nameLength = len(input("Enter your name: "))
# print(f"Your name has {nameLength} characters.")

# print(type(nameLength))

# print(float("10.78") + 23)

# PEMDAS

################################

# # BMI calculator

# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# bmi = weight / (height ** 2)

# print(f"Your BMI is {bmi} units")

################################

# # Life in weeks

# age = int(input("Enter your current age in years: "))
# expectedAge = int(input("Enter your expected age in years you will live upto: "))

# print(f"You have {(expectedAge - age) * 365} days left, {(expectedAge - age) * 52} weeks left and {(expectedAge - age) * 12} months left.")

################################

# Day 2 Project: Tip calculator
"""prints the initial game text"""
print("Welcome to the Tip Calculator!")
"""takes in the initial bill as a float value"""
initialBill = float(input("What was the total bill? ₹"))
"""takes in the tip amount as a float value"""
tip = float(input("What percentage tip would you like to give? "))
"""calculates the total bill"""
totalBill = initialBill + (initialBill * (tip/100))
"""stores the split number"""
splitNumber = int(input("How many people to split the bill with? "))
"""splits the bill"""
splittedBill = totalBill / splitNumber
"""prints the amount to be paid by each individual"""
print(f"Each person should pay ₹{round(splittedBill, 2)}")
