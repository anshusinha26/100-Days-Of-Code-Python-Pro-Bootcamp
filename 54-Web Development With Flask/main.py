# imported Flask class from flask module
from flask import Flask

# created an instance of the Flask class
app = Flask(__name__)

# created a route decorator
@app.route("/")

# created a view function
def hello_world():
    return "Hello, World!"

# check if the executed file is the main program and run the app
if __name__ == "__main__":
    app.run()