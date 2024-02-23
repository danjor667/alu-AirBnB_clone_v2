#!/usr/bin/python3
"""doc"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """doc"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """doc"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """doc"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Displays python followed by the value of text"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays n is a number only if n is an integer"""
    return f"{n} is a number"


@app.route('/number/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays HTML page if n is an integer and odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               n=n, status='even')
    else:
        return render_template('6-number_odd_or_even.html',
                               n=n, status='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
