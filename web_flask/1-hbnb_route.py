#!/usr/bin/python3
""" A WebApp that displays different texts depending on route. """
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    This function is the route handler for the root URL ("/").
    It returns the string "Hello HBNB!" as the response.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    This function is the route handler for the "/hbnb" URL.
    It returns the string "HBNB" as the response.
    """
    return "HBNB"


if __name__ == "__main__":
    """ Run the Flask application if this file is executed directly """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
