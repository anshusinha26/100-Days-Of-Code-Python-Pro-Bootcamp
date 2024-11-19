# print("Welcome to the roller coaster!")
# height = int(input("Enter your height in cm: "))

# bill = 0

# if (height > 120):
#     print("You can ride the roller coaster!")
#     age = int(input("Enter your age in years: "))
#     wantPhotos = input("Do you want photos? y/n ").lower()
#     if (age <= 12):
#         bill += 5
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
#     elif (12 < age < 18):
#         bill += 7
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
#     else:
#         bill += 12
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
# else:
#     print("You can't ride the roller coaster!")

################################################################
"""prints the ascii are for the project"""
print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"'"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")

# Day 3 Project: Treasure island
"""prints the initial project text"""
print("Welcome to the Treasure Island!")
"""prints the mission statement"""
print("Your mission is to find the treasure.")
"""asks for the direction"""
direction = input("You're at a cross road. Where do you want to go? Type 'l' for 'left' or 'r' for 'right': ").lower()
"""if the user has chosen the right direction, the game ends"""
if (direction == "r"):
    print("You fell into a hole. Game over!")
    """else if the user has chosen left direction, the user is taken to a lake"""
elif (direction == "l"):
    """asks whether the user wants to swim or wants to take a wait"""
    decision1 = input("""You've come to a lake. There is an island in the middle of the lake. 
    Type 'w' to 'wait' for a boat or type 's' to 'swim' across: """).lower()
    """if the user wants to wait, then he will reach the island unharmed"""
    if (decision1 == "w"):
        """user is asked to take a decision on whether he wants to enter blue, yellow or red door"""
        decision2 = input("""You arrived at the island unharmed. 
        There is a house with 3 doors. One red, one yellow and one blue. 
        Which colour do you chose? Type 'r' for 'red', 'y' for 'yellow' or 'b' for 'blue': """).lower()
        """if the door is red, the game ends"""
        if (decision2 == "r"):
            print("It's a room full of fire. Game over!")
        elif (decision2 == "y"):
            """else if the door is yellow, the game ends"""
            print("You entered a room full of beasts. Game over!")
            """else if the door is blue, the user wins the game"""
        elif (decision2 == "b"):
            print("You found the treasure! You won!")
            """if the user selects to swim, then he is attacked by a trout, and the game ends"""        
    elif (decision1 == "s"):
        print("You got attacked by an angry trout. Game over!")



