# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# """imported csv module"""
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# """imported pandas module"""
# import pandas
#
# """using pandas module to read a csv file"""
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# """converting the data to dictionary format"""
# dataDict = data.to_dict()
# print(dataDict)

# """converting the data to a list"""
# tempList = data["temp"].to_list()
# sum = 0
# for temp in tempList:
#     sum += temp
# avgTemp = sum / len(tempList)
# print(round(avgTemp, 2))

# avgTemp = sum(tempList) / len(tempList)
# print(round(avgTemp, 2))

# """getting the avg temperature"""
# print(
#     round(
#         data["temp"].mean(), 2
#     )
# )
#
# """getting the maximum value from the data's temp column"""
# print(
#     data["temp"].max()
# )
#
# """getting the data in a column"""
# print(
#     data.condition
# )

# """getting the data in a row"""
# print(
#     data[data.day == "Monday"]
# )

# print(
#     data[data.temp == data.temp.max()]
# )

# """getting the condition of a single row"""
# monday = data[data.day == "Monday"]
# print(monday.condition)

# """creating a dataframe from scratch"""
# dataDict = {
#     "students": ["Anuragini", "Arup", "Bibek", "Aadarsh"],
#     "age": [19, 20, 21, 21]
# }
#
# data2 = pandas.DataFrame(dataDict)
# print(data2)
#
# """converting the obtained data to csv format"""
# print(
#     data2.to_csv()
# )

#####

# """the great squirrel census data analysis"""
# """imported pandas module"""
# import pandas
#
# """using pandas to read the data and store it in a variable"""
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# """getting the rows"""
# Gray = data[data["Primary Fur Color"] == "Gray"]
# Red = data[data["Primary Fur Color"] == "Cinnamon"]
# Black = data[data["Primary Fur Color"] == "Black"]
#
# """getting the length of all the required colors"""
# numGray = len(Gray)
# numRed = len(Red)
# numBlack = len(Black)
#
# dataDict = {
#     "Fur color": ["Gray", "Red", "Black"],
#     "Count": [numGray, numRed, numBlack],
# }
#
# newSquirrelData = pandas.DataFrame(dataDict)
# newSquirrelData.to_csv("squirrelsCount.csv", index = False)

#####

"""India's states game"""
# ------------------------------------------------
"""imported turtle module"""
import turtle

"""imported Screen class from the turtle module"""
from turtle import Screen

"""imported pandas module"""
import pandas
# ------------------------------------------------


# ------------------------------------------------
"""constants"""
ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")
# ------------------------------------------------


# ------------------------------------------------
"""image"""
image = "Indian_Political_Map_March_2022.gif"

"""created tim object"""
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

"""created screen object"""
screen = Screen()
screen.title("India's states game")
screen.setup(width=800, height=800)
screen.addshape(image)

"""turtle takes the shape of the image"""
turtle.shape(image)
# ------------------------------------------------


# ------------------------------------------------
# """function for converting the initials of the answer to uppercase"""
# def toPascalCase(word):
#     words = word.split(" ")
#     words = [w.capitalize() for w in words]
#
#     newWord = " ".join(words)
#
#     return newWord
#
# newAnswer = toPascalCase(answerState)
# ------------------------------------------------


# ------------------------------------------------
"""variable to store the state's data"""
data = pandas.read_csv("indianStates.csv")

"""list to store the state's name"""
statesList = data.state.to_list()

"""list to store the x position"""
xPosList = data.x.to_list()

"""list to store the y position"""
yPosList = data.y.to_list()
# ------------------------------------------------


# ------------------------------------------------
"""list to store the states which has been answered"""
answeredStates = []

while len(answeredStates) < 28:

    """variable to take and store the answer"""
    answerState = screen.textinput(title=f"Guess the state:  {len(answeredStates)}/{len(statesList)} states correct", prompt="What's the name of the another state?").title()

    if answerState in statesList and answerState not in answeredStates:
        answeredStates.append(answerState)
        index = statesList.index(answerState)
        xPos = xPosList[index]
        yPos = yPosList[index]
        tim.goto(xPos, yPos)
        tim.write(answerState, align=ALIGNMENT, font=FONT)

    elif answerState == "Exit":
        notAnsweredState = [state for state in statesList if state not in answeredStates]
        data2 = pandas.DataFrame(notAnsweredState)
        data2.to_csv("MissingStates.csv")

        break

"""screen will exit on click"""
screen.exitonclick()
# ------------------------------------------------


# ------------------------------------------------
# """function to find the coordinates according to
# the click on specific position of the screen"""
# def getMouseClickCoordinate(x, y):
#     print(x, y)
#
# turtle.onscreenclick(getMouseClickCoordinate)
# turtle.mainloop()
# ------------------------------------------------