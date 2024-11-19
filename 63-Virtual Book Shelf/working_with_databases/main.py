# # imported sqlite3 module
# import sqlite3

# # created a connection to the database
# db = sqlite3.connect("books-collection.db")

# # created a cursor object
# cursor = db.cursor()

# # # created a table
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# #
# cursor.execute("INSERT OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")

# # commit the changes
# db.commit()

# imported Flask class from flask module
from flask import Flask

# imported SQLAlchemy class
from flask_sqlalchemy import SQLAlchemy

# created an instance of Flask class
app = Flask(__name__)
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
    
# create all the tables in the database
with app.app_context():
    db.create_all()

    # create a record
    new_book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
    db.session.add(new_book)

    # commit the changes
    db.session.commit()
