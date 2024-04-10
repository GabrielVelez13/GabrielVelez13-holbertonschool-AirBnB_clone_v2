#!/usr/bin/python3
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return Response("Hello HBNB!", mimetype='text/html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
