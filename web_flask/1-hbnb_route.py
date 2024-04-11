#!/usr/bin/python3
from flask import Flask

"""  Create an instance of the Flask class """
app = Flask(__name__)

""" Define a route for the root URL ("/") and disable strict slashes """
@app.route('/')
def hello_hbnb():
    """
    This function is the route handler for the root URL ("/").
    It returns the string "Hello HBNB!" as the response.
    """
    return "Hello HBNB!"

""" Define a route for the "/hbnb" URL and disable strict slashes """
@app.route('/hbnb')
def hbnb():
    """
    This function is the route handler for the "/hbnb" URL.
    It returns the string "HBNB" as the response.
    """
    return "HBNB"

""" Run the Flask application if this file is executed directly """
if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
