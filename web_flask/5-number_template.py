#!/usr/bin/python3
"""
Starting a Flask app
"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    dynamic routing returns c plus <text>
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Displays python followed by the value of text
    """
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays n is a number only if n is an integer
    """
    return "{} is a number".format(n)


@app.route('/number/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
