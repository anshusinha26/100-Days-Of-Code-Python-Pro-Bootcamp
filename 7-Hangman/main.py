"""import statements"""
import words
import hangman
import random

"""this print statement is used to print the logo from the hangman module"""
print(hangman.logo)

"""this word variable stores the random generated word from the words list from the hangman module"""
word = random.choice(words.words)

"""this print function gives the generated word"""
print(f"The answer is: {word}")

"""this variable stores the hangman inital stages from the hangman module"""
initialStage = hangman.initialStage

"""this variable hold the list of stages from the hangman module"""
stages = [hangman.stage1, hangman.stage2, hangman.stage3, hangman.stage4, hangman.stage5, hangman.stage6, hangman.stage7]

"""this variable hold the number of lives"""
lives = 7

"""this variable holds the number of _ generated which is equivalent to the number of characters of the randomly generated word"""
blankSpaces = ["_" for i in word]

"""this variable holds the stage"""
stage = initialStage

"""this variable is set to value of false"""

endOfGame = False

"""this loop will run until the game is not over"""
while (endOfGame == False):
    guess = input("Guess a letter: ")

    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                blankSpaces[i] = guess

        for i in blankSpaces:
            print(i, end='')

        print(stage)

        if "_" not in blankSpaces:
            print("You won!")
            endOfGame = True

    else :
        print(f"You guessed {guess}, that's not in the world. You lose a life!")
        for i in blankSpaces:
            print(i, end='')
        stage = stages[-lives]
        lives -= 1
        print(stage)

        if lives == 0:
            print("You lose!")
            endOfGame = True
