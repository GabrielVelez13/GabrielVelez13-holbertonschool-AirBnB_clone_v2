#!/usr/bin/python3
""" This version adds route input """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """ Prints Hello. """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """ Prints C plus the text added without _"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    """ Prints Python plus the text added without _ """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """ Prints a number only if it is whole. """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def numberTemplate(n):
    """ Renders a template. """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    """ Renders a template and checks if odd or even """
    if n % 2 is 0:
        return render_template("6-number_odd_or_even.html", n=n, prop="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, prop="odd")


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000, debug=True)
