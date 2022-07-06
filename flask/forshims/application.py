from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

SPORTS = ['Tennis', 'Baseball', 'Dodgeball', 'Soccer']
db = SQL("sqlite:///froshims.db")



@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)



@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not request.form.get('name') or request.form.get('sport') not in SPORTS:
        return "<h1>Form failure</h1>"

    db.execute("INSERT INTO registrants (name,sport) VALUES (?,?)", name, sport)

    return redirect("/registrants")

@app.route('/registrants')
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("/registrants.html", registrants=registrants)






