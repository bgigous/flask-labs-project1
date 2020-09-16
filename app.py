from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    page = "Welcome to Emily's Dog Costumes!"


@app.route('/services')
def services():
    page = "I offer custom made costumes for your precious canine companion, "\
        "and a free in-home consultation, to get the measurements."


@app.route('/costumes')
def costumes():
    page = "The costumes currently offered."
