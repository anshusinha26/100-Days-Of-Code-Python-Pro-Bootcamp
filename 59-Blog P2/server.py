# imported Flask and render_template class from flask module
from flask import Flask, render_template

# imported requests module to make HTTP requests
import requests

# imported datetime module as dt
import datetime as dt

# blog data
blog_endpoint = ' https://api.npoint.io/f8722f2418973c1bf92c'
blog_response = requests.get(blog_endpoint)
blog_data = blog_response.json()

# getting current day, month and year
current_day = dt.datetime.now().day
current_month= dt.datetime.now().strftime("%B")
current_year = dt.datetime.now().year

# created an instance of the Flask class and stored it in a variable called app
app = Flask(__name__)

# created a route decorator to tell Flask what URL should trigger our function
@app.route('/')
def index():
    return render_template('index.html', posts=blog_data, current_day=current_day, current_month=current_month, current_year=current_year)

# created a route decorator to tell Flask what URL should trigger our function
@app.route('/post/<int:index>')
def post(index):
    for post in blog_data:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post, current_day=current_day, current_month=current_month, current_year=current_year)

# created a route decorator to tell Flask what URL should trigger our function
@app.route('/about')
def about():
    return render_template('about.html', current_year=current_year)

# created a route decorator to tell Flask what URL should trigger our function
@app.route('/contact')
def contact():
    return render_template('contact.html', current_year=current_year)


# checks if the executed file is the main program and runs it
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

    