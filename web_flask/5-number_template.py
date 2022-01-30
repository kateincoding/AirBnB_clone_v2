#!/usr/bin/python3
"""module flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """print first message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """print route hbnb message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_ctext(text):
    """print a variable rule <text>"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_pythontext(text='is cool'):
    """print python default or not text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_integern(n):
    """display n only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_templaten(n):
    """routes with a template that shows the integer n"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
