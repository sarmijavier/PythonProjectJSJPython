from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='templates', static_folder='static')
bootstrap = Bootstrap(app) 


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=1)