# def greet():
#     print("hello");
#     print("world");
#     print("it's me");

# greet()

# def greet(name):
#     print("hello");
#     print("world");
#     print(f"it's {name}");

# name = input("Enter your name: ")
# greet(name)

# def positionalKeyWord(a, b ,c):
#     print(f"Do this with {a}")
#     print(f"Do this with {b}")
#     print(f"Do this with {c}")

# positionalKeyWord(a = 1, b = 2, c = 3)

#####

# Day 8 Project: Caesar Cipher
"""imports cc module"""
import cc

"""stores the logo"""
logo = cc.logo

"""prints the logo"""
print(logo)

"""stores all the lowercase alphabets"""
alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

"""stores the numbers"""
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

"""stores the symbols"""
symbols = [' ', "!", "@", "#", "$", "&", "?"]

"""stores all alphabets, numbers and symbols"""
allCharacters = alphabet + numbers + symbols

"""function definition"""
def casesarCipher(command, message, shift):
    """stores the encoded message"""
    encodedMessage = []
    """stores the decoded message"""
    decodedMessage = []
    """if user choses 'e', encoding starts"""
    if (command == "e"):
        """loops through the message"""
        for i in message:
            """stores the index value of the characters in the message"""
            index1 = allCharacters.index(i)
            """increases the index value of the character by shift valiue"""
            index2 = index1 + shift
            """if index2 value is more than 42, 42 is deducted from the index2, and is stored in index3 variable"""
            if (index2 > 42):
                index3 = index2 - 42
                """the new shifted character is appended to the encodedMessage list"""
                encodedMessage.append(allCharacters[index3 - 1])
                """else if the index2 value is less than or equal to 42, the character equal to index
                value of index2 is appened to the encodedMessage array"""
            elif (index2 <= 42):
                encodedMessage.append(allCharacters[index2])
        """prints the encoded result"""
        print(f"Here's the encoded result: {''.join(i for i in encodedMessage)}")
        """else if the command is to decode"""
    elif (command == "d"):
        """loops through the message"""
        for i in message:
            """stores the index value of the characters in the message"""
            index1 = allCharacters.index(i)
            """decreases the index value of the character by shift valiue"""
            index2 = index1 - shift
            """decodedMessage array is appended with the new character equal to the index value of the index2"""
            decodedMessage.append(allCharacters[index2])
        """prints the decoded result"""
        print(f"Here's the decoded result: {''.join(i for i in decodedMessage)}")
"""initially runGame variable is set to true"""
runGame = True
"""until runGame is true, this loop runs"""
while (runGame):
    command = input("Type 'e' for 'encode' of 'd' for 'decode': ").lower()
    message = input("Type your message(make sure to add only these symbols:space, !, @, #, $, &, ?): ")
    shift = int(input("Type the shift number(0-42): "))

    casesarCipher(command, message, shift)

    goAgain = input("Type 'y' for 'yes' if you want to go again, else type 'n' for 'no': ")
    if (goAgain == 'n'):
        runGame = False
        print("Caesar Cipher says: 0mmb6w2bioiqvcbowwlbvqop?\nHint: Add all the numbers in above message and use the result \nas the shift number to get the decrypted message of Caesar Cipher 😉")









# print(ord('A'))
# print(ord('Z'))