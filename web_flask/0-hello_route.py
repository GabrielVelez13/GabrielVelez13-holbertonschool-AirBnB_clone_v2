#!/usr/bin/python3
""" A WebApp that displays a special hello world. """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ Prints into a special hello world. """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
