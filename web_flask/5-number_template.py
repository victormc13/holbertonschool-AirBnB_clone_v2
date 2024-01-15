#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays the greeting message 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Displays 'C ' followed by the value of the text variable."""
    return f'C {escape(text.replace("_", " "))}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python_text(text='is_cool'):
    """Displays 'Python ' followed by the value of the text variable."""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Displays 'n is a number' only if n is an integer."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Displays a HTML page only if n is an integer
    with an H1 tag: 'Number: n' inside the BODY tag.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
