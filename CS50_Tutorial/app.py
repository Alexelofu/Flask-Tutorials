from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

#create db variable that opens sports db

db = SQL("sqlite:///sports.db")

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name").title()
    sport = request.form.get("sport").title()
    if not name or sport not in SPORTS:
        return render_template("failure.html")
    
    # Allow us insert values into db

    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    # Confirm registration(redirection)
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)