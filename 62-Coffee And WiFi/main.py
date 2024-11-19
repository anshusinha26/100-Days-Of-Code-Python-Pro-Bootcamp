# -------------------- MODULES -------------------- #
# imported Flask and render_template class from flask module
from flask import Flask, render_template, redirect, url_for

# imported Bootstrap class from flask_bootstrap module
from flask_bootstrap import Bootstrap

# imported FlaskForm class from flask_wtf module
from flask_wtf import FlaskForm

# imported StringField and SubmitField classes from wtforms module
from wtforms import StringField, SubmitField, SelectField

# imported DataRequired class from wtforms.validators module
from wtforms.validators import DataRequired, URL

# imported csv module
import csv


# -------------------- APP CONFIG -------------------- #
# created an instance of Flask class and stored it in a variable called app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# -------------------- FORMS -------------------- #
# class for the form
class Cafe_Form(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()], choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_strength_rating = SelectField(label='Wifi Strength Rating', validators=[DataRequired()], choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_socket_availability_rating = SelectField(label='Power Socket Availability', validators=[DataRequired()], choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit')


# -------------------- ROUTES -------------------- #
# decorator function that tells the app which URL should trigger the function
@app.route("/")
def home():
    return render_template("index.html")

# decorator function that tells the app which URL should trigger the function
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    cafe_form = Cafe_Form()
    if cafe_form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_file.write(f"\n{cafe_form.cafe.data},"
                           f"{cafe_form.location.data},"
                           f"{cafe_form.open.data},"
                           f"{cafe_form.close.data},"
                           f"{cafe_form.coffee_rating.data},"
                           f"{cafe_form.wifi_strength_rating.data},"
                           f"{cafe_form.power_socket_availability_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=cafe_form)

# decorator function that tells the app which URL should trigger the function
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


# -------------------- MAIN -------------------- #
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
