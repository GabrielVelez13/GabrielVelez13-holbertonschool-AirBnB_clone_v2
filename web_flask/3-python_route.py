#!/usr/bin/python3
""" This version adds route input """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
