# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import pokemon_choice_message


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    props = {
        'name': 'Blaziken',
        'starts-as': 'Torchic',
        'type': 'fire'
    }
    return render_template("index.html", props=props)

@app.route('/secret')
def secret():
    return "I found mew"

@app.route('/resultspage', methods = ["GET", "POST"])
def resultspage():
    print (request.form["pokemon"])
    # props = {
    #     'sound': 'roar'
    # }
    user_choice = request.form["pokemon"]
    message = pokemon_choice_message(user_choice)
    return render_template("resultspage.html", message = message)
