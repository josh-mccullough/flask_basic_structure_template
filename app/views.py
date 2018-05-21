from flask import request, render_template, session, redirect
from .database.database_controller import Database
from app import app

db = Database('database_name')  # TODO connect to a database sure


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        pass

    elif request.method == "POST":
        pass

    else:
        print "neither post or get, im confused"
