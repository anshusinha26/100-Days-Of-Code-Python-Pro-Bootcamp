# a = 1
# def modify():
#     global a
#     a += 1
#     print(a)
# modify()

#####

# Day 12 Project: The Number Guessing Game
"""imports random moudle"""
import random
"""imports guessingGame module"""
import guessingGame
"""prints logo"""
print(guessingGame.logo)
"""prints initial project text"""
print("Welcome to The Number Guessing Game")
"""prints initial project text"""
print("I'm thinking of a number between 1 and 100.")
"""stores the random answer"""
answer = random.randint(1, 100)
"""prints the hint to the correct answer"""
print(f"Pssst, the correct answer is {answer}")
"""asks the user to chose the difficulty level of the game"""
difficultyLevel = input("Chose a difficulty level. Type 'e' for easy and 'h' for hard: ").lower()
"""if diffulty level is easy, 10 attempts are given"""
if (difficultyLevel == 'e'):
    attempts = 10
    """else if difficulty level is hard, 5 attempts are given"""
elif (difficultyLevel == 'h'):
    attempts = 5
"""unitl attempts are more than 0, the loop runs"""
while (attempts > 0):
    """prints the number of remaining attempts"""
    print(f"You have {attempts} attempts remaining to guess the number.")
    """asks the user to make a guess"""
    guess = int(input("Make a guess: "))
    """if guess is lower than the answer, too low is printed"""
    if (guess < answer):
        print("Too low.")
        """else if the guess is higher than the answer, too high is printed"""
    elif (guess > answer):
        print("Too high.")
        """else if the guess is equal to the answer, the loop ends and the user wins"""
    elif (guess == answer):
        print(f"You got it! The answer was {guess}.")
        break
    """attempts are reduced by 1, after each wrong guess"""
    attempts -= 1
"""if attempts are not left, the user loses"""
if (attempts == 0):
    print("You have run out of guesses, you lose!")








