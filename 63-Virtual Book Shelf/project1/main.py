# imported Flask, render_template, request, redirect, url_for class from flask module
from flask import Flask, render_template, request, redirect, url_for

# imported SQLAlchemy class
from flask_sqlalchemy import SQLAlchemy

# created an instance of Flask class
app = Flask(__name__)

# set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# created an instance of SQLAlchemy class
db = SQLAlchemy(app)

# create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    db.create_all()

# route decorator to tell Flask what URL should trigger the function
@app.route('/')
def home():
    return render_template("index.html", books=db.session.query(Book).all())

# route decorator to tell Flask what URL should trigger the function
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        # get the data from the form
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        # create a record
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        # redirect to the home page
        return redirect(url_for('home'))
    return render_template("add.html")

# route decorator to tell Flask what URL should trigger the function
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected)

# route decorator to tell Flask what URL should trigger the function
@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# checks if name of the function is main and run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

