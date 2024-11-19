# import random

# randomInteger = random.randint(1, 10)
# print(randomInteger)

# randomFloat = random.random()
# print(randomFloat)

# statesOfIndia = ["Jharkhand", "Odisha", "Bihar"]
# print(statesOfIndia[0])
# print(statesOfIndia[-1])
# statesOfIndia[2] = "Delhi"
# print(statesOfIndia[-1])

# statesOfIndia.append("Madhya Pradesh")
# print(statesOfIndia)
# statesOfIndia.extend(["Uttar Pradesh", "Jammu and Kashmir", "Manipur"])
# print(statesOfIndia)

# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
# vegetables = ["spinach", "kale", "potatoes", "tomatoes", "celeries"]
# dirtyDozens = [fruits, vegetables]
# print(dirtyDozens)

#############################

# Day 4 Project: Rock Paper Scissors
"""imports random module"""
import random

"""stores rock ascii art"""
rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
"""stores paper ascii art"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
"""stores scissors ascii art"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
"""asks the user to chose rock, paper or scissors"""
myChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
"""random numbers are generated between 0 and 2"""
computerChoice = random.randint(0, 2)
"""if user's choice is 0, rock is printed"""
if (myChoice == 0):
    print(f"You chose:\n{rock}")
    """if computer's choice is 0, game is draw"""
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nIt's a draw!")
        """if computer's choice is 1, the computer wins"""
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nYou lose!")
        """if computer's choioe is 2, the user wins """
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nYou won!")
    """if user's choice is 1, paper is printed"""
elif (myChoice == 1):
    print(f"You chose:\n{paper}")
    """if computer's choice is 0, the user wins"""
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nYou won!")
        """if computer's choice is 1, the game is draw"""
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nIt's a draw!")
        """if computer's choice is 2, the computer wins"""
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nYou lose!")
        """if user's choice is 2, scissors is printed"""
elif (myChoice == 2):
    print(f"You chose:\n{scissors}")
    """if computer's choice is 0, the computer wins"""
    if (computerChoice == 0):
        print(f"Computer chose:\n{rock}\nYou lose!")
        """if computer's choice is 1, the user wins"""
    elif (computerChoice == 1):
        print(f"Computer chose:\n{paper}\nYou won!")
        """if computer's choice is 2, it's a draw"""
    elif (computerChoice == 2):
        print(f"Computer chose:\n{scissors}\nIt's a draw!")
    """else prints invalid input, if none of the above is chosen by the user"""
else:
    print("Invalid input!")





