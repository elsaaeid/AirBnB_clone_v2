#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays text
    'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """displays text
    'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ display text
    'C'
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """display text
    'python'
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """displays text
    Args is number
    Returns string
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML(n):
    """displays text
    Returns HTML page
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
