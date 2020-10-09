"""app.py"""

#flask
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import login_required

from app import create_app


app = create_app()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/modulo1')
def modulo1():

    return render_template('modulo1.html')


