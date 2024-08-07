from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)


db = SQL("sqlite:///users.db")

# Global variables
COMPOUNDS = ['Bench Press', 'OHP', 'Squat', 'Deadlift']
ASSISTANCE = ['C.G.B.P', 'Barbell Row', 'Sumo Deadlift', 'Front Squat', 'OHP']



# Base url
@app.route('/')
def index():
    # pass vars as they will be used in index.html
    return render_template('index.html', compound=COMPOUNDS, assistance=ASSISTANCE)


# Current workout plan
@app.route('/home')
def home():
    return render_template('home.html')

# if url.method == POST
@app.route('/register', methods=["POST"])
def register():

    # if error return exit
    if not request.form.get('name') or request.form.get('compound') not in COMPOUNDS or request.form.get('assistance') not in ASSISTANCE:
        return "<h1>Error form data missing </h1>"

    # get form post data
    name = request.form.get('name')
    compound = request.form.get('compound')
    assistance = request.form.get('assistance')


    # run sql commands on users.db
    db.execute("INSERT INTO registrants (name, compound, assistance) VALUES(?,?,?)", name,compound,assistance)

    # Select all from registrants table
    registrants = db.execute("SELECT * FROM registrants")

    # seperate vars with ,
    return render_template('register.html', users=registrants)


@app.route('/users')
def users():

    registrants = db.execute("SELECT * FROM registrants")

    return render_template('users.html', users=registrants)
