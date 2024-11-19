# # imported Flask class from flask module
# from flask import Flask

# # create an instance of the Flask class
# app = Flask(__name__)

# def make_bold(function):
#     def wrapper():
#         return f"<b>{function()}</b>"
#     return wrapper

# def make_emphasis(function):
#     def wrapper():
#         return f"<em>{function()}</em>"
#     return wrapper

# def make_underlined(function):
#     def wrapper():
#         return f"<u>{function()}</u>"
#     return wrapper

# # use the route() decorator to tell Flask what URL should trigger our function
# @app.route("/")
# @make_bold
# @make_emphasis
# @make_underlined
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# # use the route() decorator to tell Flask what URL should trigger our function
# @app.route("/<name>")
# def greet(name):
#     return f"<h1>Hello {name}!</h1>"

# # check if the executed file is the main program and run the app
# if __name__ == "__main__":
#     app.run(debug=True)

# -----------------------------------------------------------
# imported Flask class from flask module
from flask import Flask

# imported random module
import random

# variable to store a random number between 0 and 9
random_number = random.randint(0, 9)

# create an instance of the Flask class
app = Flask(__name__)

# use the route() decorator to tell Flask what URL should trigger our function
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

# use the route() decorator to tell Flask what URL should trigger our function
@app.route("/<int:guess>")
def guess(guess):
    if guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    
    elif guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess == random_number:
        return "<h1 style='color: green'>You found me!</h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
        
    else:
        return "<h1 style='color: blue'>Something went wrong!</h1>" \
                "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

# check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.run(debug=True)