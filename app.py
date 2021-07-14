# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request


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

@app.route('/resultspage')
def resultspage():
    props = {
        'sound': 'roar'
    }
    return render_template("resultspage.html", props=props)
