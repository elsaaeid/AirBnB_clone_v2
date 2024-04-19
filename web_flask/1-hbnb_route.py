#!/usr/bin/python3
""" class Flask """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays text on browser """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ displays text on browser """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
