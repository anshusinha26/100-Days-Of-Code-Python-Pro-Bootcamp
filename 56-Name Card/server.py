# imported Flask and render_template class from flask module
from flask import Flask, render_template

# created an instance of the Flask class and stored it in a variable called app
app = Flask(__name__)

# created a route decorator to tell Flask what URL should trigger our function
@app.route('/')
def about():
    return render_template('index.html')

# checks if the executed file is the main program and runs it
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
