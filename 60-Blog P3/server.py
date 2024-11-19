# -------------------- MODULES -------------------- #
# imported Flask and render_template class from flask module
from flask import Flask, render_template, request

# imported requests module to make HTTP requests
import requests

# imported datetime module as dt
import datetime as dt

# imported smtplib module
import smtplib


# -------------------- CONSTANTS -------------------- #
EMAIL = 'your_email'
PASSWORD = 'your_password'
RECEIVER = 'receiver_email'


# -------------------- BLOG DATA -------------------- #
# blog data
blog_endpoint = ' https://api.npoint.io/f8722f2418973c1bf92c'
blog_response = requests.get(blog_endpoint)
blog_data = blog_response.json()


# -------------------- CURRENT DATE -------------------- #
# getting current day, month and year
current_day = dt.datetime.now().day
current_month= dt.datetime.now().strftime("%B")
current_year = dt.datetime.now().year


# -------------------- FLASK -------------------- #
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
@app.route('/contact', methods=['Get', 'POST'])
def contact():
    # if the request method is POST then get the data from the form and send email
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # sending email
        with smtplib.SMTP('smtp.gmail.com', port=587, timeout=25) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=RECEIVER,
                msg=f'Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
            )

        return render_template('contact.html', current_year=current_year, message = "Successfully sent your message")
    # if the request method is GET then render the contact page
    else:
        return render_template('contact.html', current_year=current_year, message = "Contact me")


# checks if the executed file is the main program and runs it
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

    