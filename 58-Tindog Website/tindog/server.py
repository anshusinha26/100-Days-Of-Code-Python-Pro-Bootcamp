# imported Flask and render_template class from flask module
from flask import Flask, render_template

# created an instance of the Flask class and stored it in a variable called app
app = Flask(__name__)

# created a route decorator to tell Flask what URL should trigger the function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

# checks if name is the main program and runs the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)