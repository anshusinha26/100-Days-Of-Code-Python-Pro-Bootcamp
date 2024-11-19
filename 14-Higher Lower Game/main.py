"""random module is imported"""
import random
"""os module is imported"""
import os
"""higherlower module is imported"""
import higherlower

"""this variable stored the logo"""
logo = higherlower.logo
"""this variable stores the vs logo"""
vs = higherlower.vs
"""this variable stores the data"""
data = higherlower.data

"""initially the score is set to zero"""
score = 0

"""this variable stores the answer"""
answer = ""
"""this variable stotes the guessed answer"""
guess = ""

"""this function generates data by randomly chosing first and second datas and 
manipulates the global variables according to the conditions, when the guessed 
answer is true score is incremented by 1 and if the guessed answer is false the 
function ends and a final score is displayec with a sorry message"""
def genData():
    global answer
    global guess
    global score

    firstData = data[random.randint(0, len(data) - 1)]
    secondData = data[random.randint(0, len(data) - 1)]

    while (firstData["name"] == secondData["name"]):
        secondData = data[random.randint(0, len(data) - 1)]
        
    firstDataFollowers = firstData["follower_count"]
    secondDataFollowers = secondData["follower_count"]

    print(logo)

    print(f"Compare A: {firstData['name']}, a {firstData['description']}, from {firstData['country']}.")

    print(vs)

    print(f"Against B: {secondData['name']}, a {secondData['description']}, from {secondData['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (guess != "A" and guess != "B"):
        os.system("clear")
        print("Invalid input. Please try again.")
        genData()
        return

    if (firstDataFollowers > secondDataFollowers):
        answer = "A"
    else:
        answer = "B"

    if (guess != answer):
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score += 1
        os.system("clear")
        print(f"You're right! Current score: {score}")
        genData()

genData()




