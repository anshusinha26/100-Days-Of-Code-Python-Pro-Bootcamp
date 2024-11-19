# imported Flask and render_template class from flask module
from flask import Flask, render_template

# imported FlaskForm class from flask_wtf module
from flask_wtf import FlaskForm

# imported StringField class from wtforms module
from wtforms import StringField, PasswordField, SubmitField

# imported DataRequired class from wtforms.validators module
from wtforms.validators import DataRequired, Email, Length

# imported Bootstrap class 
from flask_bootstrap import Bootstrap

# created an instance of the Flask class and stored it in a variable called app and created an instance of the Bootstrap class
app = Flask(__name__)
Bootstrap(app)

# variable to store the secret key
app.secret_key = 'dfvwejnilo3442-hjguuiuygl32r23!@#'

"""class to create a form with a username and password field"""
class Login_Form(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email('Invalid email address!')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit=SubmitField(label='Log In')

# created a route decorator to tell Flask what URL should trigger our function
@ app.route("/")
def home():
    return render_template('index.html')

# created a route decorator to tell Flask what URL should trigger our function
@ app.route("/login", methods=['GET', 'POST'])
def login():
    login_form=Login_Form()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html', form=login_form)


# check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
