#!/usr/bin/python3
"""
Starting a Flask app
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    home page return hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb page returns HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    dynamic routing returns c plus <text>
    """
    new_text = text.replace('_', ' ')
    return f"C {escape(new_text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
