"""app.py"""

#flask
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import login_required

from app import create_app


app = create_app()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/modulo1')
@login_required
def modulo1():

    return render_template('modulo1.html')


if __name__ == "__main__":
    app.run(debug=1)