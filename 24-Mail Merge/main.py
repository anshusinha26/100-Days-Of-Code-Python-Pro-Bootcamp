# """reading a file"""
# with open("file1.txt") as file:
#     contents = file.read()
#     print(contents)

# """writing in a file"""
# with open("file1.txt", mode="w") as file:
#     file.write("I'm a python developer")

# """appending to a file"""
# with open("file1.txt", mode="a") as file:
#     file.write("\nMy name is Anshu")

# """creating a new file"""
# with open ("file2.txt", mode="w") as file:
#     file.write("This is the file2 created!")

#####

## Day24. Mail merge project

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""opens starting_letter.txt in read mode"""
with open("./Input/Letters/starting_letter.txt") as file:
    """variable to store the initial letter"""
    letter = file.read()

"""replaces [name] from the starting letter with the given names in invites_names.txt file,
creates a new letter with the new name and creates a new text file as with the new names on the letters"""
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for name in names:
        modifiedName = name.strip()
        modifiedLetter = letter.replace("[name],", f"{modifiedName},")
        with open(f"./Output/ReadyToSend/letterTo{modifiedName}.txt", mode="w") as file:
            file.write(modifiedLetter)
