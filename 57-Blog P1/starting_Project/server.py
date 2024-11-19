# ---------------- MODULES ---------------- #
# imported Flask and render_template class from flask module
from flask import Flask, render_template

# imported random module
import random

# imported datetime module
import datetime as dt

# imported requests module
import requests


# ---------------- FLASK APP ---------------- #

# created an instance of Flask class
app = Flask(__name__)

# created a route for index page
@app.route('/')
def index():
    random_number = random.randint(1, 100)
    now = dt.datetime.now()
    year = now.year
    return render_template('index.html', num=random_number, year=year, name='Anshu Sinha')

# created a route for name page
@app.route('/<name>')
def name(name):
    genderize_endpoint = 'https://api.genderize.io'
    genderize_response = requests.get(f'{genderize_endpoint}?name={name}')
    genderize_data = genderize_response.json()
    gender = genderize_data['gender']

    agify_endpoint = 'https://api.agify.io'
    agify_response = requests.get(f'{agify_endpoint}?name={name}')
    agify_data = agify_response.json()
    age = agify_data['age']

    return render_template('about.html', name = name, gender = gender, age = age)

@app.route('/blog/<num>')
def blog(num):
    blog_endpoint = ' https://api.npoint.io/c790b4d5cab58020d391'
    blog_response = requests.get(blog_endpoint)
    blog_data = blog_response.json()

    return render_template('blog.html', posts = blog_data)

# checking if the name of the file is main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)