# imported Flask and render_template class from flask module
from flask import Flask, render_template

# created an instance of Flask class and passed __name__ as argument
app = Flask(__name__)

# created a route for index page
@app.route('/')
def index():
    return render_template('index.html')

# check if name is main and run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)