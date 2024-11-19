# fruits = ["apple", "Orange", "pear"]
# for i in fruits:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

#####

# Day 5 Project: Password generator

"""import random module"""
import random
"""stores all lowercase alphabets"""
lowercaseLetters = [chr(i) for i in range(97, 123)]
"""stores all uppercase alphabets"""
uppercaseLetters = [chr(i) for i in range(65, 91)]
"""stores lowercaseletters plus uppercaseletters"""
allAlphabets = lowercaseLetters + uppercaseLetters
"""stores symbols"""
symbols = ["!", "@", "#", "%", "^", "&", "*", "=", "+", "_", "-", "/", "?"]
"""stores numbers"""
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
"""prints initial project text"""
print("Welcome to the PyPassword Generator!")
"""stores numbers of letters wanted in the password"""
numLetters = int(input("How many letters would you like in your password?\n"))
"""stored numbers of symbols wanted in the password"""
numSymbols = int(input("How many symbols would you like in your password?\n"))
"""stores the count of numbers wanted in the password"""
numNumbers = int(input("How many numbers would you like in your password?\n"))
"""stores randomly chosen letters, numbers and symbols"""
shuffledRandomList = random.choices(allAlphabets, k=numLetters) + random.choices(symbols, k=numSymbols) + random.choices(numbers, k=numNumbers)
"""shuffles the shuffledRandomList"""
random.shuffle(shuffledRandomList)
"""prints the final password"""
print(f"Here is your password: {''.join(str(i) for i in shuffledRandomList)}")

